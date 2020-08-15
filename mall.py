import sqlite3
basket = []



class Product():
	
	def __init__(self,name,description,category,price):
		self.name = name
		self.description = description
		self.category = category
		self.price = price
	
	def __str__(self):
		return "Name: {} \nDescription: {} \nCatagory: {} \nPrice: {}".format(self.name,self.description,self.category,self.price)
		
class Mall():
	
	def __init__(self):
		self.con = sqlite3.connect("mall.db")
		self.cursor = self.con.cursor()
		query = "CREATE TABLE IF NOT EXISTS products (NAME TEXT, DESCRIPTION TEXT, CATAGORY TEXT, PRICE FLOAT)" 
		self.cursor.execute(query)
		self.con.commit()
	
	def disconnect():
		self.con.close()
		
	def show_products(self):
		query = "SELECT * FROM products"
		self.cursor.execute(query)
		products = self.cursor.fetchall()
		print("\nALL PRODUCTS\n\n")
		if len(products) != 0:
			for i in products:
				print("\n",(products.index(i)+1),"-",i)
			
		else:
			print("There is no product left in our stocks")
		
		return products
		
	def add_product(self,product):
		
		query0 = "SELECT * FROM Products"
		self.cursor.execute(query0)
		products0 = self.cursor.fetchall()
		
		
		
		
		query = "INSERT INTO products VALUES(?,?,?,?) "
		self.cursor.execute(query,(product.name, product.description, product.category, product.price))
		self.con.commit()
		
		
		
		return products0	
		
		
	
			
	
	
	def delete_product(self,name):
		query = "DELETE FROM products WHERE name = ?"
		self.cursor.execute(query,(name,))
		self.con.commit()
		
	def search_product(self,name):
		
		liste1 = list()
		query = "SELECT * FROM products WHERE name = ?"
		self.cursor.execute(query,(name,))
		a = self.cursor.fetchall()
		
		if len(a) != 0:
			return a
		else:
			print("We are out of stock of",name)
			
		
			
	def price_sum(self):
		total = 0.0
		query = "SELECT * FROM products"
		self.cursor.execute(query)
		products3 = self.cursor.fetchall()
		
		for i in range(len(products3)):
			total += float(products3[i][3])
		print("$" + str(total))
		
	def add_basket(self,name):
		query = "SELECT * FROM products WHERE name = ?"
		self.cursor.execute(query,(name,))
		product1 = self.cursor.fetchall()
		
		if len(product1) ==0:
			print("We cannot find",name,"in our store. Please try again")
		
		elif len(product1) != 0:
			basket.append(product1)	
			return (product1)
	
	def remove_basket(self,name):
		query = "SELECT * FROM products WHERE name = ?"
		self.cursor.execute(query,(name,))
		product2 = self.cursor.fetchall()
		liste2 = list()
		liste2.append(product2[0])
		return liste2
		
	def checkout(self):
		total1 = 0
		for i in basket:
			
			total1 += i[0][3]
		print("Total price is","$" + str(total1))
