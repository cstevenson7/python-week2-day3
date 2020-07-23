def shoppingCart():
    #clear_output()
    items = [] 
         
    while True:
        print("\nEnter what you want to do. ")
        print("The choices are: ")
        action = input("Show / Add / Delete or Quit: ")
        if action.lower() == 'quit':
            break      
        elif (action.lower()).strip() == 'show':
            if items ==[]:
                print("\nYour cart is empty")
            else: 
                print("\n")        
                print(items)    
        elif (action.lower()).strip() == 'add':
            item_name = input('\nEnter item name: ')
            items.append(item_name)
        elif (action.lower()).strip() == 'delete':
            if items ==[]:
                print("\nYour cart is empty, there is nothing to delete")
                continue
            else:
                items_delete = input("\nEnter item name an that you want to delete from your cart (this deletes all occurences) ")         
                while items_delete in items:
                    items.remove(items_delete)
        else:
            print('Your choice of what you wanted to do is not valid, please try again')
            break

shoppingCart()
