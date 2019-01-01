import random


class Sneaky:
    sneaky = True
    
    def __init__(self, sneaky=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sneaky = sneaky
        
    def hide(self, light_level):
        return self.sneaky and light_level < 10

        
class Agile:
    agile = True
    
    def __init__(self, agile=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agile = agile
        
    def evade(self):
        return self.agile and random.randint(0, 1)