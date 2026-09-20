from pet import Pet
from datetime import date
from pets_functions import *
from console_helper import *
from products_functions import *
from match import *
from main_menu import *



def work_with_buyer_menu(pets: list[Pet],products: list[Product],list_color):


    is_run = True
    while is_run == True:
        print("Меню Покупателя:")
        print("1. Посмотреть все карточки животных")
        print("2. Найти животное по ID")
        print("3. Метч")
        print("4. Подать заявку на приобретение питомца")
        print("5. Подать заявку на продажу питомца")
        print("6. Приобрести аксессуары")
        print("0. В Главное меню")

        
        choosen_action = input_int("Выберите пункт меню: ", 0, 6)

        if choosen_action == 1:
            print_all_pets(pets, list_color)
        elif choosen_action == 2:
            search_id = input_int("Введите ID животного для поиска: ", 1, 2_000_000_000)
            found_pet = get_pet_by_id(pets, search_id)

            if found_pet == None:
                print(f"Животное с ID {search_id} не найдено")
            else:
                print_single_pet(found_pet,list_color)
        elif choosen_action == 3:
            
            match(pets, list_color)

        elif choosen_action == 4:
            search_id = input_int("введите ИД питомца которого вы хотите приобрести: ",1,2_000_000_000)
            found_pet = get_pet_by_id(pets, search_id)

            if found_pet == None:
                print(f"Животное с ID {search_id} не найдено")
            else:
                print_single_pet(found_pet,list_color)

                print("Вы забронировали этого животного")
                delete_pet_by_id(pets, search_id)

        elif choosen_action == 5:
            input_pet_data()
        elif choosen_action == 6:
            print_all_products(products)
            search_id = input_int("введите ИД аксессуара которого вы хотите приобрести: ",1,2_000_000_000)
            found_product = get_product_by_id(products, search_id)
            request_amount = input_int(
                "Введите количество товара для покупки: ", 1, 10_000
            )
            if found_product == None:
                print(f"Аксессуар с ID {search_id} не найден")
            else:
                print_single_product(found_product)

                is_bought = buy_product(products, search_id, request_amount)

                if is_bought == False:
                    print(
                        "Ошибка покупки товара проверьте что Вы ввели верный ID товара и товара достаточно на складе"
                    )
                else:
                    print("Товар успешно куплен")
        else:
            is_run = False

        wait_enter()
