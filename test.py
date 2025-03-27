import tkinter as tk
import math
import time

class Clock(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, width=500, height=550)
        self.canvas.pack()
        self.canvas.create_rectangle(1, 1, 500, 500, fill="#008080")
        self.canvas.create_line(50, 525, 50, 500, fill="#00CED1")
        self.canvas.create_line(450, 525, 450, 500, fill="#00CED1")
        self.canvas.create_rectangle(50, 525, 450, 500, fill="#008080")
        self.canvas.create_arc(50, 500, 450, 550, start=0, extent=-180, fill="#008080", outline="#008080")
        self.canvas.create_oval(10, 10, 490, 490, fill="#20B2AA")
        self.canvas.create_text(250, 350, text='Время пить чай', font=('Times New Roman', 8))
        self.canvas.create_text(250, 225, text='.', font=("Times New Roman", 62))
        self.canvas.create_text(250, 525, text='27.03.2025', font=('Times New Roman', 20))


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

#секундная стрелка
        sec_end_x = 250 - 180 * math.cos(sec_angle * math.pi / 180 + math.pi / 2)
        sec_end_y = 250 - 180 * math.sin(sec_angle * math.pi / 180 + math.pi / 2)
        self.canvas.create_line(250, 250, sec_end_x, sec_end_y, width=2, fill='#008080', tags="hands")
        self.canvas.create_polygon(sec_end_x, sec_end_y,
                                   sec_end_x + 10 * math.cos((sec_angle + 90) * math.pi / 180),
                                   sec_end_y + 10 * math.sin((sec_angle + 90) * math.pi / 180),
                                   sec_end_x + 10 * math.cos((sec_angle - 90) * math.pi / 180),
                                   sec_end_y + 10 * math.sin((sec_angle - 90) * math.pi / 180),
                                   fill='#008080', outline='#008080', tags="hands")

#часовая стрелка
        hour_end_x = 250 - 150 * math.cos(hour_angle * math.pi / 180 + math.pi / 2)
        hour_end_y = 250 - 150 * math.sin(hour_angle * math.pi / 180 + math.pi / 2)
        self.canvas.create_line(250, 250, hour_end_x, hour_end_y, width=5, fill='#2F4F4F', tags="hands")
        self.canvas.create_polygon(hour_end_x, hour_end_y,
                                   hour_end_x + 10 * math.cos((hour_angle + 150) * math.pi / 180),
                                   hour_end_y
                                   + 10 * math.sin((hour_angle + 150) * math.pi / 180),
                                   hour_end_x + 10 * math.cos((hour_angle - 150) * math.pi / 180),
                                   hour_end_y + 10 * math.sin((hour_angle - 150) * math.pi / 180),
                                   fill='#2F4F4F', outline='#2F4F4F', tags="hands")
#минутная стрелка
        self.canvas.create_line(
            250, 250,
            250 - 180 * math.cos(min_angle * math.pi / 180 + math.pi / 2),
            250 - 180 * math.sin(min_angle * math.pi / 180 + math.pi / 2),
            width=3, fill='#BDB76B', tags="hands"
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
