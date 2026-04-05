# Zerodha Auto Trading System

This project connects to Zerodha's Kite Connect API to fetch market data and execute automated trades.

## Prerequisites

1. **Zerodha Account**: You need an active Zerodha trading account
2. **Kite Connect API Access**: 
   - Create a developer account at [Kite Connect Developer Portal](https://developers.kite.trade/)
   - Create a new app to get your API credentials
   - Note down your `api_key` and `api_secret`
   - Set a redirect URL (e.g., `http://127.0.0.1:5000/callback`)

3. **Python Dependencies**: Already installed
   - kiteconnect
   - pandas (install if needed: `pip install pandas`)

## Setup Instructions

### Step 1: Configure API Credentials

Edit `config.py` and add your credentials:

```python
API_KEY = "your_api_key_here"  # From Kite Connect developer portal
API_SECRET = "your_api_secret_here"  # From Kite Connect developer portal
REDIRECT_URL = "http://127.0.0.1:5000/callback"  # Your registered redirect URL
```

### Step 2: Authenticate and Get Access Token

Run the authentication script:

```bash
python authenticate.py
```

This will:
1. Open the Kite login page in your browser
2. After you log in, you'll be redirected to a URL with a `request_token`
3. Copy the `request_token` from the URL and paste it into the terminal
4. The script will generate an `access_token` for you
5. Copy this access token and update it in `config.py`

**Important**: Access tokens expire daily at 6 AM. You'll need to re-authenticate each day.

### Step 3: Fetch Instruments

Run the instruments fetching script:

```bash
python fetch_instruments.py
```

This will:
1. Connect to your Zerodha account
2. Fetch the list of available instruments/trading pairs
3. Display the first 20 instruments
4. Save all instruments to a CSV file

## Files Description

- **config.py**: Stores your API credentials and access token
- **authenticate.py**: Handles the Kite Connect login flow and generates access token
- **fetch_instruments.py**: Connects to Zerodha and fetches available trading instruments
- **README.md**: This file

## Security Notes

⚠️ **IMPORTANT**: 
- Never share your `api_secret` or `access_token`
- Add `config.py` to `.gitignore` if using version control
- The `api_secret` should never be embedded in client-side applications

## Next Steps

After verifying the connection works, you can:
1. Fetch live market data
2. Place orders programmatically
3. Create trading strategies
4. Set up WebSocket for real-time data streaming

## Available Exchanges

- **NSE**: National Stock Exchange (Equity)
- **BSE**: Bombay Stock Exchange (Equity)
- **NFO**: NSE Futures & Options
- **BFO**: BSE Futures & Options
- **CDS**: Currency Derivatives
- **MCX**: Multi Commodity Exchange
- **BCD**: NSE Bond Currency Derivatives
- **MF**: Mutual Funds

## Documentation Links

- [KiteConnect Python Docs](https://kite.trade/docs/pykiteconnect/v4)
- [Kite Connect API Docs](https://kite.trade/docs/connect/v3)
- [GitHub Repository](https://github.com/zerodha/pykiteconnect)

## Troubleshooting

**Issue**: "Access token is invalid or expired"
- **Solution**: Access tokens expire at 6 AM daily. Run `authenticate.py` again.

**Issue**: "Invalid API key"
- **Solution**: Check that your API key in `config.py` matches the one in Kite Connect developer portal.

**Issue**: "Request token expired"
- **Solution**: Request tokens expire in a few minutes. Complete the authentication flow quickly.
