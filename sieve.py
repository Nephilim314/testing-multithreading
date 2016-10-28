"""
Finding prime numbers in different methods while using multithreading.
Commented out sections can be used if I want to return them as a list

"""
import math
import time
import threading


def sieveOfEratosthenes(n):
    not_prime = []
    for i in xrange(2, n+1):
        # prime = []
        # time.sleep(0.001)
        if i not in not_prime:
            print "Erastothenes says "+ str(i)+ " "
            # prime.append(i)
            for j in xrange(i*i, n+1, i):
                not_prime.append(j)
    # return prime


def sieveOfAtkin(limit):
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        # prime = []
        #time.sleep(0.001)
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] :
            # prime.append(p)
            # return prime
            print "Atkin says " + str(p) + " "
 
x = 1000
t = time.time()

thread1 = threading.Thread(target=sieveOfEratosthenes, args=(x,))
thread2 = threading.Thread(target=sieveOfAtkin, args=(x,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

#sieveOfEratosthenes(x)
#sieveOfAtkin(x)

print "Completed in ", time.time()-t
