
#In December 2020, a reddit user posted a plot (link below) of the number of primes of the form x^2+k against k and asked about the reason for the curves.
#I was able to reproduce the plot using known mathematics (the Bateman-Horn conjecture) though could not explain the reason for the curves.  The below shows how to 
#calculate the C function from the Bateman Horn conjecture.  This function estimates the density of primes in a polynomial by computing the number of composites 
#having a factor of a given prime over one period of that prime.  Link to the original post (not mine): 
#https://www.reddit.com/r/dataisbeautiful/comments/kmthuf/oc_number_of_primes_in_x2_n_for_2x1000000_and/



import sympy
from sympy import prime
import matplotlib.pyplot as plt

def xSquaredPlusK(x, k):
    return x**2 + k

curK = 1
ks = []
pis = []

thePrimes = []

for i in range(1, 30):
    thePrimes.append(prime(i))

# increase to 10,000 for the full plot matching the figure from reddit
for curK in range(1, 1000):
    if(curK % 100 == 0):
        print(curK)

    ks.append(curK)
    piPartials = 1
    for i in range(1, 30):
        p = thePrimes[i-1]
        ctSol = 0
        for j in range(p):
            if(xSquaredPlusK(j, curK) % p == 0):
                ctSol = ctSol + 1
        x = (1-1/p)**-1 * (1-ctSol/p)
        piPartials = piPartials * x
    pis.append(piPartials)

for k in ks:
    if((k%3)==1 and (k %5 == 2 or k%5 == 3) and ((k %7 == 1 or k%7==2 or k %7==4))):
        plt.scatter(k, pis[k-1], c='b')
    elif(((k)%3==0 or k%3==2) and (k%5==0 or k%5==1 or k%5==4)):
        plt.scatter(k, pis[k-1], c=['orange'])
    else: 
        plt.scatter(k, pis[k-1], c=['r'])
plt.show()