import math

def calculate_delta(a, b, c):
  delta = b**2 - 4*a*c
  return delta

# Example
a = 1
b = 5
c = 6

delta = calculate_delta(a, b, c)

print(delta)
