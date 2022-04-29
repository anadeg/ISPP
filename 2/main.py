from Controller.controller import Controller
from Model.model import Model
from View.view import MainApp


def main():
    m = Model()
    c = Controller(m)
    MainApp(c).run()


if __name__ == "__main__":
    main()
