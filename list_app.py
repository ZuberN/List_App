import os

shopping_list = []


def show_help():
    print("\U0001F31F"*58)
    print(" Use this list application to keep track of what you need!")
    print("\U0001F31F"*58)
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
ENTER 'SHOW' to see current list.
""")


def add_to_list(item):
    word=shopping_list.append(item)
    length=len(shopping_list)
    print("Item has been added to the list at position",length,".")
    
    
def show_list(shopping_list):
    print("Here is the list:")
    for item in shopping_list:
        print(item)
        
def clear_screen():
    os.system("cls"if os.name == "nt" else "clear")


show_help()

while True:
    new_item = input("> ")
    
    if new_item == 'DONE':
        break
    elif new_item =='HELP':
        show_help()
        continue
    elif new_item =='SHOW':
        show_list(shopping_list)
        continue
        
    add_to_list(new_item)
show_list(shopping_list)
#print(shopping_list)

