import customtkinter as ctk
import threading

import modules.bot as BotSystem
ChatBot = BotSystem.ChatBot()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ChatUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("DeskBot")
        self.geometry("600x420")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Output box
        self.output = ctk.CTkTextbox(self, wrap="word", corner_radius=8)
        self.output.grid(row=0, column=0, padx=12, pady=(12, 6), sticky="nsew")
        self.output.configure(state="disabled")

        # input + send button
        bottom_frame = ctk.CTkFrame(self, corner_radius=8)
        bottom_frame.grid(row=1, column=0, padx=12, pady=(6, 12), sticky="ew")
        bottom_frame.grid_columnconfigure(0, weight=1)

        # input box
        self.entry = ctk.CTkEntry(bottom_frame, placeholder_text="Type a message...")
        self.entry.grid(row=0, column=0, padx=(8, 6), pady=8, sticky="ew")
        self.entry.bind("<Return>", self._on_enter)

        # Send button
        self.send_btn = ctk.CTkButton(bottom_frame, text="Send", width=90, command=self.send_message)
        self.send_btn.grid(row=0, column=1, padx=(6, 8), pady=8)

    def _append_output(self, text: str):
        self.output.configure(state="normal")
        if self.output.get("1.0", "end-1c"):
            self.output.insert("end", "\n")
        self.output.insert("end", text)
        self.output.see("end")
        self.output.configure(state="disabled")
    
    def delete_last_line(self):
        self.output.configure(state="normal")
        content = self.output.get("1.0", "end-1c")
        if not content:
            self.output.configure(state="disabled")
            return
        
        last_line = int(self.output.index("end-1c").split('.')[0])
        start_index = f"{last_line}.0"
        self.output.delete(start_index, "end")
        self.output.configure(state="disabled")
    
    def _set_ui_enabled(self, enabled: bool):
        state = "normal" if enabled else "disabled"
        self.entry.configure(state=state)
        self.send_btn.configure(state=state)

    def send_message(self):
        msg = self.entry.get().strip()
        if not msg:
            return

        self._append_output(f"You: {msg}\n")
        self.entry.delete(0, "end")

        self._set_ui_enabled(False)

        self._append_output("Bot is currently thinking...")

        def do_response():
            try:
                resp = ChatBot.get_response(msg)
                if not isinstance(resp, str):
                    resp = "".join(str(chunk) for chunk in resp if chunk is not None)
            except Exception as e:
                resp = f"I ran into an error: {e}"

            self.after(0, lambda: self._on_bot_done(resp))

        threading.Thread(target=do_response, daemon=True).start()
    
    def _on_bot_done(self, response: str):
        self._set_ui_enabled(True)
        self.delete_last_line()
        self._append_output(f"Bot: {response}\n")

    def _on_enter(self, event):
        self.send_message()

if __name__ == "__main__":
    app = ChatUI()
    app._append_output(f"Welcome to Chatter! Type /help for commands.\n")
    app.mainloop()