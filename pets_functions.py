from pet import Pet
from product import Product
from console_helper import *
from moc import *

global_pet_id = 0

def get_next_pet_id() -> int:
    global global_pet_id

    global_pet_id += 1

    return global_pet_id

def input_pet_data() -> Pet:
    icon = input_str("Вставьте иконку животного (одно эмодзи): ", 1, 10)
    name = input_str("Введите имя животного  (от 1 до 25 символов): ", 1, 15)
    breed = input_int(f"Введите код породы из справочника (от 1 до {len(BREEDS)}): ", 1, len(BREEDS))
    diseases = input_str("Введите какими болезнями болеет животное(от 1 до 30 символов)",1 ,30)
    health_status = input_int("Введите общее состояние здоровья (от 1 до 10): ", 1, 10)
    story = input_str("Введите историю (от 1 до 30 символов): ", 1, 30)
    age = input_date("Введите дату рождения животнуму (в формате ДД.ММ.ГГГГ): ", date(2026, 1, 1),date.today(),)
    color = [input_int("Введите код цвета (от 1 до 8): ", 1, 8)]
    character = [
        input_int("Введите насколько выражена энергия от 1 до 10: ", 1, 10),
        input_int("Введите насколько выражена социализация от 1 до 10: ", 1, 10),
        input_int("Введите насколько выражена терпеливость от 1 до 10: ", 1, 10),
    ]

    return Pet(
        icon=icon,
        name=name,
        breed=breed,
        diseases=diseases,
        health_status=health_status,
        story=story,
        age=age,
        color=color,
        character=character,
    )
    
def get_pet_by_id(pets: list[Pet], search_id: int) -> Pet | None:
    for pet in pets:
        if pet.id == search_id:
            return pet
        
    return None

def add_pet_to_list(pets: list[Pet], pet: Pet):
    pets.append(pet)

def update_pet_by_id(pets: list[Pet], pet: Pet) -> bool:
    find_pet = get_pet_by_id(pets, pet.id)

    if find_pet == None:
        return False

    find_pet.icon = pet.icon
    find_pet.name = pet.name
    find_pet.breed = pet.breed
    find_pet.diseases = pet.diseases
    find_pet.health_status = pet.health_status
    find_pet.story = pet.story
    find_pet.age = pet.age
    find_pet.color = pet.color
    find_pet.character = pet.character

    return True


def delete_pet_by_id(pets: list[Pet], search_id: int) -> bool:
   
    find_pet = get_pet_by_id(pets, search_id)
    if find_pet == None:
        return False
    pets.remove(find_pet)

    return True

def print_single_pet(pet: Pet, list_color):
    print_devider("=", 60)
    print(f"{pet.icon}  {pet.name}  (ID: {pet.id})")
    print_devider("-", 60)
    print(f"Порода: {get_breed_name(pet.breed)}")
    print(f"Здоровье: {pet.health_status}/10")
    print(f"Болезни: {pet.diseases if pet.diseases else 'нет'}")
    print(f"Дата рождения: {pet.age.strftime('%d.%m.%Y')}")
    print(f"Цвет: {print_color(pet, list_color)}")
    print(f"Характер: {print_character(pet)}")
    print(f"История: {pet.story}")
    print_devider("=", 60)

def print_all_pets(pets: list[Pet], list_color):
    if len(pets) > 0:
        for pet in pets:
            print_single_pet(pet, list_color)
    else:
        print("Список животных пуст")


def print_color(pet: Pet, list_color: list):
    color = pet.color

    colors = []
    for one_color in color:
        if isinstance(one_color, int):
            colors.append(list_color[one_color - 1])
        else:
            colors.append(one_color)

    return ", ".join(colors)

def print_character(pet: Pet):
    character = pet.character

    return f"Энергия {character[0]}, Социализация {character[1]}, Терпеливость {character[2]}"
