# Getting Your Zerodha Kite Connect API Credentials

This guide will walk you through the complete process of setting up your Zerodha developer account and obtaining API credentials.

## Prerequisites

Before you begin, ensure you have:

1. ✅ **Active Zerodha Trading Account** - You must have an active trading account with Zerodha
2. ✅ **2FA TOTP Enabled** - Your account must have Time-based OTP (TOTP) enabled
   - Guide: https://support.zerodha.com/category/trading-and-markets/general-kite/login-credentials-of-trading-platforms/articles/time-based-otp-setup

---

## Step-by-Step Guide

### Step 1: Access Kite Connect Developer Portal

1. Visit the **Kite Connect Developer Portal**: 
   - URL: **https://developers.kite.trade/login**
   
2. Click on **"Sign up"** or **"Login"** if you already have an account

3. Log in using your **Zerodha credentials** (same as your trading account)

---

### Step 2: Create a New App

1. After logging in, click on **"Create New App"** or **"My Apps"** → **"Create New App"**

2. Fill in the application details:
   
   **App Name**: Give your app a name (e.g., "My Auto Trading Bot")
   
   **Redirect URL**: This is where users will be redirected after login
   - For local development, use: `http://127.0.0.1:5000/callback`
   - For production, use your actual domain
   - ⚠️ **Important**: Remember this URL - you'll need it in config.py
   
   **Description**: Brief description of what your app does
   
   **Webhook URL** (Optional): Leave blank for now
   
   **Other fields**: Fill as required

3. Accept the terms and conditions

4. Click **"Create"** or **"Submit"**

---

### Step 3: Get Your API Credentials

1. After creating the app, you'll be taken to the **app details page**

2. You'll see your credentials:
   
   📌 **API Key** (or App Key)
   - A unique string that identifies your app
   - Example format: `xxxxxxxxxxxxxx`
   - ✅ This is safe to share (but keep it secure)
   
   📌 **API Secret** (or App Secret)
   - A secret key used for authentication
   - Example format: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - ⚠️ **CRITICAL**: Never share this or commit it to version control!
   - ⚠️ Do NOT embed this in mobile/web apps
   
3. **Copy both credentials** and save them securely

---

### Step 4: Note Your Redirect URL

1. On the same app details page, verify your **Redirect URL**

2. This should match what you'll use in your code

3. Common redirect URLs:
   - Local development: `http://127.0.0.1:5000/callback`
   - Local development alt: `http://localhost:5000/callback`
   - Production: `https://yourdomain.com/callback`

---

### Step 5: Update Your config.py

Now update the `config.py` file in your project:

```python
# config.py

API_KEY = "your_api_key_here"          # Replace with your actual API Key
API_SECRET = "your_api_secret_here"    # Replace with your actual API Secret
REDIRECT_URL = "http://127.0.0.1:5000/callback"  # Match your registered redirect URL
ACCESS_TOKEN = None  # Will be filled after running authenticate.py
```

**Example with real values** (don't use these - they're just examples):
```python
API_KEY = "abc123xyz456"
API_SECRET = "def789ghi012jkl345mno678pqr901"
REDIRECT_URL = "http://127.0.0.1:5000/callback"
ACCESS_TOKEN = None
```

---

## Important Security Notes

### 🔒 Keep Your API Secret Secure

- ❌ Never commit `config.py` to Git (it's already in `.gitignore`)
- ❌ Never share your API secret publicly
- ❌ Never embed it in client-side code (mobile apps, web frontends)
- ✅ Only use it in server-side/backend code
- ✅ Store it in environment variables for production

### 🔑 Understanding Access Tokens

- **API Key & Secret**: Permanent credentials (until you regenerate them)
- **Access Token**: Temporary token that expires at **6 AM daily**
- You'll need to run `authenticate.py` daily to get a fresh access token

---

## Subscription and Pricing

### Free Tier vs Paid

1. **Developer Account**: Free to create
2. **API Usage**: 
   - Zerodha charges a monthly fee for API access
   - Check current pricing: https://kite.trade/pricing
   - As of last update: ₹2000/month for active users

3. **Subscription Process**:
   - You may need to subscribe to Kite Connect after creating your app
   - Visit your developer dashboard for subscription details

---

## Testing Your Setup

After updating `config.py`:

### 1. Run Authentication
```bash
python authenticate.py
```

Expected output:
- Browser opens with Zerodha login
- You log in with your trading credentials
- Get redirected to a URL with `request_token`
- Script generates and displays your `access_token`

### 2. Update Access Token
Copy the access token and update `config.py`:
```python
ACCESS_TOKEN = "your_generated_access_token"
```

### 3. Test Connection
```bash
python fetch_instruments.py
```

Expected output:
- ✅ Connected successfully!
- Your user profile details
- List of available instruments
- CSV file with all instruments

---

## Troubleshooting

### Problem: "Can't access Developer Portal"
- **Solution**: Ensure you're using your Zerodha trading account credentials
- Make sure 2FA TOTP is enabled on your account

### Problem: "App creation failed"
- **Solution**: Check that all required fields are filled
- Ensure redirect URL is in correct format (http:// or https://)

### Problem: "Invalid API credentials"
- **Solution**: Double-check you copied the entire API key and secret
- No extra spaces or characters
- Make sure you're using the correct app's credentials

### Problem: "Access denied" during authentication
- **Solution**: Ensure you have an active Kite Connect subscription
- Check your subscription status in the developer portal

---

## Useful Links

- 🌐 **Kite Connect Developer Portal**: https://developers.kite.trade/
- 📚 **API Documentation**: https://kite.trade/docs/connect/v3/
- 🐍 **Python Client Docs**: https://kite.trade/docs/pykiteconnect/v4/
- 💰 **Pricing**: https://kite.trade/pricing
- ❓ **Support**: https://kite.trade/forum
- 📖 **2FA TOTP Setup**: https://support.zerodha.com/category/trading-and-markets/general-kite/login-credentials-of-trading-platforms/articles/time-based-otp-setup

---

## Next Steps

After getting your credentials:

1. ✅ Update `config.py` with API Key, Secret, and Redirect URL
2. ✅ Run `authenticate.py` to get your access token
3. ✅ Update `config.py` with the access token
4. ✅ Run `fetch_instruments.py` to test the connection
5. ✅ Start building your trading strategies!

---

## Daily Workflow

Since access tokens expire at 6 AM daily:

**Every day before trading:**
1. Run `python authenticate.py`
2. Copy the new access token
3. Update `ACCESS_TOKEN` in `config.py`
4. Run your trading scripts

**Tip**: You can automate this with a simple script that stores the token in a file or environment variable.

---

**Need Help?**
- Zerodha Support: https://support.zerodha.com/
- Kite Connect Forum: https://kite.trade/forum/
