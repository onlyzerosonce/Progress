import os
import time
import tkinter as tk
from tkinter import scrolledtext

def consume_media(text_area):
    """
    This function will consume media from the predefined directories.
    """
    directories = [
        "0.SelfImprovement",
        "1.AIML",
        "2.Programming",
        "3.Investment",
        "4.SkillPolish",
        "5.Entertainment"
    ]

    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

    for directory in directories:
        if os.path.exists(directory):
            text_area.insert(tk.INSERT, f"Consuming media from: {directory}\n")
            for root, _, files in os.walk(directory):
                for file in files:
                    filepath = os.path.join(root, file)
                    text_area.insert(tk.INSERT, f"  - Consuming: {filepath}\n")
                    # Simulate media consumption
                    time.sleep(1)
            text_area.insert(tk.INSERT, "-" * 20 + "\n")

def main():
    window = tk.Tk()
    window.title("Media Consumer")

    text_area = scrolledtext.ScrolledText(window, width=80, height=20)
    text_area.pack(pady=10, padx=10)

    consume_button = tk.Button(window, text="Consume Media", command=lambda: consume_media(text_area))
    consume_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
