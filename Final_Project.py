
import tkinter as tk
import random

secret = ""
guesses = []
guesses_left = 7


def create_game():
    global secret, guesses, guesses_left
    secret_word_list = ["coding", "python", "coffee", "water", "milk", "programming", "cactus", "tree", "computer"]
    secret = random.choice(secret_word_list)
    guesses = []
    guesses_left = 7






root = tk.Tk()
root.title("Hangman Game")

secret_label = tk.Label(root, text="Secret word: ")
secret_label.pack(pady=20)

guess_label = tk.Label(root, text="Secret word: ")
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack(pady=20)

guess_button = tk.Button(root, text="Guess")
guess_button.pack()

create_game()
root.mainloop()