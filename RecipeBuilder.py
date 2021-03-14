import os
from MyUtils.dataprocessing import save_to_pickle, open_from_pickle


PATH = r"C:\Users\jordy\OneDrive\Varia\Health\Food\Mealplan"
folder = r"..\Recipes"

os.chdir(f"{PATH}/{folder}")

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
#
# ================================================================================
