salary = float(input("Enter employee salary: ₹"))

bonus = salary * 0.10
salary_with_bonus = salary + bonus
tax = salary_with_bonus * 0.05
final_salary = salary_with_bonus - tax

print(f"Original Salary: ₹{salary}")
print(f"Bonus Added: ₹{salary_with_bonus}")
print(f"After Tax Deduction: ₹{final_salary}")
