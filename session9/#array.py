#menu
menu = (f"""
1. list products
2. add product
3. delete product
4. delete by id / index
5. exit
""")
print("Menu ", menu)

list_product = []  # Pindahkan deklarasi list_product ke luar dari loop

while True:
    user_input = input("Enter your choice: ")
    if user_input == "1":
        print("list product", list_product)
    elif user_input == "2":
        product = input("Enter product: ")
        list_product.append(product)
        print("list product", list_product)
    elif user_input == "3":
        product = input("Enter product to delete : ")
        if product in list_product:
            list_product.remove(product)
            print("Remove succes")
        else:
            print("Your input invalid")
    elif user_input == "4":
        index = (input("Enter index to delete: "))
        try:
            index = int(index)
            if 0 <= index < len(list_product):
                list_product.pop(index)
                print("Product deleted successfully!")
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid index!")
    elif user_input == "5":
        print("Exit")
        break
    else :
        print("Invalid choice!")