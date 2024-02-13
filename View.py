from tkinter import *
from tkinter import messagebox

class TriangleView(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('Täisnurkse kolmnurga kalkulaator')

        # Loome kaks frame't
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        # Vidinate loomine
        (self.entry_side_a, self.entry_side_b, self.btn_calculate, self.text_box) = self.create_frame_widgets()

        self.bind('<Return>', self.controller.calculate_button_pressed)  # Enter klahvi vajutus tööle
        self.bind('<Escape>', self.on_close)  # Esc klahvi vajutus tööle
        self.protocol('WM_DELETE_WINDOW', self.on_close)

        # Aseta aken ekraani keskele ja keela suuruse muutmine
        self.center_window()
        self.resizable(False, False)

    def center_window(self):
        self.update_idletasks()
        width = 470
        height = 200
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame_height = 50  # Fikseeritud top frame resolutsioon

        frame = Frame(self, bg='blanchedalmond', height=frame_height)
        frame.pack(side=TOP, fill=X, expand=True)
        return frame

    def create_bottom_frame(self):
        frame_height = 100  # Fikseeritud bottom frame resolutsioon

        frame = Frame(self, bg='blanchedalmond', height=frame_height)
        frame.pack(side=TOP, fill=BOTH, expand=True)
        return frame

    def create_frame_widgets(self):
        # Sisestusväljad
        label_side_a = Label(self.top_frame, text="Kolmnurga alus", font=('Verdana', 12), bg='blanchedalmond')
        label_side_a.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        entry_side_a = Entry(self.top_frame, font=('Verdana', 12))
        entry_side_a.grid(row=0, column=1, padx=5, pady=5)

        label_side_b = Label(self.top_frame, text="Kolmnurga kõrgus", font=('Verdana', 12), bg='blanchedalmond')
        label_side_b.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        entry_side_b = Entry(self.top_frame, font=('Verdana', 12))
        entry_side_b.grid(row=1, column=1, padx=5, pady=5)

        # Arvutusnupp
        btn_calculate = Button(self.top_frame, text='Arvuta', font=('Verdana', 12),
                               command=self.controller.calculate_button_pressed)
        btn_calculate.grid(row=1, column=2, rowspan=2, padx=5, pady=5, sticky='ew')

        # Tekstikast
        text_box = Text(self.bottom_frame, font='Verdana', width=50, height=10)
        text_box.pack(expand=True, fill=BOTH, padx=5, pady=5)

        return entry_side_a, entry_side_b, btn_calculate, text_box

    def display_results(self, hypotenuse, perimeter, area, side_a, side_b):
        results_text = f'Kolmnurga alus: {side_a:.1f}\n'
        results_text += f'Kolmnurga kõrgus: {side_b:.1f}\n'
        results_text += f'Hüpotenuus: {hypotenuse}\n'
        results_text += f'Ümbermõõt: {perimeter}\n'
        results_text += f'Pindala: {area}\n'

        self.text_box.config(state='normal')  # Tekstikasti saab kirjutada
        self.text_box.delete('1.0', END)
        self.text_box.insert('insert', results_text + '\n')
        self.text_box.config(state='disabled')


    def on_close(self, event=None):
        # Kui akent üritatakse sulgeda
        if messagebox.askokcancel('Välju rakendusest', 'Kas soovid tõesti rakendusest väljuda?'):
            self.destroy()

    def show_error_message(self, message):
        messagebox.showerror('Viga', message)

