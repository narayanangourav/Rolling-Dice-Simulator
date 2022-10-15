import random
print("░R░o░l░l░i░n░g░ ░D░i░c░e░ ░S░i░m░u░l░a░t░o░r░")
simulator=True

while simulator:
    print("Rolled Number : ",random.randint(1,6))
    secondroll=input("Do you want to roll again? -> Y,y/N,n : ")
    if secondroll.lower() == "y" or secondroll.upper()=="Y":
        continue
    elif secondroll.lower() == "n" or secondroll.upper()=="N":
        print("Simulator Ended!")
        break
