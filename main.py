import os, time

s=""

def factorial(number):
  if number==1:
    return 1
  else:
    fact=number*factorial(number-1)
    return fact
  

while True:
  print(f"{s:^18}\033[33mMy Factorials")
  try: 
    num=int(input("Enter a number: "))
  except:
    print("Enter an integer only")
  print(f"The factorial of {num} is {factorial(num)}")
  time.sleep(1.5)
  os.system("clear")
      
    
 
    

  
 
  
    
  

   
  
    

  