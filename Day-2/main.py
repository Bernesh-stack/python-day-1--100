#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("welcome to the tip calculator")
bill =int(input("what_was_the_total_bill"))
tip = int(input("what_percentage_tip_would_you_like_to_give"))
people = int(input("How_many_people_to_split_the_bill"))
tip_as_percentage = tip/100
total_tip_amount = bill*tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill /people
final_amount = round(bill_per_person,2)
print(f"each person should pay {final_amount}")
