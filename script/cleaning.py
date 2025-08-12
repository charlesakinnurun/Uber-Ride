import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/uber.csv")

# Comine "Date" and "Time" columns and convert to datetime
df["Trip Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"])
df = df.drop(columns= ["Date","Time"])

# Clean "Booking ID" and "Customer ID" columns by removing extra double quotes
df["Booking ID"] = df["Booking ID"].str.strip('\"')
df["Customer ID"] = df["Customer ID"].str.strip('\"')

# Handle missing values 
df["Avg VTAT"] = df["Avg VTAT"].fillna(0)
df["Avg CTAT"] = df["Avg CTAT"].fillna(0)
df["Cancelled Rides by Customer"] = df["Cancelled Rides by Customer"].fillna(0)
df["Reason for cancelling by Customer"] = df["Reason for cancelling by Customer"].fillna("Customer didn't cancel the ride")
df["Cancelled Rides by Driver"] = df["Cancelled Rides by Driver"].fillna(0)
df["Driver Cancellation Reason"] = df["Driver Cancellation Reason"].fillna("Driver didn't cancel the ride")
df["Incomplete Rides"] = df["Incomplete Rides"].fillna(0)
df["Incomplete Rides Reason"] = df["Incomplete Rides Reason"].fillna("No Incomplete Ride")
df["Booking Value"] = df["Booking Value"].fillna(0)
df["Ride Distance"] = df["Ride Distance"].fillna(0)
df["Driver Ratings"] = df["Driver Ratings"].fillna(0)
df["Customer Rating"] = df["Customer Rating"].fillna(0)
df["Payment Method"] = df["Payment Method"].fillna("Customer didn't pay")

# Save the cleaned dataset
df.to_csv("datasets/uber_cleaned.csv")
print("Saved Successfully")