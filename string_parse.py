# Sample string
data = "Name: Veer, Age: 20, City: Bengaluru"

# Split the string into parts
parts = data.split(", ")

# Parse the individual components
info = {}
for part in parts:
    key, value = part.split(": ")
    info[key] = value

# Display the parsed information
print("Parsed Data:")
for key, value in info.items():
    print(f"{key}: {value}")