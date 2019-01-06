#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from IPython.display import clear_output

def instructions():
    print("""Enter 'ADD' to add an item to your cart.
Enter 'SHOW' to see what items are in your cart.
Enter 'HELP' to see your instructions.
Enter 'CLEAR' to delete all items from your cart.
Enter 'REMOVE' to delete a specific item from your cart.
Enter 'DONE' when you're done adding items and want to quit.
""")
    
def clear_screen():
    os.system('cls' if os.name =='nt' else 'clear')
    clear_output()
    
def add_item(a_list, item_to_add):
    item_to_add = input("What would you like to add? ")
    confirm = input("Are you sure? ")
    if confirm.upper() == 'Y':
        if item_to_add in a_list:
            confirm = input("Are you sure you want to add a duplicate? ")
            if confirm.upper() == 'N':
                pass
            elif confirm.upper() == 'Y':
                a_list.append(item_to_add)
        else:
            a_list.append(item_to_add)
    elif confirm.upper() == 'N':
        print(a_list)
        pass
    
def show_cart(a_list):
    print(f"Here are your items: ")
    new_dict = dict((i, a_list.count(i)) for i in a_list)
    for k, v in new_dict.items():
        print(f"{k} [{v}]")
        
def delete_item(a_list, item_to_delete):
    item_to_delete = input("What would you like to delete? ")
    confirm = input("Are you sure? ")
    if confirm.upper() == 'Y':
        a_list.remove(item_to_delete)
    elif confirm.upper() == 'N':
        pass
    
def clear_cart(a_list):
    del a_list[:]
	
def main():
    shopping_list = []
    instructions()
    
    while True:
        ask = input("What would you like to do? ")
        if ask.upper() == 'ADD':
            clear_screen()
            add_item(shopping_list, ask)
            show_cart(shopping_list)
        if ask.upper() == 'SHOW':
            clear_output()
            show_cart(shopping_list)
        if ask.upper() == 'DONE':
            clear_screen()
            show_cart(shopping_list)
            break
        if ask.upper() == 'REMOVE':
            clear_screen()
            delete_item(shopping_list, ask)
            show_cart(shopping_list)
        if ask.upper() == 'CLEAR':
            confirm = input("This will remove all items from your cart. Are you sure: Y/N? ")
            if confirm.upper() == 'Y':
                clear_screen()
                clear_cart(shopping_list)
                show_cart(shopping_list)
            else:
                continue
main()


# In[ ]:




