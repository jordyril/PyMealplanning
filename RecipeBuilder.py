import os
from MyUtils.dataprocessing import save_to_pickle, open_from_pickle
from PyMealPlanning import Recipe

PATH = r"C:\Users\jordy\OneDrive\Varia\Health\Food\PyMealplanning"
recipe_folder = r"Recipes"

os.chdir(f"{PATH}")

# ================================================================================
# INITIAL START (basically only needed once at start)
# ================================================================================
filename = "Recipe_dictionary"
if not os.path.exists(f"{filename}.pickle"):
    recipe_dic = {}
    save_to_pickle(filename, recipe_dic, folder=".")
else:
    recipe_dic = open_from_pickle(filename, folder=".")

# ================================================================================
# ADD RECIPES
# ================================================================================
test = Recipe(
    name="test cereals",
    ingredients=[Milk(200), Ingredient("Nesquik cereal", Mass(30, "g"))],
    nutrient_info=NutrientInfo(203, 33, 9, 4),
)

test.to_latex(folder=recipe_folder, photo="NesquikCereal")
