import tkinter as tk
import os
import sys
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

assets_path = os.path.join(BASE_DIR,"assets")
backgrounds_path = os.path.join(BASE_DIR, "assets", "backgrounds")
bg_path = os.path.join(BASE_DIR, "assets", "backgrounds", "bg.png")
fonts_path = os.path.join(BASE_DIR, "assets", "fonts")
icons_path = os.path.join(BASE_DIR, "assets", "icons")
icon_path = os.path.join(BASE_DIR, "assets", "icons", "icon.png")
note_icon_path = os.path.join(BASE_DIR, "assets", "icons", "note_icon.png")
readme_path = os.path.join(BASE_DIR, "assets","README.txt")

for path in [assets_path,fonts_path, icons_path, icon_path, note_icon_path, readme_path]:
    if not os.path.exists(path):
        print(f"Advertencia: La carpeta {path} no existe.")

def show_page(frame):
    frame.tkraise()


########## Main Menu ##########


root = tk.Tk()
root.title("Your Note: App de notas")
root.geometry("640x340")
root.resizable(0, 0)
root.configure(bg="lightgrey")

container = tk.Frame(root)
container.pack(fill="both", expand=True)

page1 = tk.Frame(container, bg="lightgrey")
page2 = tk.Frame(container, bg="lightgrey")

for frame in (page1, page2):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

show_page(page1)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icons_folder_path = resource_path("assets/icons")
backgrounds_folder_path = resource_path("assets/backgrounds")
bg_path = resource_path("assets/backgrounds/bg.png")
icon_path = resource_path("assets/icons/icon.png")
note_icon_path = resource_path("assets/icons/note_icon.png")
font_path = resource_path("assets/fonts/tahoma.ttf")
font_bold_path = resource_path("assets/fonts/tahomabd.ttf")

if os.path.exists(icon_path):
    try:
        icon = Image.open(icon_path)
        photo = ImageTk.PhotoImage(icon)
        root.iconphoto(False, photo)
    except Exception as e:
        print(f"Advertencia: No se pudo cargar el icono. Error: {e}")

icon = Image.open(icon_path)
photo = ImageTk.PhotoImage(icon)
root.iconphoto(False,photo)

img_bg = Image.open(bg_path).resize((580, 150))
tkimg_bg = ImageTk.PhotoImage(img_bg)
    
label_bg = tk.Label(page1, image=tkimg_bg, background="lightgrey")
label_bg.image = tkimg_bg  
label_bg.pack(pady=10)

title = tk.Label(page1, text="Añadir Actividades", font=(font_path, 15,"bold"), foreground="black", wraplength=355, justify="center", anchor="center", background="lightgrey")
title.pack(pady=5)
add_button = tk.Button(page1, text="Añadir", font=("assets/fonts/tahoma.ttf", 10), cursor="hand2",
                             relief="raised", bd=3, bg="#27548A", fg="white", command=lambda:show_page(page2))
add_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#183B4E"))
add_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#27548A"))
add_button.bind("<Enter>", lambda event: event.widget.config(bg="#183B4E")) 
add_button.bind("<Leave>", lambda event: event.widget.config(bg="#27548A"))
add_button.pack(pady=30)

credits = tk.Label(page1, text="2025 - @areimo on GitHub", font=(font_path, 8), foreground="grey", background="lightgrey")
credits.place(y=300, x=633, anchor="ne")


########## About ##########


def open_window():
    secondary_window = tk.Toplevel(root)
    secondary_window.title("Acerca de Your Note: App de notas")
    secondary_window.geometry("400x500")
    secondary_window.configure(bg="lightgrey")
    secondary_window.resizable(0, 0)
    secondary_window.iconphoto(False, photo)

    img_icon = Image.open(note_icon_path).resize((200, 200))
    tkimg_icon = ImageTk.PhotoImage(img_icon)
    
    label_img = tk.Label(secondary_window, image=tkimg_icon, background="lightgrey")
    label_img.image = tkimg_icon  
    label_img.pack(pady=10)
    label_text = tk.Label(secondary_window, text="Your Note: App de notas", font=(font_bold_path, 13), foreground="black", background="lightgrey")
    label_text.pack(pady=5)
    label_text2 = tk.Label(secondary_window, text="Versión 1.0", font=(font_path, 10), foreground="black", background="lightgrey")
    label_text2.pack(pady=8)
    label_text4 = tk.Label(secondary_window, text="Your Note es una herramienta la cual permite crear una lista de actividades y exportarla como una imagen PNG", font=(font_path, 10), foreground="black", wraplength=355, justify="center", anchor="center", background="lightgrey")
    label_text4.pack(pady=11)

    close_button = tk.Button(secondary_window, text="Cerrar", font=("assets/fonts/tahoma.ttf", 10), cursor="hand2",
                             relief="raised", bd=3, bg="#27548A", fg="white", command=secondary_window.destroy)
    close_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#183B4E"))
    close_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#27548A"))
    close_button.bind("<Enter>", lambda event: event.widget.config(bg="#183B4E")) 
    close_button.bind("<Leave>", lambda event: event.widget.config(bg="#27548A"))
    close_button.pack(pady=40)

    credits = tk.Label(secondary_window, text="2025 - @areimo on GitHub", font=(font_path, 8), foreground="grey", background="lightgrey")
    credits.pack(pady=10)

    if os.path.exists(icon_path):
     try:
        icon = Image.open(icon_path)
        photo = ImageTk.PhotoImage(icon)
        root.iconphoto(False, photo)
     except Exception as e:
        print(f"Advertencia: No se pudo cargar el icono. Error: {e}")

menu_bar = tk.Menu(root, tearoff=0, bg="gray", fg="black", relief="raised")
menu_bar.add_command(label="Acerca de",command=open_window)
root.config(menu=menu_bar)


########## Page 2 ##########


back_button = tk.Button(page2, text="X", font=("assets/fonts/tahoma.ttf", 8, "bold"), cursor="hand2",
                        relief="raised", bd=3, bg="#27548A", fg="white", command=lambda: show_page(page1))
back_button.place(x=633, y=5, anchor="ne")

activity_label = tk.Label(page2, text="Actividad 1:", font=(font_path, 10, "bold"),
                          foreground="black", background="lightgrey")
activity_label.grid(row=0, column=0, padx=10, pady=(45,10))

activity_entry = tk.Entry(page2, font=(font_path, 10), width=70)
activity_entry.grid(row=0, column=1, padx=10, pady=(45,10))

activity_label2 = tk.Label(page2, text="Actividad 2:", font=(font_path, 10, "bold"),
                           foreground="black", background="lightgrey")
activity_label2.grid(row=1, column=0, padx=10, pady=10)

activity_entry2 = tk.Entry(page2, font=(font_path, 10), width=70)
activity_entry2.grid(row=1, column=1, padx=10, pady=10)

activity_label3 = tk.Label(page2, text="Actividad 3:", font=(font_path, 10, "bold"),
                           foreground="black", background="lightgrey")
activity_label3.grid(row=2, column=0, padx=10, pady=10)

activity_entry3 = tk.Entry(page2, font=(font_path, 10), width=70)
activity_entry3.grid(row=2, column=1, padx=10, pady=10)

activity_label4 = tk.Label(page2, text="Actividad 4:", font=(font_path, 10, "bold"),
                           foreground="black",  background="lightgrey")
activity_label4.grid(row=3, column=0, padx=10, pady=10)

activity_entry4 = tk.Entry(page2, font=(font_path, 10), width=70)
activity_entry4.grid(row=3, column=1, padx=10, pady=10)

activity_label5 = tk.Label(page2, text="Actividad 5:", font=(font_path, 10, "bold"),
                           foreground="black", background="lightgrey")
activity_label5.grid(row=4, column=0, padx=10, pady=10)

activity_entry5 = tk.Entry(page2, font=(font_path, 10), width=70)
activity_entry5.grid(row=4, column=1, padx=10, pady=10)

create_button = tk.Button(page2, text="Crear Nota", font=("assets/fonts/tahoma.ttf", 10), cursor="hand2",
                             relief="raised", bd=3, bg="#27548A", fg="white")
create_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#183B4E"))
create_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#27548A"))
create_button.bind("<Enter>", lambda event: event.widget.config(bg="#183B4E")) 
create_button.bind("<Leave>", lambda event: event.widget.config(bg="#27548A"))
create_button.place(y=280 , x=320, anchor="center")

credits = tk.Label(page2, text="2025 - @areimo on GitHub", font=(font_path, 8), foreground="grey", background="lightgrey")
credits.place(y=300, x=633, anchor="ne")

root.mainloop()
