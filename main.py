from product import Product
from console_helper import *
from moc import *
from buyer_menu import *
from administrator_menu import *
from main_menu import *

pets: list[Pet] = []
products: list[Product] = []
list_color: list = ["Чёрный", "Белый", "Рыжий", "Серый", "Коричневый", "Пятнистый", "Полосатый", "Другой"]


for prod in mock_products:
    add_product_to_list(products, prod)

for prod in mock_pets:
    add_pet_to_list(pets, prod)

is_run = True

while is_run == True:
    print_pets(pets, list_color)

    print_main_menu()
    choosen_action = input_int("Выберите пункт меню: ", 0, 2)

    if choosen_action == 1:
        work_with_buyer_menu(pets,products,list_color)
    elif choosen_action == 2:
        if auth_is_administrator() == True:
            print("Пароль успешно введён")
            work_with_administrator_menu(pets,products,list_color)
        else:
            print("Ошибка ввода пароля администратора")
    elif choosen_action == 0:
        is_run = False