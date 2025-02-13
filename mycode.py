import pandas as pd
import os

data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "Country": ["USA", "UK", "Australia", "Germany"],
    "Score": [90, 85, 78, 92]
}

df = pd.DataFrame(data)

data_dir = "data"

# Create a directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")