import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv("datasets/uber_cleaned.csv")

# How many incomplete rides due to 'Vehicle Breakdown' and what was the average Ride Distance?
vehicle_breakdown_rides = df[df["Incomplete Rides Reason"] == "Vehicle Breakdown"]
count_breakdown_rides =vehicle_breakdown_rides.shape[0]
avg_distance_breakdown = vehicle_breakdown_rides["Ride Distance"].mean()

# Display the Result
print(f"Incomplete rises due to 'Vehicle Breakdown' and their average Ride Distance")
print(f"Total incomplete rises due to 'Vehicle Breakdown':{count_breakdown_rides}")
print(f"Average ride distance for these rides: {avg_distance_breakdown:.2f}")


# Plotting
metrics = ["Total Incomplete Rides","Average Ride Distance"]
values = [count_breakdown_rides,avg_distance_breakdown]

# Create a figure
plt.figure()
bars = plt.bar(metrics,values,color=["tomato","skyblue"],edgecolor="black")

# Title and styling
plt.title("Incomplete Rides Due to Vehicle Breakdown",fontsize=14)
plt.ylabel("Value")
plt.grid(axis="y",linestyle="--",alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()