import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [15, 25, 35, 45, 55]

# line plot
plt.plot(x, y, marker='o', linestyle="--")
plt.title('Basic Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# bar plot
plt.bar(x, y, color="green") # in the same way, bar, barh, pie, hist, boxplot, etc. can be created
plt.title('Basic Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(["Bar Plot"])

plt.grid(True)
plt.show()


#histogram
data = [ 1, 1, 3, 5, 4, 5, 4, 8, 9, 6, 2, 3, 1]
plt.hist(data, bins=4, color='orange', edgecolor="black")
plt.title("Histogram")
plt.show()