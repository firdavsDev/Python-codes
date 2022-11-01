import math

def print_tub(n):
     for num in range(2,n):
        if all(num%i!=0 for i in range(2, int(math.sqrt(num))+1)):
         print(num)
         
print_tub(100)

