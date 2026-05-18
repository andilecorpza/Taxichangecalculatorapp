from kivy.app import App
from kivy.lang import Builder
from datetime import datetime


class TaxiApp:
    history = []

    def calculate(self, root):
        try:
            fare = float(root.ids.fare.text)
            people = int(root.ids.people.text)
            paid = float(root.ids.paid.text)

            total = fare * people
            change = paid - total

            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.history.append(
                f"{time_now} | Spent: R{total:.2f} | Change: R{change:.2f}"
            )

            root.ids.result.text = f"Change: R{change:.2f}"

        except:
            root.ids.result.text = "Invalid input"

    def show_history(self, root):
        if not self.history:
            root.ids.result.text = "No history yet"
        else:
            root.ids.result.text = "\n".join(self.history[-10:])

    def clear(self, root):
        root.ids.fare.text = ""
        root.ids.people.text = ""
        root.ids.paid.text = ""
        root.ids.result.text = ""


class TaxiAppUI(App):

    logic = TaxiApp()

    def build(self):
        return Builder.load_file("main.kv")

    def calculate(self, root):
        self.logic.calculate(root)

    def show_history(self, root):
        self.logic.show_history(root)

    def clear(self, root):
        self.logic.clear(root)


TaxiAppUI().run()