print("RUNNING SCRIPT...")
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

summary = data.groupby("product")["sales"].sum()
print(summary)

summary.plot(kind="bar")
plt.title("Sales by Product")
plt.show()