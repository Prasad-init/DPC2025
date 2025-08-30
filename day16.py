def gcd(a, b):
  while(b):
    a, b = b, a % b
  return a

def lcm(a, b):
  result = (a * b) // gcd(a, b)
  return result

N = 4
M = 6

print(lcm(N, M))
