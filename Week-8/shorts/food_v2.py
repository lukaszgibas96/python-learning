# exercise from shorts - class methods and class variables

class Food:

    base_hearts = 1 
     
    def __init__(self, ingredients):

        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)
    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts 
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1

        return hearts
        
         

def main():
    mushroom_skewer = Food(ingredients = ["Mushroom","Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")

main()