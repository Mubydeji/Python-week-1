import random
import os

SCORE_FILE = "high_scores.txt"


# ---------------- High Score Persistence ----------------
def load_scores():
    if not os.path.exists(SCORE_FILE):
        return []

    with open(SCORE_FILE, "r") as f:
        return [int(line.strip()) for line in f if line.strip().isdigit()]


def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        for score in scores[:5]:
            f.write(str(score) + "\n")


def update_high_scores(attempts):
    scores = load_scores()
    scores.append(attempts)
    scores.sort()
    save_scores(scores)


# ---------------- Game Logic ----------------
def play_round(max_range):
    secret = random.randint(1, max_range)
    attempts = 0

    print(f"\nGuess the number between 1 and {max_range}")

    while True:
        guess = input("Your guess: ")

        if not guess.isdigit():
            print("Enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! Attempts used: {attempts}")
            return attempts


# ---------------- Main Game ----------------
def guessing_game():
    max_range = 10
    win_streak = 0

    print("ADAPTIVE GUESSING GAME")

    while True:
        attempts = play_round(max_range)
        update_high_scores(attempts)

        win_streak += 1
        if win_streak >= 2:
            max_range += 10
            win_streak = 0
            print("Difficulty increased!")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break

    print("\nTop 5 High Scores:")
    for i, score in enumerate(load_scores(), start=1):
        print(f"{i}. {score} attempts")


# ---- START GAME ----
guessing_game()
