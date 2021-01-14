
import matplotlib.pyplot as plt
y = [5,10,14,16,17,18,19,20,20,20]
x = [2,4,6,8,10,12,14,16,18,20]

# Plot
plt.plot(x,y)
plt.xlabel('time')
plt.ylabel('volume of gass')
plt.title('rate of reaction graph')
plt.show()

#> [<matplotlib.lines.Line2D at 0x10edbab70>]
print(plt)