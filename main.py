from keyboard import send
from src.CaptureScreen import getText
from src.llm import sendMessage
from src.tts import speakText
import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LLM Screen Assistant")
        self.root.geometry("500x350")
        self.root.minsize(500, 350)
        self.root.resizable(False, False)

        self.response_label = ttk.Label(root, text="Response:", font=("Arial", 10, "bold"))
        self.response_label.pack(anchor="w", padx=10, pady=(10, 0))

        self.response_text = tk.Text(root, height=10, wrap="word", state="disabled")
        self.response_text.pack(fill="both", expand=True, padx=10, pady=5)

        self.input_label = ttk.Label(root, text="Input:", font=("Arial", 10, "bold"))
        self.input_label.pack(anchor="w", padx=10, pady=(10, 0))

        self.input_entry = ttk.Entry(root)
        self.input_entry.pack(fill="x", padx=10, pady=5)
        self.input_entry.bind("<Return>", self.send_message)

        self.send_button = ttk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

    def send_message(self, event=None):
        user_input = self.input_entry.get().strip()
        AIResponse = sendMessage(user_input, getText())
        if not user_input:
            return
        
        response = AIResponse
        
        self.update_response(response)
        speakText(AIResponse)


    def update_response(self, text):
        self.response_text.config(state="normal")
        self.response_text.delete("1.0", tk.END)
        self.response_text.insert(tk.END, text)
        self.response_text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-alpha", 0.6)
    app = SimpleGUI(root)
    root.mainloop()


