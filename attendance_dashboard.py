import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Attendance": [90, 85, 95, 80, 88]
})

# Basic calculations
average = df["Attendance"].mean()
highest = df["Attendance"].max()
lowest = df["Attendance"].min()

# Create dashboard
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 1. Monthly attendance bar chart
ax[0, 0].bar(df["Month"], df["Attendance"])
ax[0, 0].set_title("Monthly Class Attendance")
ax[0, 0].set_xlabel("Month")
ax[0, 0].set_ylabel("Attendance (%)")

# 2. Line graph
ax[0, 1].plot(df["Month"], df["Attendance"], marker="o")
ax[0, 1].set_title("Attendance Trend")
ax[0, 1].set_xlabel("Month")
ax[0, 1].set_ylabel("Attendance (%)")

# 3. Pie chart
ax[1, 0].pie(
    df["Attendance"],
    labels=df["Month"],
    autopct="%1.1f%%"
)
ax[1, 0].set_title("Attendance Distribution")

# 4. Summary
ax[1, 1].axis("off")

summary = f"""
CLASS ATTENDANCE DASHBOARD

Average Attendance: {average:.2f}%
Highest Attendance: {highest}%
Lowest Attendance : {lowest}%
Total Months      : {len(df)}
"""

ax[1, 1].text(
    0.1, 0.5,
    summary,
    fontsize=12,
    verticalalignment="center"
)

plt.suptitle("Class Attendance Trend Dashboard", fontsize=18)

plt.tight_layout()
plt.show()
