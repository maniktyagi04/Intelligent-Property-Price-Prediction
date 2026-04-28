# 🔑 How to Get a Valid Groq API Key

## Why You Need This

Your application is designed to show detailed AI-powered advisory like:
- Property Summary
- Price Insight  
- Market Trends
- Recommendations
- Risk Analysis

**This feature requires a valid Groq API key to work.**

---

## 📋 Step-by-Step Instructions

### Step 1: Visit Groq Console
Open your browser and go to:
**https://console.groq.com/**

### Step 2: Create Account or Sign In
- If you don't have an account, click "Sign Up" (it's FREE!)
- If you have an account, click "Sign In"

### Step 3: Navigate to API Keys
Once logged in:
- Look for "API Keys" in the left sidebar
- Or go directly to: **https://console.groq.com/keys**

### Step 4: Create New API Key
1. Click the "Create API Key" button
2. Give it a name (e.g., "Property Prediction App")
3. Click "Create" or "Generate"
4. **IMPORTANT**: Copy the key immediately! You won't see it again!

### Step 5: Update Your .env File
1. Open the file: `backend/.env`
2. Find the line that says:
   ```
   GROQ_API_KEY=gsk_uVInOBbQFgOCSTi0LMWPWGdyb3FYAB1ioNf6zJHtjcrgxIhKjlzGnow
   ```
3. Replace it with your new key:
   ```
   GROQ_API_KEY=your_new_key_here
   ```
4. Save the file

### Step 6: Test It!
1. The backend will automatically reload (wait 2-3 seconds)
2. Go to http://localhost:5173
3. Fill in property details
4. Click "Predict Price"
5. You should now see the full AI advisory! 🎉

---

## ✅ What a Valid API Key Looks Like

```
gsk_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890AbCdEfGhIj
```

- Starts with `gsk_`
- About 56-60 characters long
- Contains letters and numbers
- No spaces

---

## 🧪 Test Your New Key

After updating the .env file, test it with this command:

```bash
curl -X POST https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_NEW_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{"model":"llama-3.3-70b-versatile","messages":[{"role":"user","content":"Hello"}],"max_tokens":10}'
```

**If it works**, you'll see a response with text.  
**If it fails**, you'll see an error message.

---

## 🎯 What Will Happen After You Add a Valid Key

### Before (Current State):
```
₹ 2,826,986.01

⚠️ To enable AI-powered advisory insights, please provide a valid Groq API key.
```

### After (With Valid Key):
```
₹ 2,826,986.01

Property Summary: The property in question is a 1-bedroom, 1-bathroom, 
single-story unit, spanning an area of 1659.0 square feet...

Price Insight: The predicted price of the property is ₹ 2826986.01...

Market Trends: The real estate market is subject to fluctuations...

Recommendation: Given the property's characteristics and location...

Risks: There are several risks to consider when purchasing this property...
```

---

## 🆘 Troubleshooting

### "I can't access console.groq.com"
- Check your internet connection
- Try a different browser
- Clear browser cache
- Try incognito/private mode

### "I created a key but it still doesn't work"
- Make sure you copied the entire key
- Check for extra spaces before or after the key
- Make sure the key starts with `gsk_`
- Wait 2-3 seconds for backend to reload
- Refresh your browser

### "I don't want to create an account"
Unfortunately, you need a Groq account to get an API key. The good news:
- It's completely FREE
- Takes less than 2 minutes
- No credit card required
- Generous free tier

---

## 💡 Alternative: Use Mock Data (Temporary)

If you can't get a Groq API key right now, I can create a mock version that shows sample advisory text. This won't be AI-generated, but it will demonstrate how the feature works.

**Would you like me to create a mock version?**

---

## 📞 Need Help?

If you're having trouble getting an API key, let me know and I can:
1. Create a mock version with sample advisory text
2. Help troubleshoot any issues
3. Provide alternative solutions

---

## 🎉 Once You Have a Valid Key

Your application will automatically:
- Generate detailed property summaries
- Provide price insights
- Analyze market trends
- Give recommendations
- Highlight risks

All powered by AI! 🚀

---

**Get your free API key now: https://console.groq.com/** 🔑
