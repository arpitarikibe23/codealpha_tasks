import requests
import json
from prettytable import PrettyTable

# Alpha Vantage API Key (Get yours from https://www.alphavantage.co/)
API_KEY = "06Q5O6S5X4MWRVLF"

# Portfolio dictionary to store stock symbols and quantities
portfolio = {}

# Function to get real-time stock price
def get_stock_price(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if "Global Quote" in data:
        return float(data["Global Quote"]["05. price"])
    else:
        print("⚠️ Error fetching stock data. Check the stock symbol or API key.")
        return None

# Function to add stock to portfolio
def add_stock(symbol, quantity):
    symbol = symbol.upper()
    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity
    print(f"✅ Added {quantity} shares of {symbol} to portfolio.")

# Function to remove stock from portfolio
def remove_stock(symbol, quantity):
    symbol = symbol.upper()
    if symbol in portfolio:
        if portfolio[symbol] > quantity:
            portfolio[symbol] -= quantity
            print(f"✅ Removed {quantity} shares of {symbol} from portfolio.")
        else:
            del portfolio[symbol]
            print(f"✅ Removed {symbol} from portfolio.")
    else:
        print("⚠️ Stock not found in portfolio.")

# Function to display portfolio
def display_portfolio():
    if not portfolio:
        print("📉 Your portfolio is empty!")
        return

    table = PrettyTable(["Stock", "Quantity", "Current Price", "Total Value"])
    total_portfolio_value = 0

    for symbol, quantity in portfolio.items():
        price = get_stock_price(symbol)
        if price:
            total_value = price * quantity
            total_portfolio_value += total_value
            table.add_row([symbol, quantity, f"${price:.2f}", f"${total_value:.2f}"])

    print("\n📊 Your Stock Portfolio:")
    print(table)
    print(f"\n💰 Total Portfolio Value: ${total_portfolio_value:.2f}")

# Main menu function
def main():
    while True:
        print("\n📈 Stock Portfolio Tracker")
        print("1️⃣ Add Stock")
        print("2️⃣ Remove Stock")
        print("3️⃣ View Portfolio")
        print("4️⃣ Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity: "))
            add_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            remove_stock(symbol, quantity)
        elif choice == "3":
            display_portfolio()
        elif choice == "4":
            print("👋 Exiting... Happy Investing!")
            break
        else:
            print("⚠️ Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
