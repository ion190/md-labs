# We all use many passwords every day but is every password we use hard enough to crack. Your password is considered strong if it follows this rules:
# -It has at least 8 characters and at most 20 characters.
# -It has a minimum of 1 lower case letter [a-z] and a minimum of 1 upper case letter [A-Z] and a minimum of 1 numeric character [0-9] and a minimum of 1 special character: ~`!@#$%^&*()-_+={}[]|\;:"<>,./?
# -It does not contain three repeating characters in a row (i.e.,“abbbcc-0”is weak, but  is “ abcbbcc-0”strong).
# - Shouldn’t contain any consecutive numbers
# Given a string password, return the minimum number of steps required to make the password strong. If the password is already strong, return the message “good”.
# In one step, you can:
# -Insert one character
# -Delete one character
# -Replace one character

def steps_to_strong(password):
    # Calculate the steps needed to make the password strong
    steps = 0

    # Add missing character types
    if not any(c.islower() for c in password):
        steps += 1
    if not any(c.isupper() for c in password):
        steps += 1
    if not any(c.isdigit() for c in password):
        steps += 1
    if not any(c in '~`!@#$%^&*()-_+={}[]|;:"<>,./?' for c in password):
        steps += 1

    # Ensure the length is between 8 and 20
    if len(password) < 8:
        steps += 8 - len(password) - steps
    elif len(password) > 20:
        steps += len(password) - 20 - steps

    # Remove repeating characters
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            steps += 1

    # Avoid consecutive numbers
    for i in range(len(password) - 1):
        if password[i].isdigit() and password[i + 1].isdigit() and abs(
                int(password[i]) - int(password[i + 1])) == 1:
            steps += 1

    return steps


password = str(input('Input password: '))
steps = steps_to_strong(password)
if steps == 0:
    print('Good password')
else:
    print('Steps required to make the password strong: ', steps)

