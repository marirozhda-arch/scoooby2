from product import Product
from pet import Pet
from console_helper import *
from products_functions import *
from main_menu import *
from pets_functions import *

def auth_is_administrator():
    password = input_str(
        "Введите пароль Администратора для входа в Меню Администратора: ", 4, 16
    )
    return password == "12345"


def work_with_administrator_menu(pets: list[Pet],products: list[Product],list_color):
    is_run1 = True
    while is_run1 == True:
        print("Меню Администратора:")
        print("1. Посмотреть все карточки животных")
        print("2. Найти карточку питомца по ID")
        print("3. Добавить новую карточку питомца")
        print("4. Изменить карточку питомца по ID")
        print("5. Удалить карточку питомца по ID")
        print("6. Управление аксессуарами")
        print("0. В Главное меню")

        choosen_action = input_int("Выберите пункт меню: ", 0, 6)

        if choosen_action == 1:
            print_main_menu(pets)

        elif choosen_action == 2:
            search_id = input_int("Введите ID животного для поиска: ", 1, 2_000_000_000)
            found_pet = get_pet_by_id(pets, search_id)

            if found_pet == None:
                print(f"Животное с ID {search_id} не найдено")
            else:

                print_single_pet(found_pet, list_color)
        elif choosen_action == 3:
            print("Введите данные нового животного")

            new_pet = input_pet_data()

            new_pet.id = get_next_pet_id()

            add_product_to_list(pets, new_pet)

            print("Карточка питомца успешно добавлена")

        elif choosen_action == 4:
            update_id = input_int(
                "Введите ID животного для обновления: ", 1, 2_000_000_000
            )
            found_pet = get_product_by_id(products, update_id)

            if found_pet == None:
                print(f"Животное с ID {update_id} не найдено")
            else:
                print("Введите новые данные для продукта ")

                update_pet = input_pet_data()

                update_pet.id = update_id

                update_pet_by_id(pets, update_pet)

                print("Карточка питомца успешно обновлёнa")
        elif choosen_action == 5:
            delete_id = input_int("Введите ID товара для удаления: ", 1, 2_000_000_000)

            is_deleted = delete_pet_by_id(pets, delete_id)

            if is_deleted == False:
                print(f"Животное с ID {delete_id} не найдено")
            else:
                print("Карточка питомца успешно удалёна")

        elif choosen_action == 6:
            is_run2 = True
            while is_run2 == True:

                print("Меню Администратора:")
                print("Управление аксессуарами")
                print("1. Посмотреть все аксессуары")
                print("2. Найти аксессуар по ID")
                print("3. Добавить новый аксессуар")
                print("4. Изменить аксессуар по ID")
                print("5. Удалить аксессуар по ID")
                print("0. Назад")

            if choosen_action == 1:
                
                print_main_menu(products)

            elif choosen_action == 2:
                search_id = input_int("Введите ID товара для поиска: ", 1, 2_000_000_000)
                found_product = get_product_by_id(products, search_id)

                if found_product == None:
                    print(f"Продукт с ID {search_id} не найден")
                else:
                    print_single_product(found_product)
            elif choosen_action == 3:
                print("Введите данные нового продукта")

                new_product = input_product_data()

                new_product.id = get_next_product_id()

                add_product_to_list(products, new_product)

                print("Товар успешно добавлен")

            elif choosen_action == 4:
                update_id = input_int(
                    "Введите ID товара для обновления: ", 1, 2_000_000_000
                )
                found_product = get_product_by_id(products, update_id)

                if found_product == None:
                    print(f"Продукт с ID {update_id} не найден")
                else:
                    print("Введите новые данные для продукта ")

                    update_product = input_product_data()

                    update_product.id = update_id

                    update_product_by_id(products, update_product)

                    print("Продукт успешно обновлён")

            elif choosen_action == 5:
                delete_id = input_int("Введите ID товара для удаления: ", 1, 2_000_000_000)

                is_deleted = delete_product_by_id(products, delete_id)

                if is_deleted == False:
                    print(f"Продукт с ID {delete_id} не найден")
                else:
                    print("Продукт успешно удалён")
            elif choosen_action == 0:
                is_run2 = False


        elif choosen_action == 0:
            is_run1 = False

        wait_enter()