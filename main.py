import tkinter
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("500x500")
app.title("YouTube Downloader")

# running the app
app.mainloop()