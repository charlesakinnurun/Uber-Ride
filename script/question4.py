import pandas as pd
import matplotlib.pyplot as plt

# Load the Cleaned data
df = pd.read_csv("datasets/uber_cleaned.csv")

# What is the Average Customer Rating of each Payment Method
avg_customer_rating_by_payment = df.groupby("Payment Method")["Customer Rating"].mean().reset_index()
print("Average Customer Rating for each Payment Method")
print(avg_customer_rating_by_payment)

# Plot
bars = plt.bar(
    avg_customer_rating_by_payment["Payment Method"],
    avg_customer_rating_by_payment["Customer Rating"],
    color="skyblue",
    edgecolor="black"
)

# Label and title
plt.xlabel("Payment Method")
plt.ylabel("Average Customer Rating")
plt.title("Average Customer Rating by Payment Method")
plt.ylim(0,5) # Ratings are usually between 0 and 5
plt.xticks(rotation=45)
plt.grid(axis="y",linestyle="--",alpha=0.7)

# Show plot
plt.tight_layout()
plt.show()