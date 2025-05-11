# Artificial Intelligence GUI Script
# Coded by Pakistani Ethical Hacker Mr. Sabaz Ali Khan
# This script creates a simple GUI with a chatbot-like AI using Tkinter
# The AI responds to basic user inputs with predefined responses

import tkinter as tk
from tkinter import messagebox
import datetime

# Dictionary for simple AI responses
responses = {
    "hello": "Hi! How can I assist you today?",
    "how are you": "I'm doing great, thanks for asking!",
    "what is ai": "Artificial Intelligence is the simulation of human intelligence in machines.",
    "who are you": "I'm an AI created by Mr. Sabaz Ali Khan, an ethical hacker from Pakistan!",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}.",
    "bye": "Goodbye! Stay safe and secure!"
}

class AIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI GUI by Sabaz Ali Khan")
        self.root.geometry("500x400")
        self.root.configure(bg="#2c3e50")

        # Title Label
        self.title_label = tk.Label(
            root,
            text="Artificial Intelligence GUI\nCoded by Mr. Sabaz Ali Khan",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        self.title_label.pack(pady=10)

        # Chat Display
        self.chat_display = tk.Text(
            root,
            height=15,
            width=50,
            font=("Arial", 10),
            bg="#34495e",
            fg="#ecf0f1",
            state="disabled"
        )
        self.chat_display.pack(pady=10)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#2c3e50")
        self.input_frame.pack(pady=5)

        # Input Field
        self.input_field = tk.Entry(
            self.input_frame,
            width=40,
            font=("Arial", 10),
            bg="#34495e",
            fg="#ecf0f1"
        )
        self.input_field.pack(side=tk.LEFT, padx=5)
        self.input_field.bind("<Return>", self.send_message)

        # Send Button
        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            command=self.send_message,
            font=("Arial", 10),
            bg="#3498db",
            fg="#ecf0f1"
        )
        self.send_button.pack(side=tk.LEFT)

        # Clear Button
        self.clear_button = tk.Button(
            root,
            text="Clear Chat",
            command=self.clear_chat,
            font=("Arial", 10),
            bg="#e74c3c",
            fg="#ecf0f1"
        )
        self.clear_button.pack(pady=5)

    def send_message(self, event=None):
        user_input = self.input_field.get().strip().lower()
        if not user_input:
            messagebox.showwarning("Input Error", "Please enter a message!")
            return

        # Enable text widget to insert message
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, f"You: {user_input}\n")

        # Get AI response
        ai_response = responses.get(user_input, "Sorry, I don't understand that. Try something like 'hello' or 'what is ai'.")
        self.chat_display.insert(tk.END, f"AI: {ai_response}\n\n")
        
        # Scroll to the end
        self.chat_display.see(tk.END)
        self.chat_display.config(state="disabled")
        
        # Clear input field
        self.input_field.delete(0, tk.END)

    def clear_chat(self):
        self.chat_display.config(state="normal")
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state="disabled")

def main():
    root = tk.Tk()
    app = AIGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()