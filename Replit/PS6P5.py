print("Enter your last name")
last_name = input()
print("Enter your salary")
salary = float(input())
print("Enter your job level")
job_level = int(input())
bonus_rate = 0
if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5 and job_level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

bonus = salary * bonus_rate

print("Last name: ", last_name)
print("Bonus: ", bonus)