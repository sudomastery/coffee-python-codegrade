class Customer:
    #delcare internal variable
    _everything = []

    def __init__(self,name):
        self.name = name
        Customer._everything.append(self) #add instance to internal variable


    #treat method as attribute
    @property
    def name (self):
        return self.name
    
    #set value of property
    
    @name.setter
    def name(self, value):

        #check if string lenght is between 1 and 15 characters
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(value) <=15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value


        #to declare other methods
        def orders(self)
            return [order for order in Order.all() if order.customer == self]
        def coffees(self):
            from coffee import Coffee