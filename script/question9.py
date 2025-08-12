import pandas as pd
import matplotlib.pyplot as plt

# Load the Cleaned Data
df = pd.read_csv("datasets/uber_cleaned.csv")

# Average Avg VTAT and Avg CTAT for completed rides with a Driver Rating 4.5 or higher
filtered_rides = df[(df["Booking Status"] == "Completed") & (df["Driver Ratings"] >= 4.5)]
avg_vtat = filtered_rides["Avg VTAT"].mean()
avg_ctat = filtered_rides["Avg CTAT"].mean()
print("Average VTAT and CTAT for completed rides with a Driver Rating of 4.5 or higher")
print(f"Average VTAT: {avg_vtat:.2f}")
print(f"Average CTAT: {avg_ctat:.2f}")

# Plotting
metrics = ["Average VTAT","Average CTAT"]
values = [avg_vtat,avg_ctat]

# Create a bar chart
plt.figure()
bars = plt.bar(metrics,values,color=["skyblue","darkblue"],edgecolor="black")

# Labels & tittle
plt.title("Average VTAT & CTAT (Driver Rating >= 4.5, Completed Rides)")
plt.ylabel("Time (minutes)")
plt.grid(axis="y",linestyle="--",alpha=0.7)

# Display the Plot
plt.tight_layout()
plt.show()