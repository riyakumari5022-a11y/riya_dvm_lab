import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# LOAD DATASET
# -------------------------------
df = pd.read_csv("Cafe_sales_cleaned.csv")

print("Columns:", df.columns)

# -------------------------------
# CLEAN DATA (VERY IMPORTANT)
# -------------------------------

# Fix Date column (handle ERROR values)
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

# Remove invalid rows
df = df.dropna(subset=['Transaction Date'])

# Fill missing numeric values
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

df['Total Spent'].fillna(df['Total Spent'].mean(), inplace=True)
df['Quantity'].fillna(df['Quantity'].mean(), inplace=True)

# Fill categorical missing values
df['Item'].fillna(df['Item'].mode()[0], inplace=True)
df['Payment Method'].fillna(df['Payment Method'].mode()[0], inplace=True)

# -------------------------------
# SAME COLOR
# -------------------------------
color = 'blue'

# -------------------------------
# 1. BAR CHART
# -------------------------------
plt.figure()
sales_by_item = df.groupby('Item')['Total Spent'].sum()

plt.bar(sales_by_item.index, sales_by_item.values, color=color)
plt.title("Bar Chart: Item vs Total Spent")
plt.xlabel("Item")
plt.ylabel("Total Spent")
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

# -------------------------------
# 2. LINE CHART
# -------------------------------
plt.figure()
df_sorted = df.sort_values('Transaction Date')

plt.plot(df_sorted['Transaction Date'], df_sorted['Total Spent'], color=color)
plt.title("Line Chart: Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Spent")
plt.grid(True)
plt.show()

# -------------------------------
# 3. PIE CHART
# -------------------------------
plt.figure()
payment_counts = df['Payment Method'].value_counts()

plt.pie(payment_counts,
        labels=payment_counts.index,
        autopct='%1.1f%%',
        colors=[color]*len(payment_counts))

plt.title("Pie Chart: Payment Method Distribution")
plt.show()

# -------------------------------
# 4. STAIR CHART
# -------------------------------
plt.figure()
plt.step(df['Quantity'], df['Total Spent'], where='mid', color=color)

plt.title("Stair Chart: Quantity vs Total Spent")
plt.xlabel("Quantity")
plt.ylabel("Total Spent")
plt.grid(True)
plt.show()

# -------------------------------
# 5. HISTOGRAM
# -------------------------------
plt.figure()
plt.hist(df['Total Spent'], bins=10, color=color)

plt.title("Histogram: Total Spent Distribution")
plt.xlabel("Total Spent")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()