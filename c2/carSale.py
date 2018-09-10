# A program which adds bullshit fees to the base price of a carself.

carTax = 1.15
carLicence = 1.05
dealerPrep = 125
destCharge = 50

print("_"*50)
basePrice = float(input('''
Hello! I am the Car Sale 2000 Ultitron Calculator.
Designed to add incredible fees for your profit!

How much is the car worth?
Input: $'''))

print("_"*50)

print("Calculating new price...")
print("_"*50)

salesPrice = float(basePrice * carTax * carLicence + dealerPrep + destCharge)
print("\nThe vehicle should be sold for the cost of $"+str(salesPrice),end="\n")

print("_"*50)

input("\nWelcome Again!\nPress Any Key To Exit.")
print("_"*50)
print("\nApplication Terminated.")
print("_"*50)
