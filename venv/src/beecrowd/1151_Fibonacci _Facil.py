
fibo =[0,1]

n = int(input())


while len(fibo) < n:
    fibo.append(fibo[-1] + fibo[-2])

for i in range(n):
    if i == n-1:
        print(fibo[i], end='\n')
    else:
        print(fibo[i], end=' ')




        
       
        
        


 


    
        
    
  
        
