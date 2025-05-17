import tkinter as tk
import tkinter.messagebox as messagebox
import os
import sys
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

assets_path = os.path.join(BASE_DIR,"assets")
backgrounds_path = os.path.join(BASE_DIR, "assets", "backgrounds")
bg_path = os.path.join(BASE_DIR, "assets", "backgrounds", "bg.png")
fonts_path = os.path.join(BASE_DIR, "assets", "fonts")
icons_path = os.path.join(BASE_DIR, "assets", "icons")
icon_path = os.path.join(BASE_DIR, "assets", "icons", "icon.ico")
note_icon_path = os.path.join(BASE_DIR, "assets", "icons", "note_icon.png")
note_img_path = os.path.join(BASE_DIR,"assets", "note.png")
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
icon_path = resource_path("assets/icons/icon.ico")
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

credits = tk.Label(page1, text="2025 - @areimo on GitHub", font=(font_path, 6), foreground="grey", background="lightgrey")
credits.place(y=305, x=633, anchor="ne")


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

    label_text = tk.Label(secondary_window,text="Your Note: App de notas",font=(font_bold_path, 13),
        foreground="black",background="lightgrey")
    label_text.pack(pady=5)

    label_text2 = tk.Label(secondary_window,text="Versión 1.0",font=(font_path, 10),
        foreground="black",background="lightgrey")
    label_text2.pack(pady=8)

    label_text4 = tk.Label(secondary_window,text="Your Note es una herramienta la cual permite crear una lista de actividades y exportarla como una imagen PNG",font=(font_path, 10),
        foreground="black",wraplength=355,justify="center",anchor="center",background="lightgrey")
    label_text4.pack(pady=11)

    close_button = tk.Button(secondary_window,text="Cerrar",font=("assets/fonts/tahoma.ttf", 10),cursor="hand2",relief="raised",
        bd=3,bg="#27548A",fg="white",command=secondary_window.destroy)
    close_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#183B4E"))
    close_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#27548A"))
    close_button.bind("<Enter>", lambda event: event.widget.config(bg="#183B4E")) 
    close_button.bind("<Leave>", lambda event: event.widget.config(bg="#27548A"))
    close_button.pack(pady=40)

    credits = tk.Label(secondary_window,text="2025 - @areimo on GitHub",font=(font_path, 8),foreground="grey",background="lightgrey")
    credits.pack(pady=10)

menu_bar = tk.Menu(root, tearoff=0, bg="gray", fg="black", relief="raised")
menu_bar.add_command(label="Acerca de",command=open_window)
root.config(menu=menu_bar)


########## Page 2 ##########


note_path = resource_path("assets/note.png")

entries = []

back_button = tk.Button(page2, text="X", font=("assets/fonts/tahoma.ttf", 8, "bold"), cursor="hand2",
                        relief="raised", bd=3, bg="#27548A", fg="white", command=lambda: show_page(page1))
back_button.place(x=633, y=5, anchor="ne")

for i in range(5):
    label = tk.Label(page2, text=f"Actividad {i+1}:", font=(font_path, 10, "bold"),
                     foreground="black", background="lightgrey")
    label.grid(row=i, column=0, padx=10, pady=(45 if i == 0 else 10, 10))

    entry = tk.Entry(page2, font=(font_path, 10), width=70)
    entry.grid(row=i, column=1, padx=10, pady=(45 if i == 0 else 10, 10))

    entries.append(entry)

def export_note_in_img(nota_texto, imagen_fondo):

    img = Image.open(imagen_fondo).convert("RGBA")

    layer_text = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(layer_text)

    try:
        font = ImageFont.truetype("assets/fonts/tahoma.ttf", 32)
    except:
        font = ImageFont.load_default()

    max_width = img.width - 100  
    space_between = 50

    def split_lines(texto, fuente, ancho_maximo):
        words = texto.split()
        lines = []
        actual_line = ""

        for word in words:
            possible_line = f"{actual_line} {word}".strip()
            bbox = draw.textbbox((0, 0), possible_line, font=fuente)
            width = bbox[2] - bbox[0]
            if width <= ancho_maximo:
                actual_line = possible_line
            else:
                lines.append(actual_line)
                actual_line = word

        if actual_line:
            lines.append(actual_line)

        return lines

    final_lines = []

    for activity in nota_texto.split("\n"):
        final_lines.extend(split_lines(activity, font, max_width))

    total_height = len(final_lines) * space_between
    vertical_displacement = 50  
    inicial_y = (img.height - total_height) // 2 + vertical_displacement  

    y = inicial_y
    for line in final_lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        ancho_linea = bbox[2] - bbox[0]
        x = (img.width - ancho_linea) // 2
        draw.text((x, y), line, font=font, fill="#446FA7")
        y += space_between

    final_img = Image.alpha_composite(img, layer_text)

    saved_file = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Guardar nota"
    )

    if saved_file:
        final_img.convert("RGB").save(saved_file)
        print("Imagen guardada en:", saved_file)

def create_note():
    activities = [entry.get().strip() for entry in entries if entry.get().strip()]
    if not activities:
        messagebox.showwarning("Campos vacíos", "Ingresa al menos una actividad")
        return

    note = "\n".join([f"Actividad {i+1}: {act}" for i, act in enumerate(activities)])
    export_note_in_img(note, note_path)

create_button = tk.Button(page2, text="Crear Nota", font=("assets/fonts/tahoma.ttf", 10), cursor="hand2",
                          relief="raised", bd=3, bg="#27548A", fg="white", command=create_note)
create_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#183B4E"))
create_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#27548A"))
create_button.bind("<Enter>", lambda event: event.widget.config(bg="#183B4E"))
create_button.bind("<Leave>", lambda event: event.widget.config(bg="#27548A"))
create_button.place(y=290, x=320, anchor="center")

root.mainloop()