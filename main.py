import tkinter
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("500x500")
app.title("YouTube Downloader")

# UI things
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=12, pady=12)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=30, textvariable=url_var)
link.pack()

# download button
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        ytVideo = ytObject.streams.get_highest_resolution()
        ytVideo.download()
    except:
        print("Something is wrong with the YouTube link")
    print("YouTube video downloaded successfully!")
        
        
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# running the app
app.mainloop()