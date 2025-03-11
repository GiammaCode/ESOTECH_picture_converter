import tkinter as tk
from view.main_view import MainView
from controller.app_controller import AppController


def main():
    root = tk.Tk()

    view = MainView(root)
    controller = AppController(view)
    view.set_controller(controller)

    view.create_widgets()  # Dopo aver settato il controller

    root.mainloop()


if __name__ == "__main__":
    main()
