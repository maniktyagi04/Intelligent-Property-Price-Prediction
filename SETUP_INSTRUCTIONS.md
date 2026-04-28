# Setup Instructions

## Prerequisites
- Python 3.8+
- Node.js 16+
- Groq API Key (get one from https://console.groq.com/)

## Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the `backend` directory with your Groq API key:
```
GROQ_API_KEY=your_actual_groq_api_key_here
```

5. Start the backend server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at: http://localhost:8000

## Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at: http://localhost:5173

## Testing the Application

1. Open your browser and go to http://localhost:5173
2. You'll see two pages:
   - **Home (Predict)**: Enter property details to get price predictions
   - **Legal Advisor**: Ask questions about real estate law

## Features

- **Price Prediction**: Uses a trained ML model to predict property prices
- **AI Advisory**: Provides intelligent insights about the property (requires valid Groq API key)
- **Legal Advisor**: RAG-powered chatbot for real estate legal questions (requires valid Groq API key)

## Notes

- The application will work without a Groq API key, but AI features will show warning messages
- Make sure both backend and frontend servers are running
- The ML model is already included in the `models` directory
