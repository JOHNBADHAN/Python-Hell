# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password: ")
pass_length = len(password)

if pass_length < 6:
    strength = "Weak"

elif pass_length <=10:
    strength = "Medium"

elif pass_length > 10:
    strength = "Strong"

print(f"The Strength of your password is {strength}")