import time

from db.config import DB


class Users(DB):
    def __init__(self, *fields):
        self.fields = fields


class Product(DB):
    def __init__(self, *fields):
        self.fields = fields





class Orders(DB):
    def __init__(self, *fields):
        self.fields = fields



class Baskets(DB):
    def __init__(self, *fields):
        self.fields = fields



user_data = {
    "user_id" : "123456765432",
    "fullname" : "Botirjon",
    "phone" : "+99875445674",
    "role" : "A",
    "password" : "1234",
    "card_number" : "1234556789012",
    "status" : "ACTIVE",
    "created_at" : time.strftime("%Y-%m-%d %H:%M:%S")
}

obj = Product().insert(**user_data)
obj = Product("fullname").select(username = "Botirjon" , password= "1234")



