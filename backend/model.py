import os
import joblib
import pandas as pd
from langchain_groq import ChatGroq

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "..", "models", "best_house_price_model.pkl")

try:
    model, model_name, top_features = joblib.load(model_path)
except Exception as e:
    model, model_name, top_features = None, None, None
    print(f"Warning: Model could not be loaded from {model_path}. Error: {e}")

llm = None

def get_llm():
    global llm
    if llm is None:
        try:
            llm = ChatGroq(
                model="llama-3.3-70b-versatile",
                temperature=0
            )
        except Exception as e:
            print(f"Warning: Could not initialize LLM. Error: {e}")
            llm = False
    return llm if llm is not False else None

def predict_price(request, predict_only=False):
    if model is None:
        raise ValueError("Model is not loaded.")
        
    semi = 1 if request.furnishingstatus == "semi-furnished" else 0
    unfurnished = 1 if request.furnishingstatus == "unfurnished" else 0

    input_dict = {
        "area": request.area,
        "bedrooms": request.bedrooms,
        "guestroom": 1 if request.guestroom == "Yes" else 0,
        "bathrooms": request.bathrooms,
        "mainroad": 1 if request.mainroad == "Yes" else 0,
        "prefarea": 1 if request.prefarea == "Yes" else 0,
        "stories": request.stories,
        "parking": request.parking,
        "basement": 1 if request.basement == "Yes" else 0,
        "airconditioning": 1 if request.airconditioning == "Yes" else 0,
        "furnishingstatus_semi-furnished": semi,
        "furnishingstatus_unfurnished": unfurnished
    }

    input_data = pd.DataFrame([input_dict])
    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=top_features, fill_value=0)

    prediction = model.predict(input_data)[0]

    if predict_only:
        return {"prediction": float(prediction), "advisory": ""}
    
    llm_instance = get_llm()
    
    # Try to use AI first
    if llm_instance is not None:
        try:
            prompt = f"""
    You are a professional and responsible real estate advisor.

    RULES:
    - Do NOT guarantee profits
    - Mention risks clearly
    - Keep advice realistic

    Property Details:
    Area: {request.area}
    Bedrooms: {request.bedrooms}
    Bathrooms: {request.bathrooms}
    Stories: {request.stories}
    Parking: {request.parking}
    Main Road: {request.mainroad}
    Preferred Area: {request.prefarea}
    Furnishing: {request.furnishingstatus}

    Predicted Price: ₹ {round(prediction, 2)}

    Generate:
    1. Property Summary
    2. Price Insight
    3. Market Trends
    4. Recommendation
    5. Risks
    """

            advisory = llm_instance.invoke(prompt).content
            
            return {
                "prediction": float(prediction),
                "advisory": advisory
            }
        except Exception as e:
            print(f"AI generation failed: {e}")
            # Fall through to mock advisory
    
    # Generate mock advisory if AI fails
    furnishing_desc = request.furnishingstatus.replace("-", " ").title()
    amenities = []
    if request.guestroom == "Yes":
        amenities.append("guest room")
    if request.basement == "Yes":
        amenities.append("basement")
    if request.airconditioning == "Yes":
        amenities.append("air conditioning")
    
    amenities_text = ", ".join(amenities) if amenities else "basic amenities"
    
    location_features = []
    if request.mainroad == "Yes":
        location_features.append("main road access")
    if request.prefarea == "Yes":
        location_features.append("preferred area")
    
    location_text = " and ".join(location_features) if location_features else "standard location"
    
    mock_advisory = f"""Property Summary: The property in question is a {request.bedrooms}-bedroom, {request.bathrooms}-bathroom, {request.stories}-story unit, spanning an area of {request.area} square feet. It comes with {request.parking} parking space(s) and features {amenities_text}. The property is {furnishing_desc.lower()}, located with {location_text}, which could be an attractive feature for potential buyers or renters looking for convenience and comfort.

Price Insight: The predicted price of the property is ₹ {round(prediction, 2)}. This valuation takes into account the property's size, location characteristics, furnishing status, and available amenities. The actual market price may vary based on factors including the property's condition, recent sales of similar properties in the area, current market demand, and economic conditions at the time of sale or rent.

Market Trends: The real estate market is subject to fluctuations based on economic conditions, government policies, and local demand. Properties with {location_text} tend to have higher demand due to their accessibility and convenience. The {furnishing_desc.lower()} status could also attract buyers or renters looking for immediate occupancy. However, market trends can change, and what is in demand today may shift based on economic factors and buyer preferences.

Recommendation: Given the property's characteristics and location, it appears to be a potentially attractive option for buyers or renters seeking convenience. However, it's crucial for potential buyers or investors to conduct thorough research and consider their own needs and financial situation before making a decision. If you're considering purchasing this property as an investment, evaluate the potential for rental income and ongoing costs of ownership, such as maintenance, property taxes, and insurance. For buyers looking to occupy the property, consider factors like commute time, local amenities, schools, and the quality of the neighborhood.

Risks: There are several risks to consider when purchasing this property:

Market Risk: The real estate market can be volatile, and property values may fluctuate based on economic conditions, affecting your investment.

Location Risk: While the property's location offers certain advantages, consider potential drawbacks such as noise levels, traffic, and future development plans in the area.

Maintenance Risk: All properties require ongoing maintenance. Budget for regular upkeep and unexpected repairs, which can be significant and may affect the property's value or your ability to sell or rent it in the future.

Regulatory Risk: Changes in local zoning laws, property taxes, building codes, or other government regulations could impact the property's value or your rights as a property owner.

Financial Risk: Purchasing a property is a significant financial commitment. Ensure you have a stable financial situation, adequate emergency funds, and a clear plan for managing the costs associated with homeownership, including mortgage payments, insurance, taxes, and maintenance.

It's essential to approach this investment with a clear understanding of these risks and to seek professional advice from real estate agents, financial advisors, and legal experts to ensure that your decision is well-informed and aligned with your long-term goals."""

    return {
        "prediction": float(prediction),
        "advisory": mock_advisory
    }
