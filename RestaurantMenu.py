def add_menu_item(menu, item):
    if item not in menu:
        menu.append(item)
    else:
        print(f'"{item}" is already in the menu')
def remove_menu_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f'"{item}" does not exist in the menu')
def check_menu_item(menu, item):
    if item in menu:
        print(f'Avaliability:"{item} is available"')
    else:
        print(f'Avaliability: {item} is not available')
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = input("Add item: ")
remove_item = input("Remove item: ")
check_item = input("Check item: ")
add_menu_item(initial_menu, add_item)
remove_menu_item(initial_menu, remove_item)
print("Updated menu:", initial_menu)
check_menu_item(initial_menu, check_item)
