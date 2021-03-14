import pandas as pd
from typing import Union, Optional

# import os
import shutil

from pylatex import Document, Command
from pylatex.utils import NoEscape
from functools import total_ordering

# ================================================================================
# UNIT
# ================================================================================


@total_ordering
class UnitMetric(object):
    def __init__(self, quantity: float, unit: str) -> None:
        self.quantity = quantity
        self.unit = unit
        self._base = None

    def _rebase(self) -> None:
        self._decimal_unit_dic = {
            "k": 3,
            "d": -1,
            "M": 6,
            "h": 2,
            "da": 1,
            "c": -2,
            "G": 9,
            "": 0,
            "m": -3,
        }
        self._prefix = self.unit.split(self._base)[0]
        self._base_quantity = 10 ** self._decimal_unit_dic[self._prefix] * self.quantity

    def __eq__(self, other) -> bool:
        return self._base_quantity == other._base_quantity

    def __lt__(self, other) -> bool:
        return self._base_quantity > other._base_quantity

    def __repr__(self) -> str:
        return f"{self.quantity} {self.unit}"


class Volume(UnitMetric):
    def __init__(self, quantity: float, unit: str = "ml") -> None:
        super().__init__(quantity, unit)
        self._base = "l"
        self._rebase()


class Mass(UnitMetric):
    def __init__(self, quantity: float, unit: str = "g") -> None:
        super().__init__(quantity, unit)
        self._base = "g"
        self._rebase()


class Energy(UnitMetric):
    def __init__(self, quantity: float, unit: str = "kcal") -> None:
        super().__init__(quantity, unit)
        self._base = "cal"
        self._rebase()


class Serving(UnitMetric):
    def __init__(self, quantity: float = 1, unit: str = "Person") -> None:
        super().__init__(quantity, unit)
        self._base = "Person"

    def _rebase(self):
        pass


# ================================================================================
# NUTRIENT
# ================================================================================
class Nutrient(object):
    def __init__(self, name, metric) -> None:
        self.name = name
        self.metric = metric

    def __repr__(self) -> str:
        return self.metric


class Calories(Nutrient):
    def __init__(self, quantity: float = 1, unit: str = "kcal") -> None:
        super().__init__("Calories", Energy(quantity, unit))


class Proteins(Nutrient):
    def __init__(self, quantity: float = 1, unit: str = "g") -> None:
        super().__init__("Proteins", Mass(quantity, unit))


class Carbs(Nutrient):
    def __init__(self, quantity: float = 1, unit: str = "g") -> None:
        super().__init__("Carbs", Mass(quantity, unit))


class Fat(Nutrient):
    def __init__(self, quantity: float = 1, unit: str = "g") -> None:
        super().__init__("Fat", Mass(quantity, unit))


class NutrientInfo(object):
    def __init__(
        self,
        calories: Union[float, Calories],
        carbs: Union[float, Carbs],
        protein: Union[float, Proteins],
        fat: Union[float, Fat],
        serving: Optional[Union[Serving, float]] = 1,
    ) -> None:

        self.calories = (
            calories if isinstance(calories, Calories) else Calories(calories)
        )
        self.carbs = carbs if isinstance(carbs, Carbs) else Carbs(carbs)
        self.protein = protein if isinstance(protein, Proteins) else Proteins(protein)
        self.fat = fat if isinstance(fat, Fat) else Fat(fat)

        self.serving = serving if isinstance(serving, Serving) else Serving(serving)

        self.list_of_nutrients = [self.calories, self.carbs, self.protein, self.fat]

    @property
    def values(self):
        return [x.metric.quantity for x in self.list_of_nutrients]

    @property
    def units(self):
        return [x.metric.unit for x in self.list_of_nutrients]

    @property
    def names(self):
        return [x.name for x in self.list_of_nutrients]

    def to_df(self) -> pd.DataFrame:
        df = pd.DataFrame(index=self.names, columns=["Value", "Unit"],)
        df["Value"] = self.values
        df["Unit"] = self.units
        return df

    def to_dic(self) -> dict:
        d = {}
        for i, cat in enumerate(self.names):
            d[cat] = (self.values[i], self.units[i])
        return d


# ================================================================================
# INGREDIENTS
# ================================================================================


@total_ordering
class Ingredient(object):
    def __init__(
        self,
        name: str,
        metric: UnitMetric,
        category: str = "Varia",
        nutrient_info: Optional[NutrientInfo] = None,
        variant: Optional[str] = None,
    ) -> None:
        self.name = name
        self.metric = metric
        self.category = category

        self.variant = variant
        self.nutrient_info = nutrient_info

    def __repr__(self):
        return f"{self.name}: {self.metric}"

    def __le__(self, right):
        return self.name <= right.name

    def __eq__(self, right):
        return self.name == right.name


class Milk(Ingredient):
    def __init__(self, quantity: float, unit: str = "ml") -> None:
        super().__init__("Milk", Volume(quantity, unit), "Liquids")


# ================================================================================
# RECIPES
# ================================================================================
class PyLaTeXRecipeUtil(object):
    def __init__(self, recipe, folder="./", *args, **kwargs) -> None:
        self.recipe = recipe
        self.doc = Document(
            f"{folder}/{self._savename}",
            documentclass=Command(
                "documentclass", arguments="standalone", options="preview"
            ),
            fontenc=None,
            inputenc=None,
            font_size="normalsize",
            lmodern=False,
            textcomp=False,
            microtype=None,
            page_numbers=False,
            indent=None,
            geometry_options=None,
            data=None,
        )
        self.folder = folder

    def _add_tex_title(self, title: str) -> None:
        title_line = NoEscape("% " + 80 * "=")

        self.doc.append(title_line)
        self.doc.append(NoEscape(f"% {title}"))
        self.doc.append(title_line)

    @property
    def _savename(self) -> str:
        return "".join(self.recipe.name.title().split(" "))

    def _space(self) -> None:
        self.doc.append(NoEscape("\n"))

    def _move_pdf(self):
        # os.remove(f"{self.folder}/")
        shutil.move(
            f"{self.folder}/{self._savename}.pdf",
            f"{self.folder}/.Output/{self._savename}.pdf",
        )


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

    def _sort_ingredients(self):
        self.ingredients = sorted(self.ingredients, reverse=True)

    # @property
    # def _savename(self):
    #     return "".join(self.name.title().split(" "))

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def to_latex(self, photo=None, folder=".") -> None:
        wrapper = PyLaTeXRecipeUtil(self, folder)

        wrapper._space()

        wrapper.doc.preamble.append(Command("usepackage", "recipe"))
        wrapper._add_tex_title("Data")

        wrapper._space()
        wrapper.doc.append(Command("title", self.name))
        wrapper.doc.append(Command("serving", self.serving))

        wrapper._space()

        for var in ["calories", "protein", "fat", "carbs"]:
            wrapper.doc.append(
                Command(var, getattr(self.nutrient_info, var).metric.quantity)
            )

        wrapper._space()

        if photo:
            wrapper.doc.append(Command("photo", photo))

        wrapper._space()

        for ing in self.ingredients:
            wrapper.doc.append(
                Command("ingredient", [ing.name, ing.metric.quantity, ing.metric.unit])
            )

        wrapper._space()

        for step in self.instructions:
            wrapper.doc.append(Command("step", step))

        wrapper._add_tex_title("Doc")
        wrapper.doc.append(Command("createrecipe"))

        # wrapper.doc.generate_tex()
        wrapper.doc.generate_pdf(clean_tex=False, clean=True)

        wrapper._move_pdf()
