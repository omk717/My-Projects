email = input("Enter Your Email: ")  # e.g., g@g.in, wscube@gmail.com

# Initialize flags for validation
has_space = False
has_uppercase = False
has_invalid_char = False

# Check if the email length is sufficient
if len(email) >= 6:
    # Check if the email starts with an alphabetic character
    if email[0].isalpha():
        # Check for exactly one '@' symbol
        if "@" in email and email.count("@") == 1:
            # Check if the domain suffix is valid
            # The domain suffix must end with a dot before the domain
            if (email[-4] == "." or email[-3] == ".") and email[-3:].isalpha():
                # Validate each character in the email
                for char in email:
                    if char.isspace():
                        has_space = True
                    elif char.isalpha():
                        if char.isupper():
                            has_uppercase = True
                    elif char not in "_.@0123456789":
                        has_invalid_char = True

                # Print results based on validation flags
                if has_space:
                    print("Wrong Email 5: Email contains spaces.")
                elif has_uppercase:
                    print("Wrong Email 5: Email contains uppercase letters.")
                elif has_invalid_char:
                    print("Wrong Email 5: Email contains invalid characters.")
                else:
                    print("Email is valid.")
            else:
                print("Wrong Email 4: Invalid domain suffix.")
        else:
            print("Wrong Email 3: Incorrect number of '@' symbols.")
    else:
        print("Wrong Email 2: Email must start with an alphabetic character.")
else:
    print("Wrong Email 1: Email is too short.")
