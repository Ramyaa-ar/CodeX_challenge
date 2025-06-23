import random
def generate():
        return random.randint(1,6)
    
while True:
    choice=input("Do u wanna roll the dice:(y/n)\n").lower()
    if choice!='y':
          print("Thanks for playing,have a good day!")
          break
    res=generate()
    print("you rolled:",res)
