# A program that allows the user to enter his/her two favorite dishes
# and outputs a new food by joining the two original food names togetherself.

food1 = input("\nWhat is your favorite food? \nInput:\t")
food2 = input("\nSounds delicious, now enter another one. \nInput:\t")
combinedFood = food1 + food2
print("\nI don't about that one, but have you ever tried\n" + combinedFood,end="?\n")

input("\nPress enter to exit.\n")
