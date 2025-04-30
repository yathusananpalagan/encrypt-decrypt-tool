import customtkinter as ctk
import tkinter as tk
from datetime import datetime
import os
import csv

ctk.set_appearance_mode("system")  # System appearance (dark/light)
ctk.set_default_color_theme("blue")

# Utility functions 
def shift_char(c, shift, encrypt=True):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        direction = 1 if encrypt else -1
        return chr((ord(c) - base + direction * shift) % 26 + base)
    return c

def get_shifts_from_text(text):
    return [(ord(c.lower()) - ord('a') + 1) for c in text if c.isalpha()]

def apply_shift(message, shifts, encrypt=True):
    result = []
    shift_len = len(shifts)
    for i, c in enumerate(message):
        shift = shifts[i % shift_len]
        result.append(shift_char(c, shift, encrypt))
    return ''.join(result)

# Main App
class EncryptApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Encrypt & Decrypt App")
        self.geometry("900x600")
        self.resizable(False, False)

        self.history = []

        self.font_style = ("Roboto", 16)  # Increased font size for text elements

        self.tabview = ctk.CTkTabview(self, width=800, height=500)  # Larger tab view area with adjusted width
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)  # Adjusted padding for more space

        self.encrypt_tab = self.tabview.add("Encrypt")
        self.decrypt_tab = self.tabview.add("Decrypt")
        self.history_tab = self.tabview.add("History")

        self.build_encrypt_tab()
        self.build_decrypt_tab()
        self.build_history_tab()

    def build_encrypt_tab(self):
        # Toggle button for light/dark mode in this tab
        toggle_button = ctk.CTkButton(self.encrypt_tab, text="Toggle Light/Dark Mode", command=self.toggle_mode)
        toggle_button.pack(pady=10)
        toggle_button.configure(font=self.font_style)

        self.message_entry_e = ctk.CTkEntry(self.encrypt_tab, placeholder_text="Enter message", width=450, height=45)
        self.message_entry_e.pack(pady=20)
        self.message_entry_e.configure(font=self.font_style)

        self.shift_entry_e = ctk.CTkEntry(self.encrypt_tab, placeholder_text="Enter shift (number or text)", width=450, height=45)
        self.shift_entry_e.pack(pady=20)
        self.shift_entry_e.configure(font=self.font_style)

        # Larger Tooltip for shift entry field
        self.shift_tooltip_e = ctk.CTkLabel(self.encrypt_tab, text="Shift can be a number (e.g., 3) or text (e.g., abc).")
        self.shift_tooltip_e.pack(pady=15)
        self.shift_tooltip_e.configure(font=("Roboto", 16))

        self.result_box_e = ctk.CTkTextbox(self.encrypt_tab, height=120, width=450)
        self.result_box_e.pack(pady=20)
        self.result_box_e.configure(font=self.font_style)
        self.result_box_e.bind("<Key>", lambda e: "break")  # Block key presses

        # Button frame to hold Encrypt and Copy button side by side
        button_frame_e = ctk.CTkFrame(self.encrypt_tab)
        button_frame_e.pack(pady=15)

        # Encrypt button
        encrypt_button = ctk.CTkButton(button_frame_e, text="Encrypt", command=self.encrypt)
        encrypt_button.grid(row=0, column=0, padx=10)
        encrypt_button.configure(font=self.font_style)

        # Copy button next to Encrypt button
        self.copy_button_e = ctk.CTkButton(button_frame_e, text="Copy", command=lambda: self.copy_to_clipboard(self.result_box_e))
        self.copy_button_e.grid(row=0, column=1, padx=10)
        self.copy_button_e.configure(font=self.font_style)

        # Clipboard confirmation message (initially empty text)
        self.clipboard_msg_e = ctk.CTkLabel(self.encrypt_tab, text="", text_color="green")
        self.clipboard_msg_e.pack(pady=5)
        self.clipboard_msg_e.configure(font=("Roboto", 16))

    def build_decrypt_tab(self):
        # Toggle button for light/dark mode in this tab
        toggle_button = ctk.CTkButton(self.decrypt_tab, text="Toggle Light/Dark Mode", command=self.toggle_mode)
        toggle_button.pack(pady=10)
        toggle_button.configure(font=self.font_style)

        self.message_entry_d = ctk.CTkEntry(self.decrypt_tab, placeholder_text="Enter encrypted message", width=450, height=45)
        self.message_entry_d.pack(pady=20)
        self.message_entry_d.configure(font=self.font_style)

        self.shift_entry_d = ctk.CTkEntry(self.decrypt_tab, placeholder_text="Enter shift (number or text)", width=450, height=45)
        self.shift_entry_d.pack(pady=20)
        self.shift_entry_d.configure(font=self.font_style)

        # Larger Tooltip for shift entry field
        self.shift_tooltip_d = ctk.CTkLabel(self.decrypt_tab, text="Shift can be a number (e.g., 3) or text (e.g., abc).")
        self.shift_tooltip_d.pack(pady=15)
        self.shift_tooltip_d.configure(font=("Roboto", 16))

        self.result_box_d = ctk.CTkTextbox(self.decrypt_tab, height=120, width=450)
        self.result_box_d.pack(pady=20)
        self.result_box_d.configure(font=self.font_style)
        self.result_box_d.bind("<Key>", lambda e: "break")  # Block key presses

        # Button frame to hold Decrypt and Copy button side by side
        button_frame_d = ctk.CTkFrame(self.decrypt_tab)
        button_frame_d.pack(pady=15)

        # Decrypt button
        decrypt_button = ctk.CTkButton(button_frame_d, text="Decrypt", command=self.decrypt)
        decrypt_button.grid(row=0, column=0, padx=10)
        decrypt_button.configure(font=self.font_style)

        # Copy button next to Decrypt button
        self.copy_button_d = ctk.CTkButton(button_frame_d, text="Copy", command=lambda: self.copy_to_clipboard(self.result_box_d))
        self.copy_button_d.grid(row=0, column=1, padx=10)
        self.copy_button_d.configure(font=self.font_style)

        # Clipboard confirmation message (initially empty text)
        self.clipboard_msg_d = ctk.CTkLabel(self.decrypt_tab, text="", text_color="green")
        self.clipboard_msg_d.pack(pady=5)
        self.clipboard_msg_d.configure(font=("Roboto", 16))

    def build_history_tab(self):
        # Title
        title = ctk.CTkLabel(self.history_tab, text="📜 Encryption & Decryption History", font=("Roboto", 20, "bold"))
        title.pack(pady=(20, 10))

        # Toggle button for light/dark mode in this tab
        toggle_button = ctk.CTkButton(self.history_tab, text="Toggle Light/Dark Mode", command=self.toggle_mode)
        toggle_button.pack(pady=10)
        toggle_button.configure(font=self.font_style)

        # Search Entry
        self.search_entry = ctk.CTkEntry(self.history_tab, placeholder_text="Search history...", width=400, height=40)
        self.search_entry.pack(pady=(10, 20))
        self.search_entry.configure(font=self.font_style)
        self.search_entry.bind("<KeyRelease>", self.update_history_display)

        # Clear Button
        clear_btn = ctk.CTkButton(self.history_tab, text="🧹 Clear History", font=("Roboto", 14),
                                command=self.clear_history, fg_color="#FF5C5C", hover_color="#CC4A4A")
        clear_btn.pack(pady=(0, 10))

        # Save Button
        save_btn = ctk.CTkButton(self.history_tab, text="💾 Save History", font=("Roboto", 14),
                         command=self.save_history_to_file, fg_color="#5CADFF", hover_color="#4696DB")
        save_btn.pack(pady=(0, 10))     

        # Container Frame
        self.history_container = ctk.CTkFrame(self.history_tab, fg_color="transparent")
        self.history_container.pack(expand=True, fill="both", padx=20)

        # Scrollable Frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self.history_container, width=850, height=450)
        self.scrollable_frame.pack(pady=10, anchor="center")

        # Table Headers
        headers = ["Action", "Original", "Result", "Timestamp"]
        for col, header in enumerate(headers):
            label = ctk.CTkLabel(self.scrollable_frame, text=header, font=("Roboto", 18, "bold"))
            label.grid(row=0, column=col, padx=50, pady=10, sticky="w")

    def update_history_display(self, event=None ):
        # Get the search term
        search_term = self.search_entry.get().lower()

        # Clear existing entries (except header row)
        for widget in self.scrollable_frame.winfo_children():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()

        # Show most recent entries at top
        history_reversed = list(reversed(self.history))

        # Filter history based on search term
        filtered_history = [
            entry for entry in history_reversed
            if any(search_term in field.lower() for field in entry)
        ]

        for row, (action, original, result, timestamp) in enumerate(filtered_history, start=1):
            # Color-coded action
            color = "green" if action == "Encrypt" else "orange"

            # Truncate long texts
            original_display = original[:40] + "..." if len(original) > 40 else original
            result_display = result[:40] + "..." if len(result) > 40 else result

            ctk.CTkLabel(self.scrollable_frame, text=action, text_color=color, font=("Roboto", 14)).grid(row=row, column=0, padx=50, pady=5, sticky="w")
            ctk.CTkLabel(self.scrollable_frame, text=original_display, font=("Roboto", 14)).grid(row=row, column=1, padx=50, pady=5, sticky="w")
            ctk.CTkLabel(self.scrollable_frame, text=result_display, font=("Roboto", 14)).grid(row=row, column=2, padx=50, pady=5, sticky="w")
            ctk.CTkLabel(self.scrollable_frame, text=timestamp, font=("Roboto", 14)).grid(row=row, column=3, padx=50, pady=5, sticky="w")

    def clear_history(self):
        self.history.clear()
        self.update_history_display()

    def save_history_to_file(self):
        # Get the absolute path of the directory where this script is located
        base_dir = os.path.dirname(os.path.abspath(__file__))
        out_dir = os.path.join(base_dir, "out")

        # Ensure the 'out' directory exists
        os.makedirs(out_dir, exist_ok=True)
        file_path = os.path.join(out_dir, "history.txt")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"{'Action'.ljust(12)} | {'Original'.ljust(40)} | {'Result'.ljust(40)} | Timestamp\n")
            f.write("-" * 120 + "\n")
            for action, orig, res, ts in self.history:
                f.write(f"{action.ljust(12)} | {orig.ljust(40)} | {res.ljust(40)} | {ts}\n")
        self.export_history_to_csv()  # Export to CSV

    def export_history_to_csv(self):
        # Ensure 'out' directory exists
        base_dir = os.path.dirname(os.path.abspath(__file__))
        out_dir = os.path.join(base_dir, "out")
        os.makedirs(out_dir, exist_ok=True)

        # Path for the CSV file
        file_path_csv = os.path.join(out_dir, "history.csv")

        # Write history to CSV file
        with open(file_path_csv, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Action", "Original", "Result", "Timestamp"])  # Write header
            for action, original, result, timestamp in self.history:
                writer.writerow([action, original, result, timestamp])

    def encrypt(self):
        msg = self.message_entry_e.get().strip()
        shift_raw = self.shift_entry_e.get().strip()

        self.result_box_e.delete("1.0", tk.END)

        if not msg:
            self.result_box_e.insert(tk.END, "❌ Please enter a message.")
            return

        try:
            shift = self.parse_shift_input(shift_raw)
        except ValueError as e:
            self.result_box_e.insert(tk.END, f"❌ {e}")
            return

        encrypted = apply_shift(msg, shift, encrypt=True)
        self.result_box_e.insert(tk.END, encrypted)
        self.add_to_history("Encrypt", msg, encrypted)

    def decrypt(self):
        msg = self.message_entry_d.get().strip()
        shift_raw = self.shift_entry_d.get().strip()

        # Ensure result_box_d is defined and packed before performing operations on it
        if hasattr(self, 'result_box_d') and self.result_box_d.winfo_ismapped():
            self.result_box_d.delete("1.0", tk.END)
        else:
            print("Error: result_box_d widget not properly initialized.")
            return

        if not msg:
            self.result_box_d.insert(tk.END, "❌ Please enter a message.")
            return

        try:
            shift = self.parse_shift_input(shift_raw)
        except ValueError as e:
            self.result_box_d.insert(tk.END, f"❌ {e}")
            return

        decrypted = apply_shift(msg, shift, encrypt=False)
        self.result_box_d.insert(tk.END, decrypted)
        self.add_to_history("Decrypt", msg, decrypted)

    def parse_shift_input(self, shift_raw):
        if not shift_raw:
            raise ValueError("Shift input is empty.")

        if shift_raw.isdigit() or (shift_raw.startswith("-") and shift_raw[1:].isdigit()):
            return [int(shift_raw)]

        if shift_raw.isalpha():
            return get_shifts_from_text(shift_raw)

        raise ValueError("Invalid shift input. Use a number or only letters.")

    def copy_to_clipboard(self, textbox):
        text = textbox.get("1.0", tk.END).strip()
        self.clipboard_clear()
        self.clipboard_append(text)

        # Show confirmation message
        confirmation_label = self.clipboard_msg_e if textbox == self.result_box_e else self.clipboard_msg_d
        confirmation_label.configure(text="Copied to clipboard!", text_color="green")
        
        # Hide confirmation message after 2 seconds
        self.after(2000, lambda: confirmation_label.configure(text=""))
    
    def toggle_mode(self):
        # Check the current appearance mode and toggle it
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "dark"
        ctk.set_appearance_mode(new_mode)  # Toggle mode

    def add_to_history(self, action_type, original, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Clean strings to avoid newline/tab issues
        clean_original = original.replace('\n', ' ').replace('\t', ' ').strip()
        clean_result = result.replace('\n', ' ').replace('\t', ' ').strip()
        
        self.history.append((action_type, clean_original, clean_result, timestamp))
        self.update_history_display()
        self.save_history_to_file()

if __name__ == "__main__":
    app = EncryptApp()
    app.mainloop()