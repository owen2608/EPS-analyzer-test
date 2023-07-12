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
        print(f"EPS data not found for {stock_symbol}.")
        return None

    # Extract EPS scores with years
    earnings = data['quarterlyEarnings']
    eps = pd.DataFrame(earnings)
    eps['year'] = pd.to_datetime(eps['fiscalDateEnding']).dt.year
    eps_scores = eps[['year', 'reportedEPS']]

    return eps_scores

# List of EV car companies
ev_companies = ['TSLA', 'RIVN', 'NIO', 'LCID', 'BYD', 'XPEV', 'PSNY', 'RIDE', 'FF', 'GOEV', 'FSR', 'KARMA', 'BNGO', 'WKHS', 'APTR', 'ALPHA', 'ARVL', 'FUV', 'RIMAC', 'LIGHT']

# Fetch and print EPS scores for each company
for company in ev_companies:
    eps_scores = get_eps_scores(company)
    
    if eps_scores is not None:
        print(f"EPS Scores for {company}:")
        for _, row in eps_scores.iterrows():
            print(f"Year: {row['year']}, EPS: {row['reportedEPS']}")
        print()
