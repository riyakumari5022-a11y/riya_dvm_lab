import matplotlib.pyplot as plt
data = [12, 15, 14, 10, 18, 20, 22, 19, 17, 16, 14, 13, 15, 18, 21]
plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()
