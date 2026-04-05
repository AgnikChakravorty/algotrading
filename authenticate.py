"""
Zerodha Authentication Script
This script helps you authenticate with Zerodha and get your access token.
Run this once to authenticate and get your access token.
"""

from kiteconnect import KiteConnect
import config
import webbrowser

# Initialize KiteConnect
kite = KiteConnect(api_key=config.API_KEY)

# Step 1: Generate login URL
login_url = kite.login_url()
print(f"Please login using this URL: {login_url}")
print("\n" + "="*80)

# Open the login URL in default browser
try:
    webbrowser.open(login_url)
    print("Login page opened in your browser...")
except:
    print("Could not open browser automatically. Please copy the URL above and paste it in your browser.")

print("\n" + "="*80)
print("After logging in, you will be redirected to your callback URL.")
print("The URL will contain a 'request_token' parameter.")
print("Example: http://127.0.0.1:5000/callback?request_token=XXXXXX&action=login&status=success")
print("\n" + "="*80)

# Step 2: Get the request token from user
request_token = input("\nEnter the request_token from the redirect URL: ").strip()

# Step 3: Generate session
try:
    data = kite.generate_session(request_token, api_secret=config.API_SECRET)
    print("\n" + "="*80)
    print("Authentication Successful!")
    print("="*80)
    print(f"\nUser ID: {data['user_id']}")
    print(f"User Name: {data['user_name']}")
    print(f"Email: {data['email']}")
    print(f"Exchanges: {', '.join(data['exchanges'])}")
    print(f"\nAccess Token: {data['access_token']}")
    print("\n" + "="*80)
    print("\nIMPORTANT: Save this access token!")
    print("Copy the access token above and paste it in config.py as ACCESS_TOKEN")
    print("This token will be valid until 6 AM tomorrow.")
    print("="*80)
    
except Exception as e:
    print(f"\n❌ Error during authentication: {e}")
    print("\nPlease check:")
    print("1. Your API key and secret are correct in config.py")
    print("2. The request token was copied correctly")
    print("3. The request token hasn't expired (they expire in a few minutes)")
