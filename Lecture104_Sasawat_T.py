class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Add to", self.name, self.lastname, "'s", "cart")

customer1 = Customer()
customer1.name = "Sasawat"
customer1.lastname = "Termprayoon"
customer1.age = 26
customer1.addCart()

customer2 = Customer()
customer2.name = "Giada"
customer2.lastname = "Pairin"
customer2.age = 26
customer2.addCart()

customer3 = Customer()
customer3.name = "Domo"
customer3.lastname = "Shikaku"
customer3.age = 27
customer3.addCart()

customer4 = Customer()
customer4.name = "Chanachai"
customer4.lastname = "P"
customer4.age = 25
customer4.addCart()

customer5 = Customer()
customer5.name = "Joechow"
customer5.lastname = "Khet"
customer5.age = 25
customer5.addCart()