import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import PytubeError
from screeninfo import get_monitors

# download function
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        ytVideo = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishedLabel.configure(text="")
        ytVideo.download()
    except PytubeError as e:
        finishedLabel.configure(text=f"An error occurred while downloading the video: {e}", text_color="red")
    else:
        finishedLabel.configure(text="YouTube video downloaded successfully!")

# progress function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progressPercentage.configure(text=per + "%")
    progressPercentage.update()
    progressBar.set(float(percentage_of_completion) / 100 )

# settings and customizations
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# creating the app
monitor = get_monitors()[0]
center_x = monitor.width // 2
center_y = monitor.height // 2
window_width = 400
window_height = 250
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

# finished downloading
finishedLabel = customtkinter.CTkLabel(app, text="")
finishedLabel.pack()

# progress percentage
progressPercentage = customtkinter.CTkLabel(app, text="0%")
progressPercentage.pack()

# progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack()

# running the app
app.mainloop()