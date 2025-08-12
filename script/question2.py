import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv("datasets/uber_cleaned.csv")

# What is the average Booking Value for each Vehicle Type?
avg_booking_value_by_vehicle = df.groupby("Vehicle Type")["Booking Value"].mean().reset_index()
print("Average Booking Value for each Vehicle Type")
print(avg_booking_value_by_vehicle)

# Plot
plt.bar(avg_booking_value_by_vehicle["Vehicle Type"],
        avg_booking_value_by_vehicle["Booking Value"],
        color="skyblue",
        edgecolor="black")

# Label and title
plt.xlabel("Vehicle Type")
plt.ylabel("Booking Value")
plt.title("Average Booking Value by Vehicle Type")
plt.xticks(rotation=45)
plt.grid(axis="y",linestyle="--",alpha=0.7)

# Show the plot 
plt.tight_layout()
plt.show()