import tkinter as tk
from openai import OpenAI
from dotenv import load_dotenv
import os

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")

        self.chat_display = tk.Text(root, bg="white", height=15, width=50)
        self.chat_display.pack()

        self.user_input = tk.Entry(root, bg="lightgray", width=40)
        self.user_input.pack()

        self.send_button = tk.Button(root, text="Send", command=self.respond)
        self.send_button.pack()

    def respond(self):
        user_text = self.user_input.get()
        self.chat_display.insert(tk.END, "You: " + user_text + "\n")
        self.user_input.delete(0, tk.END)

        response = self.generate_response(user_text)
        self.chat_display.insert(tk.END, "Bot: " + response + "\n")

    def generate_response(self, user_text):
        responses = {
            "hello": "Hi there! How can I help?",
            "how are you": "I'm just a bot, but I'm functioning well!",
            "bye": "Goodbye! Have a great day!"
        }
        return responses.get(user_text.lower(), "I don't understand.")

root = tk.Tk()
chatbot = ChatBot(root)
root.mainloop()