from functools import total_ordering
from typing import Optional

from PyMealPlanning.Nutrient import NutrientInfo
from PyMealPlanning.UnitMetrics import UnitMetric, Volume

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
