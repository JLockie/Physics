import math
import random
import matplotlib.pyplot as plt
import numpy as np 
from scipy.stats import norm, gaussian_kde, skew, kurtosis

sample1 = [random.randint(1,6) for _ in range(1000)] #rolls a six sided die with a 1/6 
                                                     #chance of landing on any side 1000 times 

bias = (0.15,0.15,0.15,0.15,0.15,0.25)               #the probability on the loaded die 
def roll(probs, ntimes):   # roll a len(probs) sided biased die with bias probs for ntimes
   return np.apply_along_axis(lambda x: x.tolist().index(1)+1, 1,        #rolls a six sided die the biased 
                  np.random.multinomial(1, bias,  size=1000)).tolist()    #chance of landing on any side

sample2 = roll(probs=bias, ntimes=1000)              #collect the 1000 biased rolls 

x = np.linspace(2,12,1000)                           #collection of data
sum = np.add(sample1, sample2)
pdf = gaussian_kde(sum)
mean = np.mean(sum)
variance = np.var(sum)
skew = skew(sum)
kurtosis = kurtosis(sum)
doubles = np.count_nonzero(sum ==12)

print("The Mean of the Summation: ", mean, '\n')          #printing data
print("The Variance of the Summation: ", variance, '\n')
print("Skewness of the Summation: ", skew, '\n')
print("Kurtosis of the Summation: ", kurtosis, '\n')
print("The # of Double Sixes: ", doubles)

plt.hist(sum, density = True)                             #plotting data
plt.plot(x,pdf(x))
plt.show()
