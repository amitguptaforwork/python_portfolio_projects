import tkinter as tk
from response import generate_response  # Import the function from response.py

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")

        self.chat_display = tk.Text(root, bg="white", height=15, width=50)
        self.chat_display.pack()

        self.user_input = tk.Entry(root, bg="lightgray", width=40)
        self.user_input.pack()
        self.user_input.bind("<Return>", self.respond)  # Bind Enter key to se

        self.send_button = tk.Button(root, text="Send", command=self.respond)
        self.send_button.pack()

    def respond(self, event=None):
        user_text = self.user_input.get()
        if user_text.strip():  # Prevent sending empty messages
            self.chat_display.insert(tk.END, "You: " + user_text + "\n")
            self.user_input.delete(0, tk.END)

            response = generate_response(user_text)
            self.chat_display.insert(tk.END, "Bot: " + response + "\n")



root = tk.Tk()
chatbot = ChatBot(root)
root.mainloop()