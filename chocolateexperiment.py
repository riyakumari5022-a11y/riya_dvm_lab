import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("products.xlsx")

plt.figure()
plt.bar(df['product_id'], df['cocoa_percent'])
plt.title("Product ID vs Cocoa %")
plt.xlabel("Product ID")
plt.ylabel("Cocoa %")
plt.xticks(rotation=90)
plt.grid(True)
plt.show()


plt.figure()
plt.plot(df['product_id'], df['weight_g'], marker='o')
plt.title("Product ID vs Weight")
plt.xlabel("Product ID")
plt.ylabel("Weight (g)")
plt.xticks(rotation=90)
plt.grid(True)
plt.show()


plt.figure()
plt.pie(df['brand'].value_counts(),
        labels=df['brand'].value_counts().index,
        autopct='%1.1f%%')
plt.title("Brand Distribution")
plt.show()


plt.figure()
plt.step(df['cocoa_percent'], df['weight_g'], where='mid')

plt.title("Stair Plot: Cocoa % vs Weight")
plt.xlabel("Cocoa %")
plt.ylabel("Weight (g)")
plt.grid(True)

plt.show()


plt.figure()
plt.hist(df['cocoa_percent'], bins=8)
plt.title("Cocoa % Distribution")
plt.xlabel("Cocoa %")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()