from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *
import tkinter as tk


# function for exiting program
def exit_prgm(app):

    exit_msg = tk.messagebox.askyesno(title="Exiting Program",
                                      message="Are you sure, you want to exit fro this program?")
    # Exits a program when "Yes" is pressed
    if exit_msg == 1:
        app.destroy()
    else:
        app.mainloop()


# Function for browsing a directory to save a video 
def browse(download_path):

    download_directory = filedialog.askdirectory(initialdir="Path")

    download_path.set(download_directory)


# Function for downloading video from Youtube link
def download(vid_link, download_path):

    youtube_link = vid_link.get()

    download_folder = download_path.get()

    getvideo = YouTube(youtube_link)

    videostream = getvideo.streams.first()

    videostream.download(download_folder)

    messagebox.showinfo(title="Download Successfully", message="Your downloaded video is in\n" + download_folder)


# Entry point of the program
def main():

    app = tk.Tk()

    app.geometry("600x120")

    app.configure(background="Gray")

    app.resizable(False, False)

    app.title("Youtube Downloader")

    vid_link = StringVar()

    download_path = StringVar()
    
    # Set up a menubar for Exit a program
    menubar = Menu(app)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=lambda: exit_prgm(app))
    menubar.add_cascade(label="File", menu=filemenu)
    app.config(menu=menubar)
    
    # Set up a label and entry box for youtube link
    link_label = Label(app, text="YouTube link  :", background="Gray", font='Arial 12')
    link_label.grid(row=1, column=0, pady=5, padx=5)
    linktxt = tk.Entry(app, width=55, textvariable=vid_link)
    linktxt.grid(row=1, column=1, pady=5, padx=5, columnspan=2)
    
    # Set up a label and entry box for directory destination
    destination = Label(app, text="Destination    :", background="Gray", font='Arial 12')
    destination.grid(row=2, column=0, pady=5, padx=5)
    destination_txt = tk.Entry(app, width=40, textvariable=download_path)
    destination_txt.grid(row=2, column=1, pady=5, padx=5)
    
    # Set up a buttons for Browsing a file for download directory and to download youtube video 
    browse_btn = tk.Button(app, text="Browse", command=lambda: browse(download_path), width=10, background="Gray")
    browse_btn.grid(row=2, column=2, pady=1, padx=1)
    download_btn = tk.Button(app, text="Download", command=lambda: download(vid_link, download_path),
                             width=20, background="Gray")
    download_btn.grid(row=3, column=1, pady=3, padx=3)
    
    # Display an app in a loop 
    app.mainloop()


# The following if statement helps Python determine whether or not the main()
# function in this program is our entry point.
if __name__ == "__main__":
    main()
