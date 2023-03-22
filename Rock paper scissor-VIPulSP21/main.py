a=input()

import random
computer = random.choice(["rock","paper","scissor"])

if(a=="rock" and computer=="paper"
 or a=="scissor" and computer=="rock"
 or a=="paper" and computer=="scissor"):
   print(computer+" beats "+a)
     
elif(computer=="rock" and a=="paper" 
    or computer=="scissor" and a=="rock" 
    or computer == "paper" and a =="scissor"): 
   print(a + " beats "+ computer) 
      
else:
   print("draw")

