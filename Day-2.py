#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("Please enter the total bill amount to be paid: "))
people = float(input("How many people to split the bill into?: "))
tip = float(input("How much tip do you want to give?: "))
tip = tip/100
split = bill//people
final_split = split+(split*tip)
print(f"Each person should pay: ${final_split}")