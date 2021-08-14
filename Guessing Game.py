import random


print("******************WELCOME TO GUESSING THE NUMBER GAME*******************")
print("        ")
user_input = int(input("Enter the number up till which you want to guess: "))

print("")

Rnd_no = random.randint(1,user_input)

guess =0
Attempt = 0
print("You have 5 attempts")
print("")
while guess != Rnd_no and Attempt < 6:
	guess = int(input(f"Enter a number between 1 and {user_input}: "))
	Attempt += 1
	if guess > Rnd_no and guess <= user_input:
		print("To high")
	elif guess < Rnd_no and guess >= 1:
		print("Too low")
	elif guess > user_input or guess < 1:
		print("Invalid-Try again")	
	else:
		print("")
		print("Correct guess")
		print(f"You used {Attempt} attempts")

	if Attempt > 5:
	 print("")
	 print("You have used all your attempts ")
	 print(f"The correct guess was {Rnd_no}")
	 
     
		
