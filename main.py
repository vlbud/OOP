class IdCounter:

    def init(self):
        self.id = 0

    def inc(self):
        self.id += 1

    def get_id(self):
        return self.id


class Password:

    def init(self, passw):
        self.passw = passw

    def is_valid(self, password):
        if password == self.passw:
            return True
        else:
            return False

    def check(self):
        d = True
        if len(self.passw) <8:
            d = False
        l = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
        n = "12345678990"
        fl = False
        fn = False
        for i in l:
            if i in self.passw:
                fl = True
        for i in n:
            if i in self.passw:
                fn = True
        if fl == False or fn == False:
            d = False
        return d

class Product:
    def init(self, IdCounter1, name, price, rating):
        IdCounter1.inc()
        self.__id = IdCounter1.get_id()
        self.__name = name
        if type(price) != int and type(price) != float:
            raise TypeError("неверный тип данных атрибута price")
        if type(rating) != int:
            raise TypeError("неверный тип данных атрибута rating")
        if price < 0:
            raise ValueError("неверное значение атрибута price")
        if rating not in range(1, 6):
            raise ValueError("неверное значение атрибута rating, должно быть от 1 до 5")
        self.price = price
        self.rating = rating

    def str(self):
        return str(self.__id)+" "+self.__name

    def repr(self):
        print(self.str()+" "+str(self.price)+" "+str(self.rating))


