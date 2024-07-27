# Write your solution here
pin = 4321 
count = 0
while True:
    p = int(input("PIN: "))
    count += 1
    
    if pin == p:
        success = True
        break
        # print("Correct! It only took you one single attempt!")

    print("Wrong") 

if count == 1: 
    print("Correct! It only took you one single attempt!")
else: 
    print(f"Correct! It took you {count} attempts")