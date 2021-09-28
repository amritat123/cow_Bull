
player_name=input("please enter your player name=")
print("________________________________________________")
print("WELCOME:-", player_name)
print("________________________________________________")
print("IN COW BULL GAME:---")

import random 
  

def secr_number(num):
    return [int(i) for i in str(num)]
      
      
def no_Duplicates(num):
    num_1= secr_number(num)
    if len(num_1) == len(set(num_1)):
        return True
    else:
        return False
  
  
def generate_Num():
    while True:
        num = random.randint(1000,9999)
        if no_Duplicates(num):
            return num
  

def num_of_Bulls_Cows(num,guess):
    bullcow = [0,0]
    num_1= secr_number(num)
    guess_1 = secr_number(guess)
      
    for i,j in zip(num_1,guess_1):
          
        
        if j in num_1:
          
           
            if j == i:
                bullcow[0] += 1
              
          
            else:
                bullcow[1] += 1
                  
    return bullcow
      
      

num = generate_Num()
your_turns =int(input('please Enter number of tries: '))


while your_turns > 0:
    guess = int(input("Enter your guess: "))
      
    if not no_Duplicates(guess):
        print("Number should be not repeated . Try again.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again.")
        continue
      
    bullcow = num_of_Bulls_Cows(num,guess)
    print(f"{bullcow[0]} bulls, {bullcow[1]} cows")
    your_turns -=1
      
    if bullcow[0] == 4:
        print("woww! You guessed right number ")
        break
else:
    print(f"You ran out of tries. Number was {num}")
