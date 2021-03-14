from typing import Optional, Union

import pandas as pd

from PyMealPlanning.UnitMetrics import Energy, Mass, Serving, UnitMetric

# ================================================================================
# NUTRIENT
# ================================================================================


class Nutrient(object):
    def __init__(self, metric: UnitMetric, name=None) -> None:
        self.name = name
        self.metric = metric

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.metric == other.metric

    def __lt__(self, other) -> bool:
        self._check_equal_type(other)
        return self._base_quantity > other._base_quantity

    def __mul__(self, other: float):
        return self.__class__(other * self.metric)

    __rmul__ = __mul__

    def __add__(self, other):
        self._check_equal_type(other)
        return self.__class__(self.metric + other.metric)

    def _check_equal_type(self, other) -> None:
        if not isinstance(other, self.__class__):
            raise SyntaxError(
                f"Cannot perform this action on type {self.__class__} and {other.__class__}"
            )

    def __repr__(self) -> str:
        return f"{self.metric.__repr__()} {self.name}"


class Calories(Nutrient):
    def __init__(self, metric: Energy = Energy(1)) -> None:
        super().__init__(metric, "Calories")


class Proteins(Nutrient):
    def __init__(self, metric: Mass = Mass(1)) -> None:
        super().__init__(metric, "Proteins")


class Carbs(Nutrient):
    def __init__(self, metric: Mass = Mass(1)) -> None:
        super().__init__(metric, "Carbs")


class Fat(Nutrient):
    def __init__(self, metric: Mass = Mass(1)) -> None:
        super().__init__(metric, "Fat")


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
            calories if isinstance(calories, Calories) else Calories(Energy(calories))
        )
        self.carbs = carbs if isinstance(carbs, Carbs) else Carbs(Mass(carbs))
        self.protein = (
            protein if isinstance(protein, Proteins) else Proteins(Mass(protein))
        )
        self.fat = fat if isinstance(fat, Fat) else Fat(Mass(fat))

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

    def __repr__(self):
        return "\n".join([x.__repr__() for x in self.list_of_nutrients])

    def __mul__(self, other: float):
        return self.__class__(
            calories=other * self.calories,
            carbs=other * self.carbs,
            fat=other * self.fat,
            protein=other * self.protein,
            serving=self.serving,
        )

    __rmul__ = __mul__

    def __add__(self, other):
        self._check_equal_type(other)
        return self.__class__(
            calories=other.calories + self.calories,
            carbs=other.carbs + self.carbs,
            fat=other.fat + self.fat,
            protein=other.protein + self.protein,
            serving=self.serving + other.serving,
        )

    def _check_equal_type(self, other) -> None:
        if not isinstance(other, self.__class__):
            raise SyntaxError(
                f"Cannot perform this action on type {self.__class__} and {other.__class__}"
            )
