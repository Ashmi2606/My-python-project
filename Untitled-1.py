import math
n=12
count=0
for i in range(1,int(math.sqrt(n)+1)):
    if n%i==0 and i!=n//i:

        count+=2
    print("it is not prime",count)                    
if count==2:
    print("it is prime",count)
else: