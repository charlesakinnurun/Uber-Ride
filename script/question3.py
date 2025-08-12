import pandas as pd
import matplotlib.pyplot as plt

# Load the Cleaned data
df = pd.read_csv("datasets/uber_cleaned.csv")

# How many rides were Completed, Cancelled by Customer or Cancelled by Driver
completed_rides = df[df["Booking Status"] == "Completed"].shape[0]
customer_cancelled = df["Cancelled Rides by Customer"].sum()
driver_cancelled = df["Cancelled Rides by Driver"].sum()
print("Total number of Completed,Cancelled by Customer and Cancelled by Driver rides:")
print(f"Completed Rides: {completed_rides}")
print(f"Cancelled Rides by Customer: {int(customer_cancelled)}")
print(f"Cancelled Rides by Driver: {int(driver_cancelled)}")

# Prepare data for Plotting
categories = ["Completed Rides","Cancelled by Customers","Cancelled by Driver"]
values = [completed_rides,customer_cancelled,driver_cancelled]

# Create the bar chart
bars = plt.bar(categories,values,color=["skyblue","darkblue","mediumblue"],edgecolor="black")

# Labels and title
plt.ylabel("Number of Rides")
plt.title("Completed,Cancelled by Customer and Cancelled by Driver Rides")
plt.grid(axis="y",linestyle= "--",alpha=0.7)

# Show the plot 
plt.tight_layout()
plt.show()