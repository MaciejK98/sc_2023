import numpy as np

def RandomGenerator(X):
  a= 16807
  q= 127773
  r= 2836
  
  m =(a * q)+ r
  print("m: ", m)
  h = np.floor(X / q)
  print("h: ",h)
  k=np.floor(X/q)
  
  random = (a * (X - (q * h))) - (r * h)
  if(random < 0):
    random = random + m
  return random
