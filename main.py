from GUI import GUI
from Level import Level


def main():
    Level.init_levels()

    new_gui = GUI()
    new_gui.run()


if __name__ == '__main__':
    main()
