from replit import clear
#Display art
from art import logo
from art import vs

print(logo)
#import
from game_data import data
import random

keep_playing = True
random_account2 = random.choice(data)
while keep_playing == True:
    #generate random acoount
    random_account = random_account2
    random_account2 = random.choice(data)
    if random_account == random_account2:
        random_account2 = random.choice(data)

    c = random_account['follower_count']
    d = random_account2['follower_count']

    current_score = 0
    #choice = input("Who has more followers? Type A or B: ")

    #while keep_playing == True:
    a = f"Compare A: {random_account['name']}, a {random_account['description']} from {random_account['country']}"
    print(a)
    print(vs)
    b = f"Compare B: {random_account2['name']}, a {random_account2['description']} from {random_account2['country']}"
    print(b)

    choice = input("Who has more followers? Type A or B: ").lower()
    if choice == 'a':
        if c > d:
            current_score += 1
            clear()
            print(f"You're right! current score: {current_score}")
        else:
            print(f"You're wrong current score: {current_score}")
            keep_playing = False

    elif choice == 'b':
        if d > c:
            current_score += 1
            clear()
            print(f"You're right! current score: {current_score}")
        else:
            print(f"You're wrong current score: {current_score}")
            keep_playing = False
