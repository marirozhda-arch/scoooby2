from pet import Pet
from console_helper import *
from pets_functions import *
import random
import math
from moc import *


def ask_question(question_text: str, answers: list[str]) -> int:
    print("")
    print(question_text)
    print("")
    for i, answer in enumerate(answers, start=1):
        print(f"{i}. {answer}")
    return input_int("Ваш ответ (1, 2 или 3): ", 1, 3)


def match(pets: list[Pet], list_color):
    energy = 0
    socialization = 0
    patience = 0

    print_devider("=", 60)
    print("Метч с питомцем")
    print("Ответьте на 5 вопросов, и мы подберём идеального питомца!")
    print_devider("=", 60)

    answer = ask_question(
        "Вопрос 1. Представьте идеальный субботний день. Чем вы займётесь?",
        ["Проспать до обеда, сериал, доставка",
         "Встретиться с друзьями, кино, кафе",
         "Поход, пробежка 10 км, танцы"],
    )

    if answer == 1:
        energy += 1
    elif answer == 2:
        energy += 5
    else:
        energy += 10

    answer = ask_question(
        "Вопрос 2. Вы пришли на вечеринку, где почти никого не знаете. Ваше поведение?",
        ["Найду укромный уголок, буду в телефоне",
         "Подойду к дружелюбному человеку, заведу беседу",
         "Я - душа компании, сразу в центр"],
    )

    if answer == 1:
        socialization += 1
    elif answer == 2:
        socialization += 5
    else:
        socialization += 10

    answer = ask_question(
        "Вопрос 3. Коллега разбил вашу любимую кружку и не извинился.",
        ["Взрыв эмоций, настроение испорчено",
         "Расстроюсь, но сдержусь (бывает)",
         "Флегматично уберу осколки (это просто вещь)"],
    )

    if answer == 1:
        patience += 1
    elif answer == 2:
        patience += 6
    else:
        patience += 10

    answer = ask_question(
        "Вопрос 4. Как вы восстанавливаете силы после тяжёлой недели?",
        ["Тишина, книга, никого не трогаю",
         "Шумная тусовка, караоке",
         "Спортзал в одиночку"],
    )

    if answer == 1:
        energy += 0
        socialization += 0
    elif answer == 2:
        energy += 8
        socialization += 10
    else:
        energy += 8
        socialization += 2

    answer = ask_question(
        "Вопрос 5. На полу в гостиной огромная лужа (неважно от чего). Ваши мысли?",
        ["Почему вечно всё через одно место?!",
         "Бедняга, пойду уберу и успокою",
         "Срочно убрать, без паники"],
    )

    if answer == 1:
        patience += 0
    elif answer == 2:
        patience += 10
        socialization += 8
    else:
        patience += 8
        energy += 5

    energy = round(energy / 18 * 10)
    socialization = round(socialization / 28 * 10)
    patience = round(patience / 20 * 10)

    character_ueser = [energy, socialization, patience]

    if not pets:
        print("Список питомцев пуст")
        return None

    best_distance = float('inf')
    best_pets = []

    for pet in pets:
        diff = [character_ueser[i] - pet.character[i] for i in range(3)]
        distance = math.sqrt(sum(d**2 for d in diff))

        if distance < best_distance:
            best_distance = distance
            best_pets = [pet]
        elif distance == best_distance:
            best_pets.append(pet)

    best_pet = random.choice(best_pets)

    print_devider("=", 60)
    print(f"Ваш профиль: Энергия {energy}, Социализация {socialization}, Терпеливость {patience}")
    print("Идеальный питомец для вас:")
    print_devider("=", 60)

    print_single_pet(best_pet, list_color)