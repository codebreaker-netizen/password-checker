import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Use at least one special character")

    return score, feedback


def main():
    password = input("Enter your password: ")

    score, feedback = check_password_strength(password)

    print("\nPassword Strength Score:", score, "/ 5")

    if score == 5:
        print("Strong password 💪")
    elif score >= 3:
        print("Moderate password ⚠️")
    else:
        print("Weak password ❌")

    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print("-", tip)


if __name__ == "__main__":
    main()