import matplotlib.pyplot as plt

x = [1,3,5,8,9]
y = [100,40,20,50,60]

# plots just a line
plt.plot(x,y)
plt.show()

# plots a green line with data points marked with circles
plt.plot(x,y, 'go-')
plt.title('some title')
plt.xlabel('some x-axis label')
plt.ylabel('some y-axis label')
plt.show()


plt.bar(x,y)
plt.title('some title')
plt.xlabel('some x-axis label')
plt.ylabel('some y-axis label')
# if you want to just save it instead, replace plt.show() with the following:
#plt.savefig('filename.png')
plt.show()
