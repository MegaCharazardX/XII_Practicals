
print("IMAGINARY DICE")
import random, time 
C= True
while C:
    print ("Dice rolling...")
    time.sleep(2)
    a=random.randint (1,6)
    print (a)
    b=input ("Do you want to roll the dice once more (y/n)?")
    if b== 'y':
        continue
    else:
        C=False
print ("In GAME OVER...") 