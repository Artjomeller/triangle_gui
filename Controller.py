from tkinter import messagebox
from Model import TriangleModel
from View import TriangleView

class TriangleController:
    def __init__(self):
        self.model = TriangleModel()
        self.view = TriangleView(self)

    def show_error(self, message):
        self.view.show_error_message(message)

    def calculate_button_pressed(self, event=None):
        try:
            side_a = float(self.view.entry_side_a.get())
            side_b = float(self.view.entry_side_b.get())

            if side_a <= 0 and side_b <= 0:
                self.show_error('Kolmnurga alus ja kõrgus peavad olema positiivne arv.')
                return
            elif side_a <= 0:
                self.show_error('Kolmnurga alus peab olema positiivne arv.')
                return
            elif side_b <= 0:
                self.show_error('Kolmnurga kõrgus peab olema positiivne arv.')
                return

            hypotenuse, perimeter, area = self.model.calculate_triangle_properties(side_a, side_b)
            self.view.display_results(hypotenuse, perimeter, area, side_a, side_b)

            # Puhastame sisestusväljad
            self.view.entry_side_a.delete(0, 'end')
            self.view.entry_side_b.delete(0, 'end')

            # Fokusseerime esimesele sisestusväljale
            self.view.entry_side_a.focus()

        except ValueError:
            self.show_error('Sisestage palun arvulised väärtused kõikidesse väljadesse.')

    def run(self):
        self.view.mainloop()

    def on_close(self):
        if messagebox.askokcancel('Välju Rakendusest', 'Oled kindel, et soovid rakendusest väljuda?'):
            self.view.destroy()
