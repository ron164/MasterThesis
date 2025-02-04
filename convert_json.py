import pandas as pd

# Load the CSV file
file_path = "/mnt/data/ECall_Connectivity_Requirements.csv"
df = pd.read_csv(file_path)

# Convert to JSON format
json_output = df.to_json(orient="records", indent=4)

# Save the JSON file
json_file_path = "/mnt/data/ECall_Connectivity_Requirements.json"
with open(json_file_path, "w") as json_file:
    json_file.write(json_output)


