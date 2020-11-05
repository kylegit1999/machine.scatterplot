import matplotlib.pyplot as plt
from scipy import stats
temp= [14.2,16.5,11.8,15.3,18.8,22.5,19.5]
sales =[ 200,330,140,340,410,445,415]
slope, intercept, r, p, std_err = stats.linregress(temp, sales)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, temp))

plt.scatter(temp, sales)
plt.plot(temp, mymodel)

plt.scatter(temp,sales)
plt.xlabel("Tempreture")
plt.ylabel("Price in R")
plt.title("Soup sales in relation to tempreture")


plt.show()
