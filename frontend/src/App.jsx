import { useEffect, useRef, useState } from 'react'
import {
  Bath,
  BedDouble,
  Building2,
  Car,
  CheckCircle2,
  Home,
  Landmark,
  MapPin,
  MessageSquare,
  Send,
  Sparkles,
  Trees,
  UserRound,
  Waves,
} from 'lucide-react'

const initialForm = {
  area: '',
  bedrooms: '',
  bathrooms: '',
  stories: '',
  parking: '',
  guestroom: 'No',
  mainroad: 'No',
  prefarea: 'No',
  basement: 'No',
  airconditioning: 'No',
  furnishingstatus: 'furnished',
}

const toggles = ['guestroom', 'mainroad', 'prefarea', 'basement', 'airconditioning']
const MAX_QUERY_LENGTH = 1200

const toINR = (value) =>
  new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0,
  }).format(value)

function App() {
  const [form, setForm] = useState(initialForm)
  const [prediction, setPrediction] = useState(null)
  const [errors, setErrors] = useState('')

  const [chatInput, setChatInput] = useState('')
  const [chatLoading, setChatLoading] = useState(false)
  const [chatHistory, setChatHistory] = useState([])

  const resultRef = useRef(null)
  const chatRef = useRef(null)

  const apiBase =
    import.meta.env.VITE_API_BASE_URL ||
    `${window.location.protocol}//${window.location.hostname || 'localhost'}:8000`

  useEffect(() => {
    if (prediction) {
      resultRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }, [prediction])

  useEffect(() => {
    if (chatRef.current) {
      chatRef.current.scrollTop = chatRef.current.scrollHeight
    }
  }, [chatHistory])

  const updateField = (key, value) => {
    setForm((prev) => ({ ...prev, [key]: value }))
  }

  const handlePredict = (event) => {
    event.preventDefault()
    setErrors('')

    const numeric = {
      area: Number(form.area),
      bedrooms: Number(form.bedrooms),
      bathrooms: Number(form.bathrooms),
      stories: Number(form.stories),
      parking: Number(form.parking),
    }

    if (Object.values(numeric).some((value) => Number.isNaN(value) || value < 0)) {
      setErrors('Please enter valid numeric values for all property details.')
      return
    }

    if (!numeric.area || !numeric.bedrooms || !numeric.bathrooms || !numeric.stories) {
      setErrors('Area, bedrooms, bathrooms, and stories are required.')
      return
    }

    const amenityCount = toggles.filter((item) => form[item] === 'Yes').length
    const furnishingFactor =
      form.furnishingstatus === 'furnished'
        ? 1.12
        : form.furnishingstatus === 'semi-furnished'
          ? 1.05
          : 0.95

    const base = numeric.area * 3500
    const structure =
      numeric.bedrooms * 300000 +
      numeric.bathrooms * 220000 +
      numeric.stories * 180000 +
      numeric.parking * 120000
    const amenities = amenityCount * 150000

    const estimatedPrice = Math.round((base + structure + amenities) * furnishingFactor)

    const factors = [
      {
        icon: Building2,
        label: `Built-up area strength: ${numeric.area.toLocaleString()} sq ft`,
      },
      {
        icon: MapPin,
        label:
          form.mainroad === 'Yes' || form.prefarea === 'Yes'
            ? 'Location premium from road/preferred zone access'
            : 'Limited location premium due to access profile',
      },
      {
        icon: Sparkles,
        label: `${amenityCount} lifestyle amenities positively impacting value`,
      },
    ]

    const explanation = `Based on your configuration, the estimate is driven by property size, room composition, amenity score, and furnishing profile. Higher connectivity and feature-rich homes generally command a stronger market valuation, while moderate amenities and unfinished interiors reduce pricing power. This estimate is directional and should be validated with current local transactions.`

    setPrediction({ estimatedPrice, factors, explanation })
  }

  const askLegalAdvisor = async (event) => {
    event.preventDefault()

    if (!chatInput.trim()) return

    const userMessage = chatInput.trim()
    setChatInput('')

    if (userMessage.length > MAX_QUERY_LENGTH) {
      setChatHistory((prev) => [
        ...prev,
        { role: 'user', text: userMessage },
        {
          role: 'ai',
          text: 'Please shorten your question so I can process it reliably.',
        },
      ])
      return
    }

    setChatHistory((prev) => [...prev, { role: 'user', text: userMessage }])
    setChatLoading(true)

    try {
      const response = await fetch(`${apiBase}/rag?query=${encodeURIComponent(userMessage)}`)
      if (!response.ok) {
        throw new Error('API error')
      }

      const data = await response.json()
      const reply = data.context || 'No legal context available for this query yet.'
      setChatHistory((prev) => [...prev, { role: 'ai', text: reply }])
    } catch {
      setChatHistory((prev) => [
        ...prev,
        {
          role: 'ai',
          text: 'I could not reach the legal backend right now. Please run the FastAPI service and try again.',
        },
      ])
    } finally {
      setChatLoading(false)
    }
  }

  const textInputClass =
    'w-full rounded-2xl border border-[#E6E1D9] bg-white py-3.5 pl-11 pr-4 text-sm text-[#2B2B2B] outline-none transition focus:border-[#5DBB9A] focus:ring-4 focus:ring-[#5DBB9A]/20'

  const selectClass =
    'w-full rounded-2xl border border-[#E6E1D9] bg-white py-3.5 px-4 text-sm text-[#2B2B2B] outline-none transition focus:border-[#5DBB9A] focus:ring-4 focus:ring-[#5DBB9A]/20'

  return (
    <main className="min-h-screen bg-[#F9F7F4] text-[#2B2B2B]">
      <div className="mx-auto flex w-full max-w-6xl flex-col gap-8 px-4 py-8 sm:px-6 lg:px-8 lg:py-10">
        <header className="rounded-2xl bg-white p-6 shadow-[0_10px_30px_rgba(0,0,0,0.06)] sm:p-8">
          <h1 className="text-2xl font-bold tracking-tight text-[#1F2937] sm:text-4xl">
            Intelligent Property Price Prediction System
          </h1>
          <p className="mt-3 text-sm text-[#5D5D5D] sm:text-base">
            Smart valuation and legal guidance in one clean workflow.
          </p>
        </header>

        <section className="rounded-2xl bg-white p-6 shadow-[0_10px_30px_rgba(0,0,0,0.06)] sm:p-8">
          <div className="mb-6 flex items-center gap-3">
            <Home className="h-5 w-5 text-[#5DBB9A]" />
            <h2 className="text-xl font-semibold text-[#1F2937]">Property Details</h2>
          </div>

          <form onSubmit={handlePredict} className="space-y-6">
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              {[
                { key: 'area', label: 'Area (sq ft)', icon: Landmark, type: 'number', min: 1 },
                { key: 'bedrooms', label: 'Bedrooms', icon: BedDouble, type: 'number', min: 1 },
                { key: 'bathrooms', label: 'Bathrooms', icon: Bath, type: 'number', min: 1 },
                { key: 'stories', label: 'Stories', icon: Building2, type: 'number', min: 1 },
                { key: 'parking', label: 'Parking Spaces', icon: Car, type: 'number', min: 0 },
              ].map((item) => (
                <label key={item.key} className="space-y-2">
                  <span className="text-sm font-medium text-[#3C3C3C]">{item.label}</span>
                  <div className="relative">
                    {item.icon && (
                      <item.icon className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#8A8A8A]" />
                    )}
                    <input
                      type="number"
                      min={item.min}
                      value={form[item.key]}
                      onChange={(event) => updateField(item.key, event.target.value)}
                      className={textInputClass}
                      required={item.key !== 'parking'}
                    />
                  </div>
                </label>
              ))}
            </div>

            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              {[
                { key: 'guestroom', label: 'Guest Room' },
                { key: 'mainroad', label: 'Main Road Access' },
                { key: 'prefarea', label: 'Preferred Area' },
                { key: 'basement', label: 'Basement' },
                { key: 'airconditioning', label: 'Air Conditioning' },
              ].map(({ key, label }) => (
                <label key={key} className="space-y-2">
                  <span className="text-sm font-medium text-[#3C3C3C]">{label}</span>
                  <select
                    value={form[key]}
                    onChange={(event) => updateField(key, event.target.value)}
                    className={selectClass}
                  >
                    <option>No</option>
                    <option>Yes</option>
                  </select>
                </label>
              ))}

              <label className="space-y-2">
                <span className="text-sm font-medium text-[#3C3C3C]">Furnishing Status</span>
                <select
                  value={form.furnishingstatus}
                  onChange={(event) => updateField('furnishingstatus', event.target.value)}
                  className={selectClass}
                >
                  <option value="furnished">Furnished</option>
                  <option value="semi-furnished">Semi-furnished</option>
                  <option value="unfurnished">Unfurnished</option>
                </select>
              </label>
            </div>

            {errors && (
              <p className="rounded-2xl bg-[#FDE7E2] px-4 py-3 text-sm text-[#8A3B2F]">{errors}</p>
            )}

            <button
              type="submit"
              className="inline-flex items-center gap-2 rounded-2xl bg-gradient-to-r from-[#5DBB9A] to-[#4BAA88] px-6 py-3 text-sm font-semibold text-white shadow-[0_10px_20px_rgba(93,187,154,0.35)] transition hover:-translate-y-0.5 hover:shadow-[0_14px_24px_rgba(93,187,154,0.4)]"
            >
              <Sparkles className="h-4 w-4" />
              Predict Price
            </button>
          </form>
        </section>

        <section
          ref={resultRef}
          className={`rounded-2xl bg-gradient-to-br from-[#FFF6F2] to-[#FCE8E2] p-6 shadow-[0_10px_30px_rgba(0,0,0,0.06)] transition-all duration-500 sm:p-8 ${
            prediction ? 'translate-y-0 opacity-100' : 'pointer-events-none -translate-y-2 opacity-0'
          }`}
        >
          <div className="mb-5 flex items-center gap-3">
            <CheckCircle2 className="h-5 w-5 text-[#D67B63]" />
            <h2 className="text-xl font-semibold text-[#1F2937]">Prediction Result</h2>
          </div>

          {prediction && (
            <>
              <p className="text-sm text-[#6A6A6A]">Estimated Price</p>
              <p className="mt-1 text-3xl font-bold text-[#1F2937] sm:text-4xl">
                {toINR(prediction.estimatedPrice)}
              </p>

              <div className="mt-6 grid gap-3 md:grid-cols-3">
                {prediction.factors.map((factor) => (
                  <article key={factor.label} className="rounded-2xl bg-white/70 p-4">
                    {factor.icon && <factor.icon className="mb-2 h-5 w-5 text-[#D67B63]" />}
                    <p className="text-sm text-[#333]">{factor.label}</p>
                  </article>
                ))}
              </div>

              <div className="mt-6 rounded-2xl bg-white/80 p-4">
                <p className="text-sm leading-relaxed text-[#444]">{prediction.explanation}</p>
              </div>
            </>
          )}
        </section>

        <div className="flex items-center gap-4 px-1">
          <div className="h-px flex-1 bg-[#D9D2C6]" />
          <p className="text-sm font-medium tracking-wide text-[#7D766A]">Legal Guidance</p>
          <div className="h-px flex-1 bg-[#D9D2C6]" />
        </div>

        <section className="rounded-2xl bg-white p-6 shadow-[0_10px_30px_rgba(0,0,0,0.06)] sm:p-8">
          <div className="mb-6 flex items-center gap-3">
            <MessageSquare className="h-5 w-5 text-[#5DBB9A]" />
            <h2 className="text-xl font-semibold text-[#1F2937]">Legal Property Advisor</h2>
          </div>

          <form onSubmit={askLegalAdvisor} className="mb-4 flex flex-col gap-3 sm:flex-row">
            <div className="relative flex-1">
              <UserRound className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#8A8A8A]" />
              <input
                type="text"
                value={chatInput}
                onChange={(event) => setChatInput(event.target.value)}
                placeholder="Ask legal property questions"
                className="w-full rounded-2xl border border-[#E6E1D9] bg-white py-3.5 pl-11 pr-4 text-sm outline-none transition focus:border-[#5DBB9A] focus:ring-4 focus:ring-[#5DBB9A]/20"
              />
            </div>

            <button
              type="submit"
              disabled={chatLoading}
              className="inline-flex items-center justify-center gap-2 rounded-2xl bg-gradient-to-r from-[#5DBB9A] to-[#4BAA88] px-5 py-3 text-sm font-semibold text-white shadow-[0_10px_20px_rgba(93,187,154,0.35)] transition hover:-translate-y-0.5 hover:shadow-[0_14px_24px_rgba(93,187,154,0.4)] disabled:cursor-not-allowed disabled:opacity-70"
            >
              <Send className="h-4 w-4" />
              {chatLoading ? 'Asking...' : 'Ask'}
            </button>
          </form>

          <div
            ref={chatRef}
            className="max-h-[340px] space-y-3 overflow-y-auto rounded-2xl border border-[#EEE7DC] bg-[#FCFBF8] p-4"
          >
            {chatHistory.length === 0 ? (
              <p className="text-sm text-[#727272]">
                Start a conversation to get legal context for your property decisions.
              </p>
            ) : (
              chatHistory.map((message, index) => (
                <div
                  key={`${message.role}-${index}`}
                  className={`max-w-[90%] rounded-2xl px-4 py-3 text-sm leading-relaxed shadow-sm ${
                    message.role === 'user'
                      ? 'ml-auto bg-[#5DBB9A] text-white'
                      : 'mr-auto bg-white text-[#2F2F2F]'
                  }`}
                >
                  {message.text}
                </div>
              ))
            )}
          </div>

          <div className="mt-5 grid gap-3 text-xs text-[#6F6F6F] sm:grid-cols-3">
            <div className="flex items-center gap-2 rounded-2xl bg-[#F7F3EC] p-3">
              <MapPin className="h-4 w-4 text-[#D67B63]" />
              Title checks
            </div>
            <div className="flex items-center gap-2 rounded-2xl bg-[#F7F3EC] p-3">
              <Waves className="h-4 w-4 text-[#D67B63]" />
              Zoning guidance
            </div>
            <div className="flex items-center gap-2 rounded-2xl bg-[#F7F3EC] p-3">
              <Trees className="h-4 w-4 text-[#D67B63]" />
              Tax & registry hints
            </div>
          </div>
        </section>

        <footer className="pb-4 text-center text-xs text-[#8A8A8A]">
          Designed for intelligent property analysis and legal-aware decision support.
        </footer>
      </div>
    </main>
  )
}

export default App
