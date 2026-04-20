import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("companydataset.csv")


df = df.head(30)


df['employees'] = df['employees'].astype(str).str.extract('(\d+)')
df['employees'] = pd.to_numeric(df['employees'], errors='coerce').fillna(1)

df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce').fillna(1)
df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce').fillna(1)
df['years'] = pd.to_numeric(df['years'], errors='coerce').fillna(2000)


df_top10 = df.sort_values(by='employees', ascending=False).head(10)
plt.figure(figsize=(10,10))
plt.pie(df_top10['employees'], autopct='%1.1f%%', startangle=90)
plt.legend(df_top10['name'], bbox_to_anchor=(1,1), fontsize=8)


plt.legend(df['name'], bbox_to_anchor=(1,1), fontsize=8)
plt.tight_layout()
plt.show()



df_sorted = df.sort_values(by='review_count', ascending=False)

plt.figure(figsize=(10,8))
plt.barh(df_sorted['name'], df_sorted['review_count'])
plt.title("Funnel Chart: Companies Review Wise")
plt.xlabel("Reviews")
plt.ylabel("Company")
plt.tight_layout()
plt.show()



print("\nTop 10 Companies Headquarters:\n")
print(df[['name', 'hq']].head(10))



plt.figure(figsize=(12,6))
plt.bar(df['name'], df['ratings'])
plt.title("Bar Chart: Companies Rating Wise")
plt.xlabel("Company")
plt.ylabel("Rating")
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
plt.show()



years = [2018, 2019, 2020, 2021, 2022]
companies = [20, 25, 30, 28, 35]

plt.plot(years, companies, marker='o')
plt.title("Line Chart: Companies Year Wise")
plt.xlabel("Year")
plt.ylabel("Number of Companies")
plt.grid(True)

plt.show()