import json
import pandas as pd

# Read JSON data from a file
with open("products.json", "r") as file:
    data = json.load(file)

# Extract products from nested JSON
products = data["store"]["products"]

# Convert to DataFrame
df = pd.json_normalize(products, sep="_")

# Display DataFrame
print(df)
