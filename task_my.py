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
user_choice = int(input("What do you choose? type 0 for rock, 1 for paper and 2 for scissors:\n"))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)

game_choice = random.randint(0, 2)
print(game_choice)
rock = 0
paper = 1
scissors = 2

print("Computer chose:\n")
if game_choice == 0:
    print(rock)
elif game_choice == 1:
    print(paper)
elif game_choice == 2:
    print(scissors)
# r p s
# r r =>draw
# r p =>p
# r s =>r
# p p =>draw
# p r =>p
# p s =>s
# s s =>draw
# s r =>r
# s p =>s
if user_choice == game_choice:
    print("draw")
elif user_choice > game_choice:
    print("you win")
elif user_choice < game_choice:
    print("you lose")
