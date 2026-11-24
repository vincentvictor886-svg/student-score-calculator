# Interactive Student Registration and Score Calculator

print("=== Student Registration and Score Calculator ===\n")

# 1. First name and surname
first_name = input("Enter your first name: ").strip().title()
surname = input("Enter your surname: ").strip().title()

# 2. Age
age = int(input("Enter your age: "))

# 3. Department
department = input("Enter your department: ").strip().title()

# 4. Scores for three subjects
score1 = float(input("Enter score for subject 1: "))
score2 = float(input("Enter score for subject 2: "))
score3 = float(input("Enter score for subject 3: "))

# 5. Total score
total_score = score1 + score2 + score3

# 6. Average score
average_score = total_score / 3

# 7. Display student information using f-strings
print("\n===== Student Information =====")
print(f"Full Name  : {first_name} {surname}")
print(f"Age        : {age}")
print(f"Department : {department}")
print(f"Scores     : {score1}, {score2}, {score3}")
print(f"Total Score  : {total_score}")
print(f"Average Score: {average_score:.2f}")
