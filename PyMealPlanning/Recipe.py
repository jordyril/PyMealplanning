from pylatex import Command
from typing import Union, Optional

from PyMealPlanning.Ingredient import Ingredient
from PyMealPlanning.Nutrient import NutrientInfo
from PyMealPlanning.UnitMetrics import Serving
from PyMealPlanning.utils import PyLaTeXRecipeUtil

# ================================================================================
# RECIPES
# ================================================================================


# @total_ordering
class Recipe(object):
    def __init__(
        self,
        name: str,
        ingredients: Union[list, Ingredient],
        nutrient_info: NutrientInfo,
        prep_time: Optional[float] = 1,
        prep_time_unit: Optional[str] = "min",
        serving: Union[float, Serving] = 1,
        tag: Union[str, list] = ["Breakfast", "Lunch", "Dinner"],
        score: float = 5,
        instructions: Union[str, list] = "Mix everything and Enjoy!",
    ) -> None:

        self.name = name
        self.ingredients = (
            ingredients if isinstance(ingredients, list) else [ingredients]
        )
        self.nutrient_info = nutrient_info
        self.serving = serving if isinstance(serving, Serving) else Serving(serving)
        self.tags = tag if isinstance(tag, list) else [tag]
        self.prep_time = prep_time
        self.prep_time_unit = prep_time_unit
        self.instructions = (
            instructions if isinstance(instructions, list) else [instructions]
        )
        self.score = score

        # methods
        self._sort_ingredients()

    def _sort_ingredients(self) -> None:
        self.ingredients = sorted(self.ingredients, reverse=True)

    def __eq__(self, other) -> bool:
        pass

    def __lt__(self, other) -> bool:
        pass

    def to_latex(self, photo=None, folder=".") -> None:
        wrapper = PyLaTeXRecipeUtil(self, folder)

        wrapper.recipe_to_latex(photo=photo)
        # wrapper._space()

        # wrapper.doc.preamble.append(Command("usepackage", "recipe"))
        # wrapper._add_tex_title("Data")

        # wrapper._space()
        # wrapper.doc.append(Command("title", self.name))
        # wrapper.doc.append(Command("serving", self.serving))

        # wrapper._space()

        # for var in ["calories", "protein", "fat", "carbs"]:
        #     wrapper.doc.append(
        #         Command(var, getattr(self.nutrient_info, var).metric.quantity)
        #     )

        # wrapper._space()

        # if photo:
        #     wrapper.doc.append(Command("photo", photo))

        # wrapper._space()

        # for ing in self.ingredients:
        #     wrapper.doc.append(
        #         Command("ingredient", [ing.name, ing.metric.quantity, ing.metric.unit])
        #     )

        # wrapper._space()

        # for step in self.instructions:
        #     wrapper.doc.append(Command("step", step))

        # wrapper._add_tex_title("Doc")
        # wrapper.doc.append(Command("createrecipe"))

        # wrapper.doc.generate_pdf(clean_tex=False, clean=True)

        # wrapper._move_pdf()
