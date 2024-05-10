# imports needed for the gui settings, as well as establishing messageboxes and random selection of word
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Word list for the game, more can be added but this is a fine baseline
words = ["python", "hangman", "game", "programming", "development", "coding", "water", "debugging"]


# Main class Hangman game
class HangmanGame:
    def __init__(self, master):  # The __init__ line set to self and master
        self.master = master
        self.master.title("Hangman Game")  # Titles the GUI
        self.master.geometry("900x500")  # Increases the window size

        # Sets the background image from the image within the zip folder
        self.background_image = Image.open("GUI_BG.jpg")  # Path to the image
        self.background_image = self.background_image.resize((900, 500))  # Sets the size and next line adds alt text
        self.background_photo = ImageTk.PhotoImage(self.background_image, name="Blue and gold background image")
        self.background_label = tk.Label(master, image=self.background_photo)  # Adds label to background
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Sets the positioning
        self.background_label.pack(expand=True, fill=BOTH)  # Positioning and fills the window

        self.word = random.choice(words)  # Picks a word at random from the aforementioned list
        self.guesses = []  # Stores each guess in a list
        self.lives = 6  # Sets the 'lives' or how many guesses you have
        self.incorrect_guesses = []  # Stores incorrect guesses for showing on the GUI

        # These lines are to create and position the canvas so  the imported image can be centered
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Set the background image onto the canvas
        self.canvas_image = Image.open("Gallows_BG.jpg")  # Path to your image
        self.canvas_image = self.canvas_image.resize((400, 400))  # Sets the size of the image
        self.canvas_image = ImageTk.PhotoImage(self.canvas_image, name="Cartoon image of a stockade")  # Alt text
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.canvas_image)  # Placement and setting of pic

        self.display_word = tk.StringVar()  # Displays the word that is to be guessed
        self.display_word.set("_ " * len(self.word))  # Hides it behind _______
        # Creates the label so the word is visible and then positions it
        self.word_label = tk.Label(master, textvariable=self.display_word, font=("Arial", 20))
        self.word_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Adds the label for the words next to input box and positions it
        self.guess_label = tk.Label(master, text="Guess a letter:", font=("Arial", 14), bg="Black", fg="White")
        self.guess_label.place(relx=0.30, rely=0.5, anchor=tk.CENTER)

        # Adds the input box and positions it
        self.guess_entry = tk.Entry(master, font=("Arial", 14))
        self.guess_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Adds the button to process the input guess and positions it
        self.guess_button = tk.Button(master, text="Guess", font=(
            "Arial", 14), command=self.make_guess, bg="Green", fg="White")
        self.guess_button.place(relx=0.65, rely=0.5, anchor=tk.CENTER)

        # Adds the button to restart the game and positions it
        self.restart_button = tk.Button(master, text="Restart", font=(
            "Arial", 14), command=self.restart_game, bg="Orange", fg="White")
        self.restart_button.place(relx=0.35, rely=0.7, anchor=tk.CENTER)

        # Adds the button to quit the game and positions it
        self.quit_button = tk.Button(master, text="Quit", font=(
            "Arial", 14), command=master.destroy, bg="Red", fg="White")
        self.quit_button.place(relx=0.65, rely=0.7, anchor=tk.CENTER)

        # Adds the label to display incorrect guesses and how many left counter
        self.guesses_label = tk.Label(master, text="Incorrect Guesses:", font=("Arial", 14))
        self.guesses_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    # Creates a function that processes each guess
    def make_guess(self):
        guess = self.guess_entry.get().lower()
        if len(guess) == 1 and guess.isalpha():
            if guess not in self.guesses:  # Adds guess to guesses list
                self.guesses.append(guess)
                if guess not in self.word:  # Checks if guess was wrong and adds it to incorrect guesses
                    self.lives -= 1
                    self.incorrect_guesses.append(guess)
                    self.update_display()
                elif self.lives == 0:  # Checks if out of guesses
                    self.game_over()
                else:
                    self.update_display()  # Updates display if guess was correct
            else:
                messagebox.showinfo("Invalid Guess", "You've already guessed that letter!")
        else:
            messagebox.showinfo("Invalid Guess", "Please enter a single letter.")

    # Creates a function to updates the gui display after each guess mostly just formatting
    def update_display(self):
        display = ""
        for char in self.word:
            if char in self.guesses:  # Adds it to the display showing guesses
                display += char + " "
            else:
                display += "_ "
        self.display_word.set(display)
        self.guesses_label.config(text=f"Incorrect Guesses: {', '.join(
            self.incorrect_guesses)} (Remaining: {self.lives})")  # Shows incorrect guesses
        if "_" not in display:
            messagebox.showinfo("Congratulations", f"You've guessed the word: {self.word}!")
            self.restart_game()  # For when word is guessed

    def game_over(self):
        messagebox.showinfo("Game Over", f"You've run out of lives! The word was: {self.word}")
        self.restart_game()  # For when you run out of guesses

    def restart_game(self):  # Restarts the game to default settings
        self.word = random.choice(words)
        self.guesses = []
        self.lives = 6
        self.display_word.set("_ " * len(self.word))
        self.guesses_label.config(text="Incorrect Guesses:")


# Main function to run game
def main():
    root = tk.Tk()  # Application  window
    HangmanGame(root)  # Creates an instance
    root.mainloop()  # Starts Tkinter loop


# Checks if being run directly
if __name__ == "__main__":
    main()
