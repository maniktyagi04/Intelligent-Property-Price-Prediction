# 🚀 Quick Start Guide

## Your Application is Running! 🎉

### 📍 Access Your Application

**Frontend (Main App)**: http://localhost:5173

**Backend API**: http://localhost:8000

**API Documentation**: http://localhost:8000/docs

---

## 🎯 How to Use

### 1. Property Price Prediction
1. Go to http://localhost:5173
2. Fill in the property details form:
   - Area (sq ft)
   - Number of bedrooms, bathrooms, stories
   - Parking spaces
   - Select amenities (guest room, main road access, etc.)
3. Click "Predict Price"
4. View the predicted price

### 2. Legal Advisor Chat
1. Click "Legal Advisor" in the navigation
2. Type your real estate legal questions
3. Get AI-powered responses

---

## ⚠️ Enable AI Features

Currently, AI features show a warning because the Groq API key is not set.

**To enable AI advisory and legal chat:**

1. Get a free API key from: https://console.groq.com/
2. Open `backend/.env` file
3. Replace this line:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
   With your actual key:
   ```
   GROQ_API_KEY=gsk_your_actual_key_here
   ```
4. Save the file (backend will auto-reload)
5. Refresh your browser

---

## 🛑 Stop the Servers

When you're done testing:

1. Go back to your terminal/IDE
2. Press `Ctrl+C` in both terminal windows (backend and frontend)

Or if using the IDE, stop the running processes.

---

## 📊 Test Data Examples

Try these property configurations:

**Luxury Property:**
- Area: 8000 sq ft
- Bedrooms: 4
- Bathrooms: 3
- Stories: 3
- Parking: 2
- All amenities: Yes
- Furnishing: Furnished

**Budget Property:**
- Area: 2000 sq ft
- Bedrooms: 2
- Bathrooms: 1
- Stories: 1
- Parking: 0
- Most amenities: No
- Furnishing: Unfurnished

---

## 🔍 Troubleshooting

**Frontend not loading?**
- Check if http://localhost:5173 is accessible
- Make sure the frontend server is running

**Backend errors?**
- Check if http://localhost:8000/docs is accessible
- Make sure the backend server is running
- Check backend terminal for error messages

**AI features not working?**
- Verify your Groq API key is set in `backend/.env`
- Check that the key is valid at https://console.groq.com/

---

## 📚 More Information

- Full setup instructions: `SETUP_INSTRUCTIONS.md`
- Project status: `PROJECT_STATUS.md`
- Original README: `README.md`

---

**Enjoy testing your Intelligent Property Price Prediction System! 🏡**
