import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
comp=[rock, paper, scissors]
user=input('choose 0 for Rock,1 for Paper,2 for Scissors')
if user == '0':
    print('You chose',comp[0])
    n=random.randint(0,2)
    print('but computer chose',comp[n])
    if n==1:
        print('you loss')
    elif n==2:
        print('you Win')
    elif n==0:
        print("it's a draw")
elif user == '1':
    print('You chose',comp[1])
    n=random.randint(0,2)
    print('but computer chose',comp[n])
    if n==2:
        print('you loss')
    elif n==0:
        print('you Win')
    elif n==1:
        print("it's a draw")
elif user == '2':
    print('You chose',comp[2])
    n=random.randint(0,2)
    print('but computer chose',comp[n])
    if n==0:
        print('you loss')
    elif n==1:
        print('you Win')
    elif n==2:
        print("it's a draw")
else:
    print('wrong input')