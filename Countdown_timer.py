# Import time to take time as a inbuilt function 
import time
def cotdon(t):
    # Loop to traverse till zero
    while t>0:
        print(t)
        t -=1  
        # To decrease number one by one
        time.sleep(1)
        # Decreasing with respect time
    print("Time's up!!")

# normal input 
print("How many seconds to count-down?")
sec=input("Enter second:\n")

print("Countdown starts")
time.sleep(1)
# To handle the error in the prgm.
while not sec.isdigit():
    print("There wasn't an integer number! Enter proper nummber....")
    sec = input()
sec=int(sec)
cotdon(sec)
