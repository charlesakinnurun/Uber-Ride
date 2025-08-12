import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv("datasets/uber_cleaned.csv")

# Customer ID with the highest number of rides and their total Booking Value
top_customer_id = df["Customer ID"].value_counts().idxmax()
total_booking_value = df[df["Customer ID"] == top_customer_id]["Booking Value"].sum()
print("Customer with the highest number of rides and their total Booking Value:")
print(f"Top Customer ID: {top_customer_id}")
print(f"Total Booking Value for this customer: {total_booking_value:.2f}")
