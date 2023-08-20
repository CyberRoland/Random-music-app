from customtkinter import *
from tkinter import *
from PIL import Image,ImageTk
import os
from pygame import mixer

Spotify = CTk()
Spotify.title('MeloMind')
Spotify.geometry('800x400')


def stretch_image(event):
    global Top_img


    width = event.width
    height = event.height




    # Create an Image
    resized_image = top_original.resize((width,height))
    Top_img = ImageTk.PhotoImage(resized_image)


    # Place on canvas


    canvas.create_image(0,0, image = Top_img, anchor = 'nw')

def show_slider():
    global Volume_slide_shown

    if Volume_slide_shown:
        Volume_Slider.place_forget()
        Volume_slide_shown = False
    else:
        Volume_Slider.place(relx = 0.94, rely = .34, relheight = .5, anchor = 'n')
        Volume_slide_shown = True

def pause_song():
    if mixer.music.get_busy() == True:
        mixer.music.pause()
        pause.configure(text="▶")
    else:
        mixer.music.unpause()
        pause.configure(text="⏸")

def change_volume(event):
    print(Volume_Slider.get())
    mixer.music.set_volume(Volume_Slider.get()/100)

def update_song(*args):
    selected_song = Entrysong.get()
    selected_song_without_extension = selected_song.replace(".mp3", "")
    song_name.config(text=selected_song_without_extension)

    mixer.music.load(os.path.join(f"songs/{selected_song_without_extension}.mp3"))
    mixer.music.play(-1)

def restart(*args):
    selected_song = Entrysong.get()
    selected_song_without_extension = selected_song.replace(".mp3", "")

    mixer.music.load(os.path.join(f"Python\Projects\songs\{selected_song_without_extension}.mp3"))
    mixer.music.play(-1)




    
Entrysong = StringVar(value='Pick a Song')

# BackGround image

top_original = Image.open('Python\Projects\Extra stuff\Top.png')
Top_img = ImageTk.PhotoImage(top_original)


canvas = Canvas(Spotify, bg = 'green', border=0, bd=0, borderwidth=0)
canvas.place(x=0,y=0,relheight=1,relwidth=1)
canvas.bind('<Configure>',stretch_image)



# Progress bar
Volume_Slider = CTkSlider(Spotify,
                         bg_color='#0a0c30',
                         fg_color='white',
                         border_color='#0a0c30',
                         border_width=6,
                         corner_radius=0,
                         from_=0,
                         to=100,
                         progress_color='blue',
                         button_color='blue',
                         button_hover_color='Blue',
                         orientation=VERTICAL,
                         command=change_volume)
Volume_Slider.set(0)

# Song Files
with open("Python\Projects\Extra stuff\songs.txt", "r") as file:
    songs = file.read().splitlines()

songs = [song.replace(".mp3", "") for song in songs]


# Song name

song_name = Label(Spotify,text='Pick a Song', bg='black',fg='blue',activebackground='green',activeforeground='green',font=("Power Clear",50))
song_name.place(relx=0.5,rely=0.45,anchor='center')

# Pause
pause = CTkButton(Spotify, text='⏸', fg_color='White', text_color='Blue', command=pause_song)
pause.place(relx=.056,rely=.913, relwidth = 0.08, relheight = 0.08, anchor='center')

# Volume Button
volume_button = CTkButton(Spotify, text="🔈", font=('Arial', 25), fg_color='white',text_color='blue', corner_radius=100, command=show_slider)
volume_button.place(relx=.94,rely=.913, relwidth = 0.08, relheight = 0.08, anchor='center')

#  Songs
song_list = CTkComboBox(Spotify,
                         values=songs,
                          variable=Entrysong,
                          fg_color='white',
                         text_color='blue',
                          dropdown_fg_color='white',
                          dropdown_text_color='blue',
                          dropdown_hover_color='Black',
                          justify='center',
                         command=update_song)
song_list.place(relx = 0.5, rely = .914,relwidth = 0.7 ,anchor = 'center')

# Restart Button

restart = CTkButton(Spotify, text="🔄", font=('Arial', 25), fg_color='white',text_color='blue', corner_radius=100, command=restart)
restart.place(relx=.056,rely=.08, relwidth = 0.08, relheight = 0.08, anchor='center')

# Varibles
Volume_slide_shown = False
paused = False

# Song List
song_list['values'] = songs



# Initalize mixer

mixer.init()

# Volume Defualt
mixer.music.set_volume(1000)

Spotify.mainloop()


 