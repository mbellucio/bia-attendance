def ehprimo(num):
  divisores = 0
  i = 1
 
  if num % 2 == 0:
    divisores = 2

  if divisores == 2:
    return True
  else:
    return False
  
print(ehprimo(13))