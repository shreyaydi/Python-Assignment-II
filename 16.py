class Valorant:
    def __init__(self, name, signature,ultimate,fighting_style):
        self.name = name
        self.signature = signature
        self.ultimate = ultimate
        self.fighting_style = fighting_style

    def display(self):
        print("\n Player Name=", self.name)
        print("\n Signature Ability=", self.signature)
        print("\n Ultimate=",self.ultimate)
        print("\n Fighting Style=", self.fighting_style)

    def ultimate_power(self):
        self.ultimate = 'Blade Storm'
        print("\n Player Name=", self.name)
        print("\n Signature Ability=", self.signature)
        print("\n Ultimate=",self.ultimate)
        print("\n Fighting Style=", self.fighting_style)

info = Valorant('Jett','Tail Wind',None,'Jett has a agile and evaise fighting style')

print('Before getting ultimate power: ')
info.display()
print('\nAfter getting ultimate power: ')
info.ultimate_power()