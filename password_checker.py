import re

def password_strength(password):

    checks = [
        (r'.{8,}', " at least 8 characters\n"),
        (r'[A-Z]', " at least one uppercase letter\n"),
        (r'[a-z]', " at least one lowercase letter\n"),
        (r'\d', " at least one digit\n"),
        (r'[\W_]', " at least one special character")
    ]

    feedback = []

    for pattern, message in checks:
        
        if not re.search(pattern, password):
            feedback.append(message)

    if len(feedback) == 0:
        return "Strong: Password meets all criteria!"
    
    else:
        return f"Weak: Your password should contain:\n{"".join(feedback)}"

while True:
    user_password = input("Enter a password: ")
    result = password_strength(user_password)
    print(result)
