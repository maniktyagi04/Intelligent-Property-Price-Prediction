# 🏡 Intelligent Property Price Prediction and Advisory System

## 📌 Overview

This project is a full-stack AI-driven application designed to predict real estate property prices and provide intelligent advisory insights. It combines machine learning models with modern backend architecture and LLM-based reasoning to deliver accurate predictions along with contextual explanations.

The system enables users to input property details and receive:

* Predicted property price
* AI-generated insights and recommendations
* Domain-specific advisory using a lightweight RAG pipeline

---

## 🚀 Features

* 📊 Machine Learning-based property price prediction
* ⚙️ FastAPI backend with RESTful APIs
* 🌐 React (Vite) frontend for user interaction
* 🤖 LLM integration (Llama 3 via Groq) for intelligent insights
* 📚 Lightweight RAG-based advisory system using domain knowledge
* ☁️ Deployment: Frontend on Vercel, Backend on Render

---

## 🧠 Tech Stack

### Backend

* FastAPI
* Python
* Pydantic

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Frontend

* React (Vite)

### AI / LLM

* Groq API
* Llama 3

### Deployment

* Vercel (Frontend)
* Render (Backend)

---

## ⚙️ Machine Learning Pipeline

* Data preprocessing and cleaning
* Feature engineering and encoding
* Feature selection using model-based importance
* Model training and comparison:

  * Linear Regression
  * Decision Tree Regressor
  * Random Forest Regressor
* Model evaluation and selection
* Model serialization for inference

---

## 🤖 LLM & RAG Integration

* Integrated Llama 3 using Groq API for generating contextual insights
* Implemented prompt engineering for property-specific recommendations
* Built a lightweight RAG pipeline using domain-specific knowledge files
* Injected contextual data into prompts to enhance response relevance

---

## 🌐 API Endpoints

* `/predict` → Predict property price
* `/insights` → Generate AI-based insights
* `/rag` → Answer real estate queries using contextual knowledge

---

## 📂 Project Structure

```
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
│   ├── utils/
│   └── data/
├── frontend/
│   ├── src/
│   ├── components/
│   └── pages/
├── dataset/
├── models/
└── README.md
```

---

## 📊 Dataset

* Dataset used for training the model:
  https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

---

## 🌍 Deployment Links

* Frontend (Vercel): https://frontend-eta-six-kjtjs91us4.vercel.app/
* Backend (Render): https://intelligent-property-backend.onrender.com

---

## 🛠️ Setup Instructions

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 📈 Future Improvements

* Integrate vector database (FAISS/Chroma) for advanced RAG
* Improve feature engineering and model accuracy
* Add authentication and user management
* Enhance UI/UX for better user experience

---

## 📌 Conclusion

This project demonstrates the integration of machine learning, backend engineering, and LLM-based reasoning into a single scalable system. It showcases practical implementation of real-world AI applications in the real estate domain.

---
