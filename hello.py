def prime(n):
  if n<=1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

for j in range(2,50):
  if prime(j):
    print(j,end=" ")

