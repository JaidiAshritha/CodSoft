import random
import string

def generate_password(length):
    """
    Generates a strong random password
    using letters, numbers, and symbols.
    """

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("\n" + "=" * 45)
print("        🔐 PASSWORD GENERATOR 🔐")
print("=" * 45)

try:
    length = int(input("\nEnter Password Length: "))
    
    if length <= 0:
        print("\n❌ Length must be greater than 0")

    else:
        password = generate_password(length)

        print("\n" + "-" * 45)
        print("✅ Your Secure Password is:")
        print(f"\n   {password}")
        print("-" * 45)

        print("\n🔒 Password Strength: STRONG")
        print("✨ Password Generated Successfully!\n")

except ValueError:
    print("\n❌ Please enter a valid number.")