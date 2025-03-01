print(F"The result is {10 + 5}")

first_name = "John"
last_name = "Doe"
print(f"Full name: {first_name} {last_name}")

integer_value = 42
float_value = 23.5
print(f"Integer: {integer_value}")
print(f"Float: {float_value}")


fruits = ["apple", "banana", "orange"]
print(f"First fruit: {fruits[0]}")
print(f"All fruits: {', '.join(fruits)}")


x = 10
y = 5
print(f"Addition: {x + y}")
print(f"Multiplication: {x * y}")
print(f"Division with 2 decimal places: {x / y:.2f}")


numbers = [1, 2, 3, 4, 5]
text = "python"
print(f"List length: {len(numbers)}")
print(f"Maximum value: {max(numbers)}")
print(f"Uppercase text: {text.upper()}")



score = 85
print(f"Result: {'Pass' if score >= 70 else 'Fail'}")

# x > 10 ? 'Pass' : 'Fail'


value = 85
print(f"Status: {'High' if value > 75 else 'Medium' if value > 25 else 'Low'}")


stock_level = 15
reorder_point = 20
price = 49.99
print(f"Stock Alert: {'Order more' if stock_level < reorder_point else 'Stock OK'}")
print(f"Total Value: ${stock_level * price:.2f}")


value = 75
threshold = 50
multiplier = 1.5
result = value > threshold
adjusted_value = value * multiplier if result else value
print(f"Adjusted Value: {adjusted_value}")
print(f"Status: {'Exceeds threshold' if result else 'Within limits'}")


x = 100
y = 200
print(f"{x=}, {y=}")
print(f"{x + y=}")


pi = 3.14159
price = 19.99999
percentage = 0.89665 #89.66%
percentage = 1.896 #189.600000%
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Price rounded to 2 decimals: {price:.2f}")
print(f"Percentage with 1 decimal: {percentage:.2%}")



population = 1234567
revenue = 1234567.89
# Using comma as thousand separator
print(f"Population: {population:,}")
print(f"Revenue: ${revenue:,.2f}")
# Using underscore as thousand separator
print(f"Population: {population:_}")
print(f"Revenue: ${revenue:_.2f}")


name = "Python"
width = 20
print(f"Left aligned:   |{name:<20}|")
print(f"Right aligned:  |{name:>20}|")
print(f"Center aligned: |{name:^20}|")


customer_id = 42
invoice_number = 157
print(f"Customer ID: {customer_id:04d}")
print(f"Invoice: INV-{invoice_number:05d}")


name = "Alice"
role = "Data Scientist"
experience = 5
print(f"Name: {name}\nRole: {role}\nExperience: {experience} years")


profile = f"""
Team Member Profile:
------------------
Name: {name}
Role: {role}
Experience: {experience} years
"""
print(profile)





title = "Sales Analysis"
period = "Q3 2024"
sales = 150000
growth = 27.5
header = f"""
{title}
{'=' * len(title)}
Period: {period}
"""
metrics = f"""
Performance Metrics:
- Total Sales: ${sales:,}
- Growth Rate: {growth}%
"""
notes = f"""
Additional Notes:
- All figures are preliminary
- Data updated as of {period}
"""
# Combining all sections
full_report = f"{header}\n{metrics}\n{notes}"
print(full_report)



