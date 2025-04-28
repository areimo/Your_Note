import tkinter as tk
import os
import sys
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

assets_path = os.path.join(BASE_DIR,"assets")
backgrounds_path = os.path.join(BASE_DIR, "assets", "backgrounds")
fonts_path = os.path.join(BASE_DIR, "assets", "fonts")
icons_path = os.path.join(BASE_DIR, "assets", "icons")
icon_path = os.path.join(BASE_DIR, "assets", "icons", "icon.png")
note_icon_path = os.path.join(BASE_DIR, "assets", "icons", "note_icon.png")
readme_path = os.path.join(BASE_DIR, "README.txt")

for path in [assets_path,fonts_path, icons_path, icon_path, note_icon_path, readme_path]:
    if not os.path.exists(path):
        print(f"Advertencia: La carpeta {path} no existe.")

root = tk.Tk()
root.title("Your Note: App de notas")
root.geometry("800x600")
root.resizable(0, 0)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icons_folder_path = resource_path("assets/icons")
icon_path = resource_path("assets/icons/icon.png")
note_icon_path = resource_path("assets/icons/note_icon.png")
font_path = resource_path("assets/fonts/tahoma.ttf")
font_bold_path = resource_path("assets/fonts/tahomabd.ttf")

if os.path.exists(icon_path):
    try:
        root.iconphoto(icon_path)  
    except Exception as e:
        print(f"Advertencia: No se pudo cargar el icono. Error: {e}")
else:
    print(f"Advertencia: No se encontró el icono en {icon_path}")

icon = Image.open(icon_path)
photo = ImageTk.PhotoImage(icon)
root.iconphoto(False,photo)

    title = tk.Label(secondary_window, text="Añadir Actividad", font=(font_path, 15,"bold"), foreground="black", wraplength=355, justify="center", anchor="center", background="white")
    label_text4.pack(pady=11)


########## About ##########


def open_window():
    secondary_window = tk.Toplevel(root)
    secondary_window.title("Acerca de Your Note: App de notas")
    secondary_window.geometry("400x500")
    secondary_window.configure(bg="white")
    secondary_window.resizable(0, 0)
    secondary_window.iconphoto(False,photo)
    

    img_icon = Image.open(note_icon_path).resize((200, 200))
    tkimg_icon = ImageTk.PhotoImage(img_icon)

    label_img = tk.Label(secondary_window, image=tkimg_icon, background="white")
    label_img.image = tkimg_icon  
    label_img.pack(pady=10)
    label_text = tk.Label(secondary_window, text="Your Note: App de notas", font=(font_bold_path, 13), foreground="black", background="white")
    label_text.pack(pady=5)
    label_text2 = tk.Label(secondary_window, text="Versión 1.0", font=(font_path, 10), foreground="black", background="white")
    label_text2.pack(pady=8)
    label_text4 = tk.Label(secondary_window, text="Your Note es una herramienta la cual permite crear una lista de actividades y exportarla como una imagen PNG", font=(font_path, 10), foreground="black", wraplength=355, justify="center", anchor="center", background="white")
    label_text4.pack(pady=11)

    close_button = tk.Button(secondary_window, text="Cerrar", font=("assets/fonts/tahoma.ttf", 10), cursor="hand2",
                             relief="raised", bd=3, bg="#27548A", fg="white", command=secondary_window.destroy)
    close_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#183B4E"))
    close_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#27548A"))
    close_button.bind("<Enter>", lambda event: event.widget.config(bg="#183B4E")) 
    close_button.bind("<Leave>", lambda event: event.widget.config(bg="#27548A"))
    close_button.pack(pady=40)

    label_text3 = tk.Label(secondary_window, text="2025 - @areimo on GitHub", font=(font_path, 8), foreground="grey", background="white")
    label_text3.pack(pady=10)

    if os.path.exists(icon_path):
        try:
            secondary_window.iconphoto(icon_path)
        except Exception as e:
            print(f"⚠️ Advertencia: No se pudo cargar el icono. Error: {e}")
  
menu_bar = tk.Menu(root, tearoff=0, bg="white", fg="black", relief="flat")
menu_bar.add_command(label="Acerca de",command=open_window)
root.config(menu=menu_bar)

root.mainloop()