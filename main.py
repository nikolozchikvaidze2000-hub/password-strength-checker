
print("===================================")
print("       PASSWORD STRENGTH CHECKER")
print("===================================")

print("This program checks password complexity.")
print("Use a fictional test password, not your real password.")
print()

password = input("Enter a test password: ")

score = 0

if len(password) >= 8:
    score = score + 1

if len(password) >= 12:
    score = score + 1

if any(ch.isupper() for ch in password):
    score = score + 1

if any(ch.islower() for ch in password):
    score = score + 1

if any(ch.isdigit() for ch in password):
    score = score + 1

if any(not ch.isalnum() for ch in password):
    score = score + 1

print()
print("========== RESULTS ==========")

print("Password length:", len(password))
print("Security score:", score, "/ 6")

if score >= 5:
    print("Strength: STRONG")
elif score >= 3:
    print("Strength: MEDIUM")
else:
    print("Strength: WEAK")

print()
print("========== RECOMMENDATIONS ==========")

if len(password) < 12:
    print("- Use at least 12 characters.")

if not any(ch.isupper() for ch in password):
    print("- Add uppercase letters.")

if not any(ch.islower() for ch in password):
    print("- Add lowercase letters.")

if not any(ch.isdigit() for ch in password):
    print("- Add numbers.")

if not any(not ch.isalnum() for ch in password):
    print("- Add special characters.")

if score >= 5:
    print("Good job! Your password meets most of the checks.")

print()
print("Thank you for using Password Strength Checker!")
