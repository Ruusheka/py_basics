import random
from  art import logo,vs
from game_data import data
score=0
def detail(acc):
    acc_name=acc["name"]
    acc_desc=acc["description"]
    acc_country=acc["country"]
    return f"{acc_name} {acc_desc} {acc_country}"

def follower(ac1,ac2,n):
    if ac1>ac2:
        return n=="a"
    else:
        return n=="b"

print(logo)
game=True
acc2=random.choice(data)

while game:
    acc1=acc2
    acc2=random.choice(data)
    if acc1==acc2:
        acc2=random.choice(data)
    print(f"compare A :{detail(acc1)}")
    print(vs)
    print(f"Against B :{detail(acc2)}")
    ch=input("Who has more followers ?'A' or 'B'")

    print(logo)

    acc1_follower=acc1["follower_count"]
    acc2_follower=acc2["follower_count"]

    high_follower= follower(acc1_follower,acc2_follower,ch)

    if high_follower:
        score+=1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game = False