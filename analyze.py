import requests
import pandas as pd

def get_eps_scores(stock_symbol):
    api_key = 'NSZ8QYTYZU9CSYZ0'
    url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={stock_symbol}&apikey={api_key}'

    # Fetch earnings data from Alpha Vantage
    response = requests.get(url)
    data = response.json()

    # Check if earnings data is available
    if 'quarterlyEarnings' not in data or len(data['quarterlyEarnings']) == 0:
        print("EPS data not found for the provided stock symbol.")
        return None

    # Extract EPS scores
    earnings = data['quarterlyEarnings']
    eps = pd.DataFrame(earnings)['reportedEPS']

    return eps

# Example usage
stock_symbol = input("Enter stock symbol (e.g., AAPL, GOOG): ")
eps_scores = get_eps_scores(stock_symbol)

if eps_scores is not None:
    print(f"EPS Scores for {stock_symbol}:")
    print(eps_scores)
