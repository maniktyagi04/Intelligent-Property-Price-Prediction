# 🔑 How to Get a Valid Groq API Key

## The Problem
The API key you provided is being rejected by Groq's servers. This could be because:
- The key has expired
- The key was revoked
- There's a typo in the key
- The key doesn't have the right permissions

## ✅ Solution: Get a New API Key

### Step 1: Visit Groq Console
Go to: **https://console.groq.com/**

### Step 2: Sign In or Sign Up
- If you have an account, sign in
- If not, create a free account (it's quick!)

### Step 3: Navigate to API Keys
- Look for "API Keys" in the left sidebar or menu
- Or go directly to: **https://console.groq.com/keys**

### Step 4: Create New API Key
1. Click "Create API Key" button
2. Give it a name (e.g., "Property Prediction App")
3. Click "Create"
4. **IMPORTANT**: Copy the key immediately (you won't see it again!)

### Step 5: Update Your .env File
1. Open `backend/.env` file
2. Replace the current key with your new key:
   ```
   GROQ_API_KEY=your_new_key_here
   ```
3. Save the file

### Step 6: Test It
The backend will automatically reload. Then:
1. Go to http://localhost:5173
2. Fill in property details
3. Click "Predict Price"
4. You should now see AI-generated advisory!

## 🆘 If You Don't Have a Groq Account

### Alternative: Use Without AI Features
The application works perfectly without the AI features:
- ✅ Price predictions work (ML model)
- ✅ All form features work
- ❌ No AI advisory text
- ❌ No legal advisor chat

To disable the error messages and just show predictions:
1. I can modify the code to hide the AI advisory section
2. The app will work smoothly with just predictions

**Would you like me to do this?**

## 📝 What the API Key Looks Like

A valid Groq API key should:
- Start with `gsk_`
- Be about 56-60 characters long
- Contain letters and numbers
- Example format: `gsk_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890AbCdEfGhIj`

## 🔍 Verify Your New Key

Once you get a new key, you can test it with this command:
```bash
curl -X POST https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_NEW_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{"model":"llama-3.3-70b-versatile","messages":[{"role":"user","content":"Hello"}],"max_tokens":10}'
```

If it works, you'll see a response. If not, you'll see an error.

## ⚡ Quick Fix Option

If you can't get a new API key right now, I can:
1. Modify the UI to hide the AI advisory section
2. Show only the price prediction
3. Remove error messages
4. Make the app look clean and professional

This way, the app will work smoothly without any error messages, and you can add the AI features later when you get a valid key.

**Let me know if you want me to implement this quick fix!**
