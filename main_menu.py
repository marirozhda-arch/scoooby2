from pet import Pet
from console_helper import *
from products_functions import *


def print_pets(pets: list[Pet]):
    print("Список животных в приюте")
    print_all_products(pets)
    print_devider("=", 125)


def print_main_menu():
    print("Главное меню:")
    print("1. Меню Покупателя")
    print("2. Меню Администратора")
    print("0. Выход")