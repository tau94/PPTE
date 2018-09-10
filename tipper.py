# A program that displays a 15% tip and a 20% tip for restaurant visitors.

print('''
Greetings!
I am the tip calculator.''')
bill = float(input("\nHow much is the bill in $?\nInput without sign: "))

tip15 = float(bill * 0.15)
tip20 = float(bill * 0.2)

print("\nA fifteen percent tip is $"+str(tip15),end="\n")
print("The total is $"+str(tip15+bill),end="\n")
print("\nA twenty percent tip is $"+str(tip20),end="\n")
print("The total is $"+str(tip20+bill),end="\n")
input("\nHave a pleasant day!\nPress Any Key To Exit.\n\n")
