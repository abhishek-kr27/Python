# Tip Calculator
print("Welcome to the Tip Calculator.")
Total_Bill =float(input("What was the total bill? $ "))
Tip = float(input("What percentage tip would you like to give? 10 , 12, or 15?  "))
People =int(input("How many people to split the bill?  "))

Bill_per_person= (Total_Bill * ((100+Tip)/100))/People
Bill = round(Bill_per_person,2) # round off till 2 decimal places not including 0 only 33.3
Bill= "{:.2f}".format(Bill_per_person) # round off till 2 decimal places including 0 like 33.30
print(f"Each person should pay : ${Bill}")