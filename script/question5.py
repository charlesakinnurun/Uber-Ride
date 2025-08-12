import pandas as pd
import matplotlib.pyplot as plt

# Load the Cleaned data
df = pd.read_csv("datasets/uber_cleaned.csv")

# Convert the "Trip Datetime" object to datetime
df["Trip Datetime"] = pd.to_datetime(df["Trip Datetime"])

# What is the total number of rides and the average ride distance for each day of the week
df["Day of Week"] = df["Trip Datetime"].dt.day_name()
rises_by_day = df.groupby("Day of Week").agg(Total_Rides=("Booking ID","count"),Average_Ride_Distance=("Ride Distance","mean")).reset_index()
rises_by_day =rises_by_day.rename(columns={
    "Total_Rides":"Total Rides",
    "Average_Ride_Distance":"Average Ride Distance"
})

# Display the Result
print("Total number of rides and Average ride distance for each day of the week")
print(rises_by_day)

# Plotting
# Ensure the days are in proper week order
days_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
rises_by_day["Day of Week"] = pd.Categorical(rises_by_day["Day of Week"],categories=days_order,ordered=True)
rises_by_day = rises_by_day.sort_values("Day of Week")

# Create a Plot
fig,ax1 = plt.subplots(figsize=(10,6))

# Plot the Total Rides on the left y-axis
bars = ax1.bar(rises_by_day["Day of Week"],rises_by_day["Total Rides"],color="skyblue",label="Total Rides")
ax1.set_xlabel("Day of Week")
ax1.set_ylabel("Total Rides",color="blue")
ax1.tick_params(axis="y",labelcolor="blue")


# Create a second y-axis for Average Ride Distance
ax2 = ax1.twinx()
ax2.plot(rises_by_day["Day of Week"],rises_by_day["Average Ride Distance"],color = "red",marker = "o",label="Average Ride Distance")
ax2.set_ylabel("Average Ride Distance",color = "red")
ax2.tick_params(axis="y",labelcolor= "red")

# Title and grid
plt.title("Total Rides and Average Ride Distance of each day of the week")
ax1.grid(axis="y",linestyle="--",alpha= 0.6)

# Legends
fig.legend(loc="upper right", bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)


# Show Plot
plt.tight_layout() 
plt.show()