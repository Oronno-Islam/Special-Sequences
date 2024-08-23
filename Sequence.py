def Fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return Fibonacci(n - 1) + Fibonacci(n - 2)


def LucasNumber(n):
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return LucasNumber(n - 1) + LucasNumber(n - 2)


def Zekendorf(n):
  fibs = [1, 2]
  
  while fibs[len(fibs) - 1] <= n:
    fibs.append(fibs[len(fibs) - 1] + fibs[len(fibs) - 2])
  fibs.pop()
  
  result = []
  
  while n >0:
    largest = max(f for f in fibs if f <=n)
    result.append(largest)
    n-= largest
    fibs.remove(largest)  
      
  return f"Zeckendorf representation of {sum(result)}: {result}"


