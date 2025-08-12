import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv("datasets/uber_cleaned.csv")

# Convert the "Trip Datetime"object to datetime
df["Trip Datetime"] = pd.to_datetime(df["Trip Datetime"])

# What are the top 5 most popular Pickup Location and Drop Location pairs?
top_5_routes = df.groupby(["Pickup Location","Drop Location"]).size().nlargest(5).reset_index(name="Ride Count")
print("Top 5 most popular Pickup Location and Drop Location pairs")
print(top_5_routes)

# Plotting
# Combine Pickup and Drop Location into one label for plotting
top_5_routes["Route"] = top_5_routes["Pickup Location"] + " " + top_5_routes["Drop Location"]

# Plot
plt.barh(top_5_routes["Route"],top_5_routes["Ride Count"],color="skyblue",edgecolor="black")
plt.xlabel("Ride Count")
plt.ylabel("Route (Pickup → Drop)")
plt.title("Top 5 most popular Pickup Location and Drop Location pairs")
plt.gca().invert_yaxis() # Highest at the top
plt.grid(axis="x",linestyle="--",alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()