from typing import Optional, Union

import pandas as pd

from PyMealPlanning.UnitMetrics import Energy, Mass, Serving

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


# ================================================================================
# NUTRIENTINFO
# ================================================================================
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
