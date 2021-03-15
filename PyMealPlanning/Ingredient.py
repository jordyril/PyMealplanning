from functools import total_ordering
from typing import Optional, Union

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

    def __mul__(self, other: float):
        return self.__class__(
            name=self.name,
            metric=other * self.metric,
            category=self.category,
            nutrient_info=other * self.nutrient_info if self.nutrient_info else None,
            variant=self.variant,
        )

    __rmul__ = __mul__

    def __add__(self, other):
        self._check_equal_type(other)
        return self.__class__(
            name=self.name,
            metric=other.metric + self.metric,
            category=self.category,
            nutrient_info=None,
            variant=self.variant,
        )

    def _check_equal_type(self, other) -> None:
        if not isinstance(other, self.__class__):
            raise SyntaxError(
                f"Cannot perform this action on type {self.__class__} and {other.__class__}"
            )
        if not self.__eq__(other):
            raise ValueError(
                f"Cannot perform this action on different ingredients, {self.name} and {other.name}"
            )


class Milk(Ingredient):
    def __init__(
        self,
        metric: Union[Volume, float] = Volume(1),
        name="Milk",
        category="Liquids",
        *args,
        **kwargs,
    ) -> None:
        metric = metric if isinstance(metric, Volume) else Volume(metric)
        super().__init__(name=name, metric=metric, category=category, *args, **kwargs)
