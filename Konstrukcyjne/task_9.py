import copy


class Smartphone:
    def __init__(self, model, memory, color, price):
        self.model = model
        self.memory = memory
        self.color = color
        self.price = price

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (f"Smartphone [model='{self.model}', memory='{self.memory}GB', "
                f"color='{self.color}', price={self.price} USD]")


original_smartphone = Smartphone("PhoneX", 64, "czarny", 3000)
print("Oryginalny smartfon:", original_smartphone)

cloned_smartphone = original_smartphone.clone()
cloned_smartphone.memory = 128
cloned_smartphone.color = "biały"
print("Sklonowany smartfon:", cloned_smartphone)

print("Czy oryginalny smartfon i jego klon to różne obiekty?", original_smartphone is not cloned_smartphone)
