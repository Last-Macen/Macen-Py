secret_word = "Macen"
guess = ""
guess_count = 0
guess_limit = 3
limit = False

while guess != secret_word and not limit: #while user guess is not right and limit is not true
    if guess_count < guess_limit: 
       guess = input("Enter guess: ")
       guess_count += 1
    else :
         limit = True #change limit to True once count > guess limit
if limit:
    print("You are out of guesses you lose")
else:
    print("you win!! ")
