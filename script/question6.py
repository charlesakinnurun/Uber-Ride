import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/uber_cleaned.csv")

# Which Pickup Location has the highest number of No Driver Found rides?
no_driver_found_locations = df[df["Booking Status"] == "No Driver Found"]["Pickup Location"].value_counts().idxmax()
print("Pickup Location with the highest number of 'No Driver Found' rides:")
print(no_driver_found_locations)

