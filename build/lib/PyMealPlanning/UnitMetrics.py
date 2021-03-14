from functools import total_ordering


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
