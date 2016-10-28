def sieve(n):
    not_prime = []
    prime = []
    for i in xrange(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in xrange(i*i, n+1, i):
                not_prime.append(j)
    return prime
print "Till which integer you want to do the primality test?"
x = int(raw_input(">"))
print sieve(x)
