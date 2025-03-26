import tkinter as tk
import math
import time


class Clock(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, width=500, height=550)
        self.canvas.pack()
        self.canvas.create_rectangle(1, 1, 500, 500, fill="lightblue")
        self.canvas.create_line(100, 100, 500, 500, fill="lightblue")
        self.canvas.create_oval(10, 10, 490, 490, fill="lightblue")
        self.canvas.create_text(250, 350, text='Время пить чай', font=('Times New Roman', 8))
        self.canvas.create_text(250, 225, text='.', font=("Times New Roman", 62))

        self.draw_clock_markings()

        self.update_clock()


    def draw_clock_markings(self):
        for i in range(60):
            self.canvas.create_line(
                250 + 210 * math.cos(-i * 6 * math.pi / 180 + math.pi / 2),
                250 - 210 * math.sin(-6 * i * math.pi / 180 + math.pi / 2),
                250 + 190 * math.cos(-6 * i * math.pi / 180 + math.pi / 2),
                250 - 190 * math.sin(-6 * i * math.pi / 180 + math.pi / 2),
                width=2
            )
            if i % 5 == 0:
                self.canvas.create_line(
                    250 + 215 * math.cos(-i * 6 * math.pi / 180 + math.pi / 2),
                    250 - 215 * math.sin(-6 * i * math.pi / 180 + math.pi / 2),
                    250 + 190 * math.cos(-6 * i * math.pi / 180 + math.pi / 2),
                    250 - 190 * math.sin(-6 * i * math.pi / 180 + math.pi / 2),
                    width=4
                )

        for i in range(12):
            self.canvas.create_text(
                250 + 225 * math.cos(-i * 30 * math.pi / 180 + math.pi / 2),
                250 - 225 * math.sin(-30 * i * math.pi / 180 + math.pi / 2),
                text=i + 1, font=('Arial', 16)
            )

    def update_clock(self):

        time_now = time.localtime()
        time_sec = int(time.strftime("%S", time_now))
        time_hour = int(time.strftime("%I", time_now))
        time_min = int(time.strftime("%M", time_now))

        sec_angle = 6 * time_sec
        min_angle = time_min * 6 + time_sec * 0.1
        hour_angle = time_hour * 30 + time_min * 60 * (30 / 3600)

        self.canvas.delete("hands")


        sec_end_x = 250 - 180 * math.cos(sec_angle * math.pi / 180 + math.pi / 2)
        sec_end_y = 250 - 180 * math.sin(sec_angle * math.pi / 180 + math.pi / 2)
        self.canvas.create_line(250, 250, sec_end_x, sec_end_y, width=2, fill='red', tags="hands")
        self.canvas.create_polygon(sec_end_x, sec_end_y,
                                   sec_end_x + 10 * math.cos((sec_angle + 90) * math.pi / 180),
                                   sec_end_y + 10 * math.sin((sec_angle + 90) * math.pi / 180),
                                   sec_end_x + 10 * math.cos((sec_angle - 90) * math.pi / 180),
                                   sec_end_y + 10 * math.sin((sec_angle - 90) * math.pi / 180),
                                   fill='red', outline='red', tags="hands")


        hour_end_x = 250 - 150 * math.cos(hour_angle * math.pi / 180 + math.pi / 2)
        hour_end_y = 250 - 150 * math.sin(hour_angle * math.pi / 180 + math.pi / 2)
        self.canvas.create_line(250, 250, hour_end_x, hour_end_y, width=5, fill='darkblue', tags="hands")
        self.canvas.create_polygon(hour_end_x, hour_end_y,
                                   hour_end_x + 10 * math.cos((hour_angle + 150) * math.pi / 180),
                                   hour_end_y
                                   + 10 * math.sin((hour_angle + 150) * math.pi / 180),
                                   hour_end_x + 10 * math.cos((hour_angle - 150) * math.pi / 180),
                                   hour_end_y + 10 * math.sin((hour_angle - 150) * math.pi / 180),
                                   fill='darkblue', outline='darkblue', tags="hands")

        self.canvas.create_line(
            250, 250,
            250 - 180 * math.cos(min_angle * math.pi / 180 + math.pi / 2),
            250 - 180 * math.sin(min_angle * math.pi / 180 + math.pi / 2),
            width=3, fill='darkblue', tags="hands"
        )

        self.canvas.delete("text")
        text_bottom = '2-2 ис'
        self.canvas.create_text(950, 525, text=text_bottom, font=('Arial', 16), tags="text")

        self.canvas.move("text", -0.5, 0)
        if self.canvas.bbox("text")[2] < 0:
            self.canvas.move("text", 600, 0)
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = Clock(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
