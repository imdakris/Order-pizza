def new_order() -> bool:
    """New order"""
    answer = input(f"Will you be placing a new order?; y/n")
    if answer == "y":
        return False
    elif answer == "n":
        return True


def get_order(ingredients: list) -> list:
    '''Get order'''
    order = []
    for ingredient in ingredients:
        command = input(f"Add {ingredient}; y/n: ")
        if command == "y":
            order.append(ingredient)
    return order


def check_order(order: list) -> bool:
    '''Check order'''
    if not order:
        print("You haven't ordered anything")
        return new_order()
    for ingredient in order:
        print(ingredient)
    answer = input("Correct order?; y/n")
    if answer == "y":
        print("Your order is accepted. Wait.")
        return True
    elif answer == "n":
        return new_order()


def main() -> None:
    '''Main'''
    while True:
        ingredients = ["tomatoes", "mushrooms", "cheese", "sausage", "olives"]
        order = get_order(ingredients)
        if check_order(order):
            exit()




if __name__ == "__main__":
    main()
