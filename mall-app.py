# You have to have mall.py and import it to use this.
# It's using sqlite3 for database.
# Delevopled by eLovNeQ
!#/usr/bin/python3


from mall import *
import os
import time


mall = Mall()
names = list()


print("""

**********************************************

Welcome to eLovNeQ's Mall

1- List products
2- Add product
3- Remove product
4- Search Product
5- Add to basket
6- Remove from basket
7- Checkout
8- All products's price sum
9- User guide

Press q to quit
Press c to clear the screen
**********************************************


""")

while True:
	
	inp = input("\nWhat you wanna do: ")
	
	if inp == "1":
		mall.show_products()
	
	elif inp == "2":
		
		
		name = input("Name: ")
		description = input("Description: ")		
		category = input("Category: ")
		price = float(input("Price: "))
		#new_product = Product(name,description,category,price)
		#print("Adding the products...")
		#time.sleep(1)
		#print("Product added succesfully")
		
		for i in (mall.show_products()):
			names.append(i[0])
		
		if name not in names:
			new_product = Product(name,description,category,price)
			print("Adding the products...")
			time.sleep(1)
			print("Product added succesfully")	
		
		else:
			print("\nProduct already exists")	
		
			
		
	elif inp == "3":
	
		name = input("Which product you want to remove?\n\n Name: ")
		sure = input("Are you sure Y/N ? :")
		mall.search_product(name)
		liste1 = list()
		liste1.append(mall.search_product(name))
		if liste1 != [None]:
			
			print(liste1)
		
			if sure == "Y":
				print("Deleting the product...")
				time.sleep(1)
				mall.delete_product(name)
				print("Product deleted successfully")
			
			elif sure == "N":
				print("Cancelled")
				pass
			
			else:
				print("Only type Y or N")
			
					
	elif inp == "4":
	
		name = input("Name: ")
		print("Searching in the mall...")
		time.sleep(1)
		print(mall.search_product(name))
	
	elif inp == "5":
		
		
		
		name = input("Name: ")
		mall.add_basket(name)
		
			
		if len(basket) !=0 :
			
			
			print("*****************************\nYOUR CART\n\n")
			for i in basket:
				print(i)
		elif len(basket) ==0:
			
			print("Basket is empty")	
		
		else:	
			print("Enter valid value")
	
	elif inp == "6":
		name = input("\nWhat do you wanna remove from your basket | Name: ")
		print("\n")
		ind = basket.index(mall.remove_basket(name))
		basket.pop(ind)
		
		if len(basket) != 0:
			
			for i in basket:
				print(i)
		
		elif len(basket) ==0:
			print("\nBasket is empty")
		
	
	elif inp == "7":
		mall.checkout()
	
	elif inp == "8":
		mall.price_sum()
	
	elif inp == "9":
		print("""
		USER GUIDE
		1- LIST PRODUCTS ---> If you type '1' it lists all products in our store with their name, description, category, price . 
		
		2- ADD PRODUCT ---> You just need to enter the neccessary information about the product that you wanna add. Thats all.
		
		3- REMOVE PRODUCT ---> Type the product name that you want to remove from our store.
		
		4- SEARCH PRODUCT ---> Type the name of the product you want to search.
		
		5- ADD TO BASKET ---> Type the name of the product that you want to add to cart
		
		6- REMOVE FROM BASKET --> Type the name of the product that you want to remove from your cart.
		
		7- CHECKOUT ---> Calculate the total price of your cart.
		
		8- All products's price sum ---> What happens if you buy 1 piece from each product ?
		
		9- USER GUIDE ---> Print this.
		
		q ---> QUIT
		
		c ---> Clear the screen.		
		
		""")
	
	
			
	elif inp == "c":
		os.system("clear" or "cls")
	
	elif inp == "q":
		if len(basket) != 0:
			print("You have items in your basket")
			suret = input("Do you wanna leave them ? You will lose your cart and bonuses Y/N ? :")
			
			if suret == "Y":
				print("Quiting... See you again...")
				time.sleep(1)
				break
			
			elif suret == "N":
				print("Canceling...")
				pass
			
			else:
				print("Only type Y or N")
				
		else:
			
			print("Quiting... See you again...")
			time.sleep(1)
			break
		
	
