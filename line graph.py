import matplotlib.pyplot as plt

x_input = input("Enter X values (comma separated): ")
y_input = input("Enter Y values (comma separated): ")

x = list(map(float, x_input.split(',')))
y = list(map(float, y_input.split(',')))

if len(x) != len(y):
    print("Error: X and Y must have the same number of values.")
else:

    plt.plot(x, y, marker='o')
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Line Graph from User Input")
    plt.grid(True)
    plt.show()