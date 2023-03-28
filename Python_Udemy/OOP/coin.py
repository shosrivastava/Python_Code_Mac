import random

class Coin:

    def __init__(self, rare = False, heads = True, clean = True, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)


        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

        def rust(self):
            self.color = self.rusty_color

        def clean(self):
            self.color = self.clean_color
        
        def __del__(self):
            print("The coin has been spent!")

        def flip(self):
            heads_options = [True, False]
            choice = random.choice(heads_options)
            self.heads = choice

class one_rupee_coin(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_color":"Grey",
            "rusty_color":"Greenish",
            "num_of_edges": 1,
            "diameter": 22.5
        }

        super().__init__(**data)

coin1 = one_rupee_coin()

print(coin1.color)

# The code can be further modified to add other attributes as well.