import json
import os

class FruitMarket:
    def __init__(self, filename='stock.json'):
       self.filename = filename
       self.stock = self.load_stock()


    def load_stock(self):
           if os.path.exists(self.filename):
                  with open(self.filename, 'r') as file:
                         return json.load(file)
       
           return{}
    
    def save_stock(self):
           with open(self.filename, 'w') as file:
                  json.dump(self.stock, file, indent=4)


    def add_stock(self,fruit,quantity,price):
              if fruit in self.stock:
                     self.stock[fruit] ['quantity'] += quantity
                     self.stock[fruit] ['price'] = price

              else:
                     self.stock[fruit] = {'quantity in kg' : quantity, 'price': price}

              self.save_stock()       
              print(f"{quantity} kg of {fruit} added to our stock.")



    def view_stock(self):
              if self.stock:
                      print("Current Fruit Stock")
                      for fruit, details in self.stock.items():
                            print(f"{fruit}: {details['quantity in kg']} kg ₹{details['price']} per kg")

              else:
                     print("No Stock Available\n Check After Sometime")
                           
    def update_stock(self):
                     
       fruit = input("Enter Fruit name to update: ").capitalize()
       if fruit in self.stock:
              print(f"Current Details of {fruit}: quantity = {self.stock[fruit]['quantity in kg']} kg, price = {self.stock[fruit]['price']} per kg")
              new_quantity = int(input(f"Enter new quantity for {fruit}: "))
              new_price = int(input("Enter new price for {fruit}: "))

              self.stock[fruit]['quantity'] = new_quantity
              self.stock[fruit]['fruit'] = new_price
              self.save_stock()
              print(f"{fruit} stock Updated Succesfully")

       else:
              print(f"{fruit} not found in stock")



    def buy_fruit(self):
            fruit = input("Enter Fruit Name to Buy: ").capitalize()

            if fruit in self.stock:
                print(f"{fruit}: {self.stock[fruit]['quantity in kg']} @ kg ₹{self.stock[fruit]['price']}/kg")


            try:
              qty = int(input(f"Enter how many kg of {fruit} do you want?: (eg 0.5 means 500gm" ))

            except ValueError:
                print("Invalid Input. Please Enter a number in kg like this 0.5 means 500Ggm.")
                

                if qty <= self.stock[fruit]['quantity in kg']:
                        total = qty * self.stock[fruit]['price']
                        self.stock[fruit]['quantity in kg'] -= qty
                        print(f"Total Price: ₹{total}.\nThank You for Your Purchase!")
                        self.save_stock()

                else:
                        print("Sorry not enough quantity is available")

            else:
                print(f"{fruit} is not available")



class Manager(FruitMarket):
    def __init__(self, market):
        self.market = market


    def manager_menu(self):
          while True:
                print(f"\n--------Manager Menu------------")
                print(f"1. Add Fruit Stock")
                print(f"2. View Fruit Stock")
                print(f"3. Update Fruit Stock")
                print(f"4. Existing Fruit Market")

                choice = int(input("Enter Your Choice here: "))

                if choice ==1:
                      
                      fruit = input("Enter Fruit Name to add: ").capitalize()
                      quantity = int(input("Enter quantity in  Kg : "))
                      price = int(input("Enter price for (in kg): "))
                      self.market.add_stock(fruit, quantity,price)

                elif choice ==2:
                       self.market.view_stock()

                elif choice ==3:
                       fruit = input("Enter Fruit Name: ").capitalize()
                       quantity = int(input("Enter Fruit Qty: "))
                       price = int(input("Enter New Price per kg: "))
                       self.market.update_stock()

                elif choice ==4:
                       print("Existing Manager Menu.")
                       break
                else:
                       print("Error: Invalid Choice. try again")
                       break 
                

class Customer:
       def __init__(self, market):
              self.market = market

       def customer_menu(self):
              while True:
                     print(f"***********Customer Menu*************")
                     print(f"1. View Fruit Stock")
                     print(f"2. Buy Fruit")
                     print(f"3. Exist")

                     choice = int(input("Enter Your Choice: "))

                     if choice ==1:
                            self.market.view_stock()

                     elif choice==2:
                            self.market.buy_fruit()

                     elif choice==3:
                            print("----------------Thank You For Visiting Fruit Market------------")
                            break
                     else:
                            print("Error: Invalid Choice\n Try Again")
                            break

def manager_login():
       username = input("Enter Manager's User Name: ")
       Password = input("Enter Password: ")

       if username == "admin" and Password == "Fruit1234":
              print("\n Login Successful")
              return True
       else:
              print("Unauthorized Access: Login Failed\n Try Again")
              return False
       

if __name__ == "__main__":
       market = FruitMarket()
       manager = Manager(market)
       customer = Customer(market)


       print("\n--------Welcome To Fruit Market------------")
       print("1. For Manager")
       print("2. For Customer")

       role = int(input("Enter Your Role (1 or 2): "))

       if role ==1:
              if manager_login():
                     manager.manager_menu()

              else:
                     print("Existing Due to Failed Login")

       elif role ==2:
              customer.customer_menu()

       else:
              print("Invalid Role Selection")