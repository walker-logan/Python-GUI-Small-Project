import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import PytubeError
from screeninfo import get_monitors

# settings and customizations
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# creating the app
monitor = get_monitors()[0]
center_x = monitor.width // 2
center_y = monitor.height // 2
window_width = 400
window_height = 200
position_x = center_x - window_width // 2
position_y = center_y - window_height // 2

app = customtkinter.CTk()
app.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
app.title("YouTube Downloader")

# UI things
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=12, pady=12)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=30, textvariable=url_var)
link.pack(padx=10, pady=10)

# download button
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        ytVideo = ytObject.streams.get_highest_resolution()
        ytVideo.download()
    except PytubeError as e:
        print(f"An error occurred while downloading the video: {e}")
    else:
        print("YouTube video downloaded successfully!")
        
        
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# running the app
app.mainloop()