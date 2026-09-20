from product import Product
from datetime import date
from console_helper import *

global_product_id = 0

def get_next_product_id() -> int:
    global global_product_id

    global_product_id += 1

    return global_product_id

def input_product_data() -> Product:
    icon = input_str("Вставьте иконку товара (одно эмодзи): ", 1, 10)
    best_before_date = input_date(        
        "Введите дату производства в формет ДД.ММ.ГГГГ: ",
        date(2026, 1, 1),
        date.today())
    
    name = input_str("Введите название товара (от 1 до 25 символов): ", 1, 25)
    category = input_str("Введите категорию товара (от 1 до 20 символов): ", 1, 20)
    price = input_int("Введите цену товара (от 1 до 10 000 000 руб.): ", 1, 10_000_000)
    rating = input_float("Введите рейтинг товара (от 1 до 5, можно дробный): ", 1, 5)
    amount = input_int(
        "Введите количество товара на складе (от 1 до 10 000 ед.): ", 1, 10_000
    )

    return Product(
        icon=icon,
        best_before_date=best_before_date,
        name=name,
        category=category,
        price=price,
        rating=rating,
        amount=amount,
    )

def get_product_by_id(products: list[Product], search_id: int) -> Product | None:
    for product in products:
        if product.id == search_id:
            return product

    return None


def add_product_to_list(products: list[Product], product: Product):
    products.append(product)

def update_product_by_id(products: list[Product], product: Product) -> bool:
    find_product = get_product_by_id(products, product.id)

    if find_product == None:
        return False

    find_product.icon = product.icon
    find_product.best_before_date = product.best_before_date
    find_product.name = product.name
    find_product.category = product.category
    find_product.price = product.price
    find_product.rating = product.rating
    

    return True

def delete_product_by_id(products: list[Product], search_id: int) -> bool:
   
    find_product = get_product_by_id(products, search_id)
    if find_product == None:
        return False
    products.remove(find_product)

    return True

def print_table_products_header():


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

def print_single_product(product: Product):
    print_devider("=", 60)
    print(f"{product.icon}  {product.name}  (ID: {product.id})")
    print_devider("-", 60)
    print(f"Категория: {product.category}")
    print(f"Цена: {product.price} руб.")
    print(f"Рейтинг: {product.rating} / 5")
    print(f"В наличии: {product.amount} шт.")
    print(f"Годен до: {product.best_before_date.strftime('%d.%m.%Y')}")
    print_devider("=", 60)

def print_all_products(products: list[Product]):
    
    print_devider("=", 60)
    print("Список аксессуаров".center(60))
    print_devider("=", 60)


    if len(products) > 0:
        for product in products:
            print_single_product(product)
    else:
        print("Список товаров пуст")

def buy_product(products: list[Product], search_id: int, request_amount: int) -> bool:
    find_product = get_product_by_id(products, search_id)


    if find_product == None:
        return False

    if find_product.amount < request_amount:
        return False

    find_product.amount -= request_amount

    return True