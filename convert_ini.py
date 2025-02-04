from configparser import ConfigParser

# Create a ConfigParser object
config = ConfigParser()

# Use the first column as section names and remaining columns as key-value pairs
for _, row in df.iterrows():
    section = str(row.iloc[0])  # First column as section name
    config[section] = {df.columns[i]: str(row.iloc[i]) for i in range(1, len(df.columns))}

# Save to an INI file
ini_file_path = "/mnt/data/ECall_Connectivity_Requirements.ini"
with open(ini_file_path, "w") as ini_file:
    config.write(ini_file)

