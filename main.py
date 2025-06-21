import os
from tkinter import Tk, Button, Label, filedialog, StringVar
from moviepy.editor import VideoFileClip, vfx

def process_video(input_path, output_path):
    clip = VideoFileClip(input_path)

    # fundal blurat la 1920×1080
    blurred = clip.fx(vfx.blur, size=50)
    bg = blurred.resize(height=1920)
    x1 = (bg.w - 1080) / 2
    bg = bg.crop(x1=x1, width=1080)

    # clip original redimensionat dacă e nevoie
    fg = clip
    if clip.w != 1080:
        fg = clip.resize(width=1080)
    y_pos = (1920 - fg.h) / 2

    final = bg.set_duration(fg.duration).overlay(
        fg.set_position(("center", y_pos))
    )

    final.write_videofile(output_path, codec="libx264", audio_codec="aac")

def select_and_run():
    inp = filedialog.askopenfilename(
        title="Selectează video input",
        filetypes=[("MP4 files","*.mp4"),("All files","*.*")]
    )
    if not inp: return

    out_default = os.path.splitext(inp)[0] + "_tiktok.mp4"
    out = filedialog.asksaveasfilename(
        title="Salvează ca",
        initialfile=os.path.basename(out_default),
        defaultextension=".mp4",
        filetypes=[("MP4 files","*.mp4")]
    )
    if not out: return

    status.set("Procesare în curs…")
    root.update()
    process_video(inp, out)
    status.set(f"Finalizat: {os.path.basename(out)}")

# GUI
root = Tk()
root.title("Covertor Reclame Haladit")
root.geometry("400x150")

btn = Button(root, text="Alege video și convertește", command=select_and_run, padx=10, pady=5)
btn.pack(pady=20)

status = StringVar(value="Așteptare…")
lbl = Label(root, textvariable=status)
lbl.pack()

root.mainloop()
