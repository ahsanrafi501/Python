secret_number= 9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("Guess:"))
    guess_count+=1
    if guess==secret_number:
        print('You Won!')
        break
else: #this else is with while loop. In python the is else statement with while lopp
    print("Sorry,You failed")
    
