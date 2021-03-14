import os
from MyUtils.dataprocessing import save_to_pickle, open_from_pickle
from PyMealPlanning.Recipe import Recipe
from PyMealPlanning.Ingredient import Ingredient, Milk
from PyMealPlanning.UnitMetrics import Mass
from PyMealPlanning.Nutrient import NutrientInfo
from datetime import date
from typing import Union

# from PyMealPlanning.RecipeDictionary import RecipeDictionary

PATH = r"C:\Users\jordy\OneDrive\Varia\Health\Food\PyMealplanning"
recipe_folder = r"Recipes"

os.chdir(f"{PATH}")


# ================================================================================
# ADD RECIPES
# ================================================================================
test = Recipe(
    name="test cereals2",
    ingredients=[Milk(200), Ingredient("Nesquik cereal", Mass(30, "g"))],
    nutrient_info=NutrientInfo(203, 33, 9, 4),
)

# test.to_latex(folder=recipe_folder, photo="NesquikCereal")


recipe_dic.add_recipe(test)
recipe_dic.delete_recipe(test)
