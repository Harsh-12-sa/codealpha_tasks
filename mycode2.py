import requests
import json

# Alpha Vantage API (Replace with your own API key)
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://www.alphavantage.co/query"

# Portfolio dictionary to store stock data
portfolio = {}

def get_stock_price(symbol):
    """Fetch real-time stock price from Alpha Vantage API"""
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    try:
        return float(data["Global Quote"]["05. price"])
    except KeyError:
        print("Error fetching stock data. Please check the symbol and try again.")
        return None

def add_stock(symbol, quantity):
    """Add stock to the portfolio"""
    price = get_stock_price(symbol)
    if price:
        portfolio[symbol] = {"quantity": quantity, "price": price}
        print(f"Added {quantity} shares of {symbol} at ${price} per share.")

def remove_stock(symbol):
    """Remove stock from the portfolio"""
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print("Stock not found in portfolio.")

def view_portfolio():
    """Display the stock portfolio"""
    if not portfolio:
        print("Your portfolio is empty.")
        return
    total_value = 0
    print("\nStock Portfolio:")
    for symbol, data in portfolio.items():
        value = data["quantity"] * data["price"]
        total_value += value
        print(f"{symbol}: {data['quantity']} shares @ ${data['price']} each | Total: ${value:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main(test_inputs=None):
    options = ["1", "2", "3", "4"]
   
    if test_inputs is None:
        test_inputs = ["1", "AAPL", "10", "3", "4"]
   
    print("\nStock Portfolio Tracker")
    for choice in test_inputs:
        print(f"\nUser Choice: {choice}")
        if choice == "1":
            symbol = "AAPL"
            quantity = 10
            add_stock(symbol, quantity)
        elif choice == "2":
            symbol = "AAPL"
            remove_stock(symbol)
        elif choice == "3":