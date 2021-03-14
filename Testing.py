import os
from pylatex import Document, Command
from pylatex.utils import NoEscape

os.chdir(r"C:\Users\jordy\OneDrive\Varia\Health\Food\Mealplan")
recipe_folder = r"../Recipes"

from classes import Recipe, Ingredient, NutrientInfo, Milk, Mass


# ================================================================================
# TESTING CLASSES
# ================================================================================


test = Recipe(
    name="test cereals",
    ingredients=[Milk(200), Ingredient("Nesquik cereal", Mass(30, "g"))],
    nutrient_info=NutrientInfo(203, 33, 9, 4),
)

test.to_latex(folder=recipe_folder, photo="NesquikCereal")

