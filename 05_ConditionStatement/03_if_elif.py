employee_name = input("Enter employee name: ")
employee_salary = float(input("Enter employee salary: "))
performance_rating = float(input("Enter performance rating (1.0 to 5.0): "))

if performance_rating < 1.0 or performance_rating > 5.0:
    print("Invalid performance rating! Please enter a value between 1.0 and 5.0.")
else:
     if performance_rating >= 4.5:
        bonus_percentage = 20
     elif performance_rating >= 4.0:
        bonus_percentage = 15
     elif performance_rating >= 3.5:
        bonus_percentage = 10
     elif performance_rating >= 3.0:
        bonus_percentage = 5
     else:
        bonus_percentage = 0
        print("\nEmployee Bonus Details:")
        
     bonus_amount = (employee_salary * bonus_percentage) / 100
     print("\nEmployee Bonus Details:")
     print(f"Employee Name: {employee_name}")
     print(f"Employee Salary: ${employee_salary:.2f}")
     print(f"Performance Rating: {performance_rating}")
     print(f"Bonus Percentage: {bonus_percentage}%")
     print(f"Bonus Amount: ${bonus_amount:.2f}")

     if bonus_percentage >= 15:
        print("Congratulations! You are eligible for a promotion.")
     else:
        print("Keep up the good work! You are not eligible for a promotion yet.")

        