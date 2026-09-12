from pet import Pet
from product import Product
from console_helper import *

global_pet_id = 0

def get_next_pet_id() -> int:
    global global_pet_id

    global_pet_id += 1

    return global_pet_id

def input_product_data() -> Pet:
    icon = input_str()
    name = input_str()
    breed = input_int()
    diseases = input_str()
    health_status = input_int()
    story = input_str()
    age = input_date()
    color = list(input_int())
    character = list(input_int())

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

def print_table_pets_header():

   print(
        f"{'ИД':<5}"
        f"{'Иконка':<1}"
        f"{'Кличка':<20}"
        f"{'Количество рождаемых детнышей за раз':<4}"
        f"{'Особенности':<100}"
        f"{'Возраст':<8}"
        f"{'История':<50}"
        f"{'Дата рождения':<12}"
        f"{'Окрас':<50}"
        f"{'Характеристики(дружелюбие, энергия, социализация)':<50}"
    )

def print_single_pet(pet: Pet):

    print(f"{pet.id:<5}{pet.icon:<1}{pet.name:<20}{pet.breed:<4}{pet.diseases:<100}{pet.health_status:<12}{pet.story:<50}{pet.age:<12}{pet.color:<50}{pet.character:<50}")

def print_all_pets(pets: list[Pet]):
    
    print_table_pets_header()


    if len(pets) > 0:
        for pet in pets:
            print_single_pet(pet)
    else:
        print("Список животных пуст")
        
        
def save_products_to_txt_file_for_print(products: list[Product], filename: str) -> bool:
    try:
        with open(filename, "w", encoding="utf-8") as file_out:
            file_out.write("Карточки питомцов, которые ждут вашего внимания\n\n")
                        
            file_out.write(             
            f"{'ИД':<5}"
            f"{'Иконка':<1}"
            f"{'Кличка':<20}"
            f"{'Количество рождаемых детнышей за раз':<4}"
            f"{'Особенности':<100}"
            f"{'Возраст':<8}"
            f"{'История':<50}"
            f"{'Дата рождения':<12}"
            f"{'Окрас':<50}"
            f"{'Характеристики(дружелюбие, энергия, социализация)':<50}"
            "\n")
            
            if len(products) > 0:
                for product in products:
                    file_out.write(
                        f"{Pet.id:<5}"
                        f"{Pet.icon:<15}"
                        f"{Pet.name:<20}"
                        f"{Pet.breed:<4}"
                        f"{Pet.diseases:<100}"
                        f"{Pet.health_status:<12}"
                        f"{Pet.story:<50}"
                        f"{Pet.age:<12}"
                        f"{Pet.color:<50}"
                        f"{Pet.character:<50}"
                        "\n""\n"
                    )
            
            print("Чтобы посмотреть следующуу карточку, нажмите Enter")
            return True
             
    except OSError:
        return False

    return True

for _ in range(count_products):
     Pet.append(
                    Pet(
                        id=int(file_in.post()),
                        icon=file_in.post().strip(),
                        name=str(file_in.post()),
                        breed=file_in.post().strip(),
                        diseases=file_in.post().strip(),
                        health_status=file_in.post().strip(),
                        story=file_in.post().strip(),
                        age=file_in.post().strip(),
                        color=file_in.post().strip(),
                        character=file_in.post().strip()
                    )
                )
                        
                    
                
