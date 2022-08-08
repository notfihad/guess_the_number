import random
print("Welcome to Guess The Number Game\n")

def input_check() :
    valid = False
    while not valid: 
        try:
            global G_num
            G_num = int(input('Enter your guess: '))
            valid = True 
        except ValueError:
            print('Please only input digits')
  
def check() :
    for x in range(1,8) :
        print("Attempt no "+str(x))
        input_check()
        if G_num == O_num :
            print("Congratulations, you have guessed it right")
            exit()
        elif x!=7 :
            print("Your guessed number was wrong")
            hint= abs(O_num-G_num)
            if hint<=5 :
                print("Your number is (+/-) 5 off the original number\n")
            elif hint<=10 :
                print("Your number is (+/-) 10 off the original number\n")
            else :
                extra=10-abs(O_num-G_num)%10
                hint= abs(O_num-G_num)+extra
                randomize =[hint,hint+10,hint-10]
                hint=random.choice(randomize)
                print("Your number is (+/-) "+str(hint)+" off the original number\n")
        else :
            print("Sorry all your guesses were wrong.The number was"+str(O_num))

def num_generator() :
    global O_num    
    O_num = random.randint(0,100)
    print("We have a random number between 0 to 100.You have 7 attempts.Can you guess it ??")
    check()
num_generator()

z=input("Wanna try again? Press Y for yes or N for no")
if z =="Y" or "y" :
    num_generator()
else :
    exit()
exit()

