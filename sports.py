import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Make a request to the NBA API to fetch player statistics
response = requests.get('https://api.nba.com/stats/summerleague/stats/player')

# Extract the player statistics data from the response
data = response.json()['resultSets'][0]['rowSet']

# Define the column names for the DataFrame
columns = response.json()['resultSets'][0]['headers']

# Create a pandas DataFrame from the player statistics data
df = pd.DataFrame(data, columns=columns)

# Select the relevant features and target variable
features = ['points', 'assists', 'rebounds']
target = 'minutes'  # Assuming 'minutes' is the target variable

# Filter the DataFrame to include only the selected features and target variable
df_filtered = df[features + [target]]

# Split the dataset into features (X) and target variable (y)
X = df_filtered.drop(target, axis=1)
y = df_filtered[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model (you can use different metrics depending on your needs)
score = model.score(X_test, y_test)

print("Predicted minutes:", predictions)
print("R^2 score:", score)
