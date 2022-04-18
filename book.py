"""
@author: Mohamed Jalat
"""

class Book :
    name=""
    listBook=[]

    def __init__(self, name):
        self.name=name


    def insert_buy(self,quantity, price):
        id=len(Book.listBook)+1
        typeTransac="BUY"
        ordername=order(typeTransac,quantity,price,id)
        Book.listBook.append(ordername)
        print(f"--- Insert {ordername} on {self.name}")
        Book.ShowBook(self)
        return True



    def insert_sell(self,quantity, price):
        id=len(Book.listBook)+1
        typeTransac="SELL"
        ordername=order(typeTransac,quantity,price,id)
        print(f"--- Insert {ordername} on {self.name}")
        quantity=Book.ComparePreviousTransac(self,quantity,price)
        ordername=order(typeTransac,quantity,price,id)
        Book.listBook.append(ordername)
        Book.ShowBook(self)
        return f"--- Insert {order} on {self.name}"

    def ShowBook(self):
        Book.listBook=Book.SortList(self)
        print(f"Book on {self.name}")
        for i in range(len(Book.listBook)):
            if (Book.listBook[i].quantity!=0):
                print(f"        {str(Book.listBook[i])}")
        print("-------------------------")
        return True

    def SortList(self):
        sell=[]
        buy=[]
        for order in self.listBook:
            if(order.typeTransac=="SELL"):
                sell.append(order)
            else:
                buy.append(order)
        self.listBook=[]
        sell.sort(key=lambda Book : Book.price,reverse=True)
        buy.sort(key=lambda Book : Book.price,reverse=True)
        for order in sell:
            self.listBook.append(order)
        for order in buy:
            self.listBook.append(order)
        return self.listBook

    def ComparePreviousTransac(self,quantité,prix):
        compteurinter=0
        for order in self.listBook :
            compteurinter=0
            if (quantité>0):
                if(order.price >= prix and order.typeTransac=="BUY"):
                    while(quantité>0 and order.quantity>0):
                        order.quantity=order.quantity-1
                        quantité=quantité-1
                        compteurinter+=1
                if compteurinter!=0:
                    print(f"Execute {compteurinter} at {order.price} on {self.name}")
        return quantité

                
class order:

    def __init__(self, typeTransac, quantity, price,id):
        self.typeTransac=typeTransac
        self.quantity=quantity
        self.price=price
        self.id=id

    def __str__(self):
        return f"{self.typeTransac}   {self.quantity}@{self.price}   id={self.id}"
