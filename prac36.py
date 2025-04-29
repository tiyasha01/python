#create class order which stores item & its price.Use dunder function __gt__()to convey
#order1>order2 if price of order1>price of order2
class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price>ord2.price

ord1=order("chips",20)
ord2=order("tea",15)
print(ord1>ord2)