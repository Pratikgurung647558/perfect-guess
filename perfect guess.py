import random  
 
n = random.randint(1,100)         #computer chooses random

a = -1    #for staring the loop
chance=0      #for no. of guesses
while(a != n):
    a =  int(input("enter the no."))  
    chance+=1
    if(a < n):
        print("the input number is smaller than the generated no.")
    elif(a>n):
        print("the input number is greater than generated no.")
    else:
        print(f"the no. {n} is matched and no. of guess {chance}")


#performance comments
if(chance <= 5):
    print("brilliant guesses")
elif(chance >= 6 & chance <= 10):
    print("good Guesses")
elif(chance >= 11 & chance <= 20 ):
    print("fine guesses")
else:
    print("bad guesses")
    
