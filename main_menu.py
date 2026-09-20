from pet import Pet
from console_helper import *
from pets_functions import *


def print_pets(pets: list[Pet], list_color):
    print("Список животных в приюте")
    print_all_pets(pets, list_color)
    print_devider("=", 125)


def print_main_menu():
    print("Главное меню:")
    print("1. Меню Покупателя")
    print("2. Меню Администратора")
    print("0. Выход")