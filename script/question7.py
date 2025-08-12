import pandas as pd
import matplotlib.pyplot as plt

# Load the Cleaned Data
df = pd.read_csv("datasets/uber_cleaned.csv")

# What is the distribution of Booking Status for each Vehicle Type?
status_by_vehicle = pd.crosstab(df["Vehicle Type"], df["Booking Status"])
print("Distribution of Booking Status for each Vehicle Type")
print(status_by_vehicle)

# Plot
status_by_vehicle.plot(kind="bar",color=["blue","skyblue","mediumblue","darkblue","royalblue"])

# Labels and title
plt.xlabel("Vehicle Type")
plt.ylabel("Booking Status")
plt.title("Distribution of Booking Status by Vehicle Type")
plt.xticks(rotation=45)
plt.grid(axis="y",linestyle="--",alpha=0.7)
plt.legend(title="Booking Status")

# Show the Plot
plt.tight_layout()
plt.show()