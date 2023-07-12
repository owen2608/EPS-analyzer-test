import requests

# Make a request to the API endpoint
response = requests.get('https://www.nba.com/2023-summer-league-vegas-player-stats')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the data from the response (assuming the response is in JSON format)
    data = response.json()

    # Process the data as needed
    # ...

    # Example: Print the first player's name
    first_player_name = data['players'][0]['name']
    print("First player's name:", first_player_name)
else:
    # Handle the case when the request was not successful
    print("Error: API request failed with status code", response.status_code)
