from itertools import count
 
def sieveOfSundaram(n):
    nk = (n-1)//2
    ks = list(range(nk+1))
 
    for i in count(1):
        step  = 2*i+1
        start = i*(step + 1)
        if start > nk:
            break
         
        ks[start::step] = (0 for _ in range(start, nk+1, step))
 
    prime = [2] + [2*k+1 for k in filter(None, ks)]

    return prime

print "Till which integer you want to do the primality test?"

x = int(raw_input(">"))

print sieveOfSundaram(x)