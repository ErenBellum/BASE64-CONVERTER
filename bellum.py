try:
    import customtkinter as ctk
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter"])
    import customtkinter as ctk

import base64
import tkinter.filedialog as fd
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Base64App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Erenbellum - Base64 Converter")
        self.geometry("700x600")
        self.configure(bg="black")

        self.label = ctk.CTkLabel(self, text="Metni girin veya dosya seçin", font=("Consolas", 16), text_color="cyan")
        self.label.pack(pady=10)

        self.textbox = ctk.CTkTextbox(self, width=600, height=200, font=("Consolas", 14))
        self.textbox.pack(pady=10)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10)

        self.encode_button = ctk.CTkButton(self.frame, text="Metni Base64'e Dönüştür", command=self.encode_text)
        self.encode_button.grid(row=0, column=0, padx=10)

        self.decode_button = ctk.CTkButton(self.frame, text="Base64'ten Metne Çevir", command=self.decode_text)
        self.decode_button.grid(row=0, column=1, padx=10)

        self.load_file_button = ctk.CTkButton(self, text="Dosyadan Yükle", command=self.load_file)
        self.load_file_button.pack(pady=10)

        self.output_label = ctk.CTkLabel(self, text="Sonuç:", font=("Consolas", 16), text_color="cyan")
        self.output_label.pack()

        self.output_box = ctk.CTkTextbox(self, width=600, height=220, font=("Consolas", 14))
        self.output_box.pack(pady=10)

    def encode_text(self):
        text = self.textbox.get("1.0", "end").strip()
        try:
            encoded = base64.b64encode(text.encode()).decode()
            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", encoded)
        except Exception as e:
            self.output_box.insert("1.0", f"Hata: {str(e)}")

    def decode_text(self):
        text = self.textbox.get("1.0", "end").strip()
        try:
            decoded = base64.b64decode(text).decode()
            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", decoded)
        except Exception as e:
            self.output_box.insert("1.0", f"Hata: {str(e)}")

    def load_file(self):
        file_path = fd.askopenfilename(filetypes=[("Metin Dosyaları", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                self.textbox.delete("1.0", "end")
                self.textbox.insert("1.0", content)

if __name__ == "__main__":
    app = Base64App()
    app.mainloop()
