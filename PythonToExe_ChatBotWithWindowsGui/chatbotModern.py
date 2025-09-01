import tkinter as tk
from tkinter import ttk
from response import generate_response  # Import the function from response.py
from PIL import Image, ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("400x500")

        # Load and set the background image
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((400, 500))  # Initial size
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Auto-resizing background

        # Frame for Label & Dropdown in the same row
        model_frame = tk.Frame(root, bg=root.cget("bg"))  # Transparent background
        model_frame.pack(pady=10, padx=10, fill="x")

        # Model Selection Label
        tk.Label(model_frame, text="Select Model:", font=("Arial", 12), bg=model_frame.cget("bg")).grid(row=0, column=0, padx=5)

        # Model Selection Dropdown
        self.model_list = ["openai/gpt-4o", "gemini/gemini-2.5-flash"]  # Replace with actual models
        self.model_dropdown = ttk.Combobox(model_frame, values=self.model_list, font=("Arial", 12), width=20)
        self.model_dropdown.grid(row=0, column=1, padx=5)

        self.model_dropdown.current(0)  # Default selection

         # Frame for API Key Label & Entry
        api_frame = tk.Frame(root, bg=root.cget("bg"))
        api_frame.pack(pady=10, padx=10, fill="x")

        # API Key Label
        tk.Label(api_frame, text="API Key:", font=("Arial", 12), bg=api_frame.cget("bg")).grid(row=0, column=0, padx=5)

        # API Key Entry Field
        self.api_key_entry = ttk.Entry(api_frame, font=("Arial", 12), width=30)
        self.api_key_entry.grid(row=0, column=1, padx=5)



        # Chat display area
        self.chat_display = tk.Text(root, bg="light grey", font=("Arial", 12), height=15, width=50)
        self.chat_display.pack(fill="both", expand=True) #text area and background dynamically resize


        # User input field
        self.user_input = tk.Entry(root, font=("Arial", 12))
        self.user_input.pack(padx=10, pady=5, fill="x")
        self.user_input.bind("<Return>", self.respond)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.respond, font=("Arial", 12))
        self.send_button.pack(padx=10, pady=5)

    def respond(self, event=None):
        user_text = self.user_input.get()
        if user_text.strip():
            self.chat_display.insert(tk.END, "You: " + user_text + "\n")
            self.user_input.delete(0, tk.END)

            response = generate_response(user_text, self.model_dropdown.get(), self.api_key_entry.get())
            self.chat_display.insert(tk.END, "Bot: " + response + "\n")

    

root = tk.Tk()
chatbot = ChatBot(root)
root.mainloop()