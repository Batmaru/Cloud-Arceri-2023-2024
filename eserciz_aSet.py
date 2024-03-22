import random
import time

# costruzione del set
start = time.time_ns()
aSet = set()
for v in range(1,10000000):
   aSet.add(random.randint(1, 1000000000))
end = time.time_ns()

print (f"il tempo richiesto è: {(end-start)/100000000}")

# ricerca nel set
     
start = time.time_ns()
trovati = 0
for v in range(1,10000000):
    if random.randint(1 , 1000000000) in aSet:
        trovati += 1
end = time.time_ns()

print (f"il tempo richiesto è: {(end-start)/100000000} e ne ha {trovati}")


     
