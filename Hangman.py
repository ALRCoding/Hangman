import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word_list = ["apple", "banana", "cherry", "grape", "kiwi", "orange", "lemon", "peach"]
        self.word = random.choice(self.word_list)
        self.guessed_letters = []

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.hangman_drawings = [
            """
              ------
              |    |
                   |
                   |
                   |
                   |
            """,
            """
              ------
              |    |
              O  |
                   |
                   |
                   |
            """,
            """
              ------
              |    |
              O  |
              |    |
                   |
                   |
            """,
            """
              ------
              |    |
              O  |
             /|    |
                   |
                   |
            """,
            """
              ------
              |    |
              O  |
             /|\   |
                   |
                   |
            """,
            """
              ------
              |    |
              O  |
             /|\   |
             /     |
                   |
            """,
            """
              ------
              |    |
              O  |
             /|\   |
             / \   |
                   |
            """
        ]

        self.attempts = 0
        self.max_attempts = len(self.hangman_drawings) - 1

        self.display_word_label = tk.Label(root, text="", font=("Arial", 24))
        self.display_word_label.pack(pady=20)

        self.guess_entry = tk.Entry(root, font=("Arial", 16))
        self.guess_entry.pack()

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.make_guess, font=("Arial", 16))
        self.submit_button.pack(pady=10)

        self.hangman_image = self.canvas.create_text(200, 200, text=self.hangman_drawings[self.attempts], font=("Arial", 16))

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if guess in self.guessed_letters:
            return

        self.guessed_letters.append(guess)

        display_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display_word += letter
            else:
                display_word += "_ "

        self.display_word_label.config(text=display_word)

        if guess not in self.word:
            self.attempts += 1
            if self.attempts <= self.max_attempts:
                self.canvas.itemconfig(self.hangman_image, text=self.hangman_drawings[self.attempts])
            else:
                self.display_word_label.config(text=f"You lost! The word was '{self.word}'.")
                self.submit_button.config(state=tk.DISABLED)

        if "_" not in display_word:
            self.display_word_label.config(text=f"Congratulations! You guessed the word '{self.word}'.")
            self.submit_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
