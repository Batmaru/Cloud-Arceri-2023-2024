import random
import time

start = time.time_ns()
lista=[]
for v in range(1,10000000):
   
   lista.append(random.randint(1, 1000000000))
end = time.time_ns()

print (f"il tempo richiesto è: {(end-start)/1000000000}")
