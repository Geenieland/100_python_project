print("Welcome to the tip calculator! ")
bill = input("What was the total bill? ")
give = input("How much tip would you like to give?  10, 12, or 15? ")
split = input("How many people to split the bill? ")

a_bill = float(bill)
a_give = float(give)
a_split = float(split)

tip = (a_bill + a_bill * (a_give / 100) ) / a_split
real_tip = round(tip, 2)
real_tip = "{:.2f}".format(tip)
print(f"Each person should pay: {real_tip} ")


or


print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give?  10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_anmout = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: {final_anmout} ")
