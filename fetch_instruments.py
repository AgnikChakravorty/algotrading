"""
Fetch Instruments from Zerodha
This script connects to Zerodha and fetches the list of available instruments/trading pairs.
"""

from kiteconnect import KiteConnect
import config
import pandas as pd
from datetime import datetime

def connect_kite():
    """Initialize and authenticate KiteConnect"""
    kite = KiteConnect(api_key=config.API_KEY)
    
    # Set access token
    if not config.ACCESS_TOKEN or config.ACCESS_TOKEN == "your_access_token_here":
        print("❌ Error: ACCESS_TOKEN not set in config.py")
        print("\nPlease run authenticate.py first to get your access token.")
        return None
    
    kite.set_access_token(config.ACCESS_TOKEN)
    return kite

def fetch_instruments(kite, exchange="NSE"):
    """
    Fetch instruments from specified exchange
    
    Args:
        kite: KiteConnect instance
        exchange: Exchange name (NSE, BSE, NFO, BFO, CDS, MCX, etc.)
    
    Returns:
        List of instruments
    """
    try:
        print(f"\n📊 Fetching instruments from {exchange}...")
        instruments = kite.instruments(exchange)
        print(f"✅ Successfully fetched {len(instruments)} instruments from {exchange}")
        return instruments
    except Exception as e:
        print(f"❌ Error fetching instruments: {e}")
        return None

def display_instruments(instruments, limit=20):
    """Display instruments in a readable format"""
    if not instruments:
        return
    
    # Convert to DataFrame for better display
    df = pd.DataFrame(instruments)
    
    print(f"\n{'='*100}")
    print(f"First {limit} instruments:")
    print(f"{'='*100}\n")
    
    # Display first few instruments
    print(df[['tradingsymbol', 'name', 'exchange', 'instrument_type', 'segment']].head(limit))
    
    print(f"\n{'='*100}")
    print(f"Total instruments: {len(instruments)}")
    print(f"{'='*100}")

def save_instruments_to_csv(instruments, exchange="NSE"):
    """Save instruments to CSV file"""
    if not instruments:
        return
    
    df = pd.DataFrame(instruments)
    filename = f"instruments_{exchange}_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(filename, index=False)
    print(f"\n💾 Instruments saved to {filename}")

def main():
    print("="*100)
    print("Zerodha Kite Connect - Fetch Instruments")
    print("="*100)
    
    # Connect to Kite
    kite = connect_kite()
    if not kite:
        return
    
    try:
        # Verify connection by fetching user profile
        profile = kite.profile()
        print(f"\n✅ Connected successfully!")
        print(f"User: {profile['user_name']} ({profile['user_id']})")
        print(f"Email: {profile['email']}")
        print(f"Broker: {profile['broker']}")
        print(f"Available Exchanges: {', '.join(profile['exchanges'])}")
        
    except Exception as e:
        print(f"\n❌ Connection failed: {e}")
        print("\nPossible reasons:")
        print("1. Access token is invalid or expired (tokens expire at 6 AM daily)")
        print("2. API key is incorrect")
        print("3. Network connectivity issues")
        print("\nPlease run authenticate.py again to get a fresh access token.")
        return
    
    # Fetch instruments from NSE
    instruments = fetch_instruments(kite, exchange="NSE")
    
    if instruments:
        # Display sample instruments
        display_instruments(instruments, limit=20)
        
        # Save to CSV
        save_instruments_to_csv(instruments, exchange="NSE")
        
        print("\n" + "="*100)
        print("Available exchanges to fetch from:")
        print("NSE, BSE, NFO (F&O), BFO, CDS, MCX, BCD, MF (Mutual Funds)")
        print("\nYou can modify the exchange parameter in the script to fetch from other exchanges.")
        print("="*100)

if __name__ == "__main__":
    main()
