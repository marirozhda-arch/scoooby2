from dataclasses import dataclass,timedelta
from datetime import date
from typing import List, Optional
from pet import Pet
from product import Product

mock_pets = [
    Pet(
        icon="🐶",
        name="Барсик",
        breed=3,          # например, дворняжка
        diseases="",
        health_status=9,
        story="Найден на улице, очень ласковый и дружелюбный.",
        age=date(2021, 5, 10),
        color=["Рыжий", "Белый"],
        character=[6, 8, 7],
        id=1,
    ),
    Pet(
        icon="🐱",
        name="Мурка",
        breed=7,          # британская
        diseases="Аллергия на курицу",
        health_status=7,
        story="Хозяйка переехала за границу, ищет новый дом.",
        age=date(2020, 11, 2),
        color=["Серый"],
        character=[3, 5, 9],
        id=2,
    ),
    Pet(
        icon="🐕",
        name="Рекс",
        breed=1,          # немецкая овчарка
        diseases="",
        health_status=10,
        story="Спасён из плохих условий, прошёл обучение.",
        age=date(2019, 3, 15),
        color=["Чёрный", "Коричневый"],
        character=[9, 7, 4],
        id=3,
    ),
    Pet(
        icon="🐈",
        name="Лайма",
        breed=12,         # сиамская
        diseases="",
        health_status=8,
        story="Очень общительная, любит детей.",
        age=date(2022, 7, 20),
        color=["Белый", "Серый"],
        character=[5, 10, 6],
        id=4,
    ),
    Pet(
        icon="🐰",
        name="Пушистик",
        breed=25,         # декоративный кролик
        diseases="Чувствительное пищеварение",
        health_status=6,
        story="Отказник из зоомагазина, нужен особый уход.",
        age=date(2023, 1, 30),
        color=["Белый"],
        character=[2, 3, 8],
        id=5,
    ),
    Pet(
        icon="🦜",
        name="Кеша",
        breed=30,         # волнистый попугай
        diseases="",
        health_status=9,
        story="Весёлый и разговорчивый, любит внимание.",
        age=date(2020, 9, 12),
        color=["Пятнистый"],
        character=[7, 8, 5],
        id=6,
    ),
    Pet(
        icon="🐹",
        name="Шарик",
        breed=18,         # хомяк
        diseases="",
        health_status=8,
        story="Маленький и шустрый, любит крутиться в колесе.",
        age=date(2022, 2, 5),
        color=["Рыжий"],
        character=[6, 2, 6],
        id=7,
    ),
    Pet(
        icon="🐢",
        name="Тортилла",
        breed=40,         # сухопутная черепаха
        diseases="",
        health_status=10,
        story="Медлительная и спокойная, любит греться под лампой.",
        age=date(2015, 6, 1),
        color=["Коричневый", "Зелёный"],
        character=[1, 1, 10],
        id=8,
    ),
    Pet(
        icon="🐍",
        name="Змейка",
        breed=35,         # маисовый полоз
        diseases="",
        health_status=7,
        story="Спокойная, привыкла к рукам, ест заморозку.",
        age=date(2021, 12, 10),
        color=["Полосатый", "Оранжевый"],
        character=[4, 2, 9],
        id=9,
    ),
    Pet(
        icon="🐠",
        name="Голди",
        breed=50,         # золотая рыбка
        diseases="",
        health_status=5,
        story="Из аквариума, нужен просторный аквариум.",
        age=date(2023, 10, 1),
        color=["Золотой"],
        character=[1, 1, 5],
        id=10,
    ),
    Pet(
        icon="🦎",
        name="Геккон",
        breed=45,         # леопардовый геккон
        diseases="",
        health_status=9,
        story="Очень милый, любит, когда его кормят с пинцета.",
        age=date(2021, 4, 18),
        color=["Пятнистый", "Жёлтый"],
        character=[3, 3, 8],
        id=11,
    ),
    Pet(
        icon="🐴",
        name="Буян",
        breed=60,         # пони
        diseases="Артрит задних ног (лёгкая степень)",
        health_status=4,
        story="Спасён с фермы, нужен опытный хозяин и выпас.",
        age=date(2012, 8, 25),
        color=["Коричневый", "Чёрный"],
        character=[8, 6, 2],
        id=12,
    ),
]



TODAY = date.today()

mock_products = [
    Product(
        icon="🦴",
        best_before_date=TODAY + timedelta(days=365),
        name="Игрушка-кость резиновая",
        category="Игрушки",
        price=349,
        rating=4.7,
    ),
    Product(
        icon="🐕",
        best_before_date=TODAY + timedelta(days=180),
        name="Ошейник кожаный с застёжкой",
        category="Ошейники и поводки",
        price=1299,
        rating=4.8,
    ),
    Product(
        icon="🦮",
        best_before_date=TODAY + timedelta(days=180),
        name="Поводок-рулетка 5 м",
        category="Ошейники и поводки",
        price=1599,
        rating=4.5,
    ),
    Product(
        icon="🐾",
        best_before_date=TODAY + timedelta(days=90),
        name="Лежанка мягкая 60×50 см",
        category="Лежанки и домики",
        price=2899,
        rating=4.9,
    ),
    Product(
        icon="🧶",
        best_before_date=TODAY + timedelta(days=730),
        name="Домик-плед для кошки",
        category="Лежанки и домики",
        price=2199,
        rating=4.6,
    ),
    Product(
        icon="🐱",
        best_before_date=TODAY + timedelta(days=365),
        name="Когтеточка вертикальная",
        category="Когтеточки",
        price=1799,
        rating=4.7,
    ),
    Product(
        icon="🪮",
        best_before_date=TODAY + timedelta(days=1825),
        name="Щётка-пуходёрка для вычёсывания",
        category="Уход и груминг",
        price=459,
        rating=4.4,
    ),
    Product(
        icon="🥣",
        best_before_date=TODAY + timedelta(days=1825),
        name="Миска-непроливайка на резиновом основании",
        category="Посуда",
        price=799,
        rating=4.6,
    ),
    Product(
        icon="🐟",
        best_before_date=TODAY + timedelta(days=365),
        name="Игрушка-удочка с перьями",
        category="Игрушки",
        price=299,
        rating=4.3,
    ),
    Product(
        icon="🎒",
        best_before_date=TODAY + timedelta(days=730),
        name="Переноска-рюкзак с иллюминатором",
        category="Переноски",
        price=3499,
        rating=4.5,
    ),
]