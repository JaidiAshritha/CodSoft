import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("=" * 55)
print("        ✊ ROCK • 📄 PAPER • ✂ SCISSORS")
print("=" * 55)

print("""
GAME RULES:
✔ Rock beats Scissors
✔ Scissors beats Paper
✔ Paper beats Rock
""")

while True:
    user_choice = input("\nEnter Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print("❌ Invalid Choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("\n" + "-" * 45)
    print(f"👤 You Chose      : {user_choice.upper()}")
    print(f"💻 Computer Chose : {computer_choice.upper()}")
    print("-" * 45)

    if user_choice == computer_choice:
        print("🤝 It's a TIE!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("CONGRATULATIONS! 🎉 You WIN this round!")
        user_score += 1

    else:
        print("😢 Computer WINS this round!")
        computer_score += 1

    print("\n📊 SCORE BOARD")
    print("-" * 20)
    print(f"👤 Your Score      : {user_score}")
    print(f"💻 Computer Score  : {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n" + "=" * 55)
        print("        🎮 FINAL GAME RESULT 🎮")
        print("=" * 55)

        print(f"\n👤 Your Final Score      : {user_score}")
        print(f"💻 Computer Final Score  : {computer_score}")

        if user_score > computer_score:
            print("\n🏆 CONGRATULATIONS! YOU ARE THE CHAMPION!")

        elif computer_score > user_score:
            print("\n💻 COMPUTER IS THE CHAMPION!")

        else:
            print("\n🤝 THE GAME ENDED IN A DRAW!")

        print("\n✨ Thanks for Playing!")
        break