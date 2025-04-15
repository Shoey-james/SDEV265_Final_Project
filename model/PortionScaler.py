from fractions import Fraction
from model.UnitsRegistry import UnitsRegistry
from model.Units import Units, Volume, Weight

class PortionScaler:
    original_unit: str
    original_value: float
    scale_factor: int
    scaled_value: float
    unit_options: list

    def __init__(self, original_unit: str, original_value: float, scale_factor: int):
        self.original_unit = original_unit.lower()
        self.original_value = original_value
        self.scale_factor = scale_factor
        self.scaled_value = 0.0
        self.unit_options = []

    def scale_ingredient(self):
        self.scaled_value = self.original_value * self.scale_factor
        return self.scaled_value

    def get_equivalents(self) -> str:
        # Find the matching unit object from either weight or volume groups
        all_units = UnitsRegistry.volume_group + UnitsRegistry.weight_group
        # Find the unit by iterating from both groups
        from_unit = next(
            (u for u in all_units if u.unit_name == self.original_unit or u.abbreviation == self.original_unit),
            None
        )
        # If unit is not found
        if not from_unit:
            return f"{self.scaled_value} {self.original_unit}"

        # Assign unit group based on type
        if isinstance(from_unit, Volume):
            self.unit_options = UnitsRegistry.volume_group
        elif isinstance(from_unit, Weight):
            self.unit_options = UnitsRegistry.weight_group

        # Find out if there is an equivalent from the unit group
        equivalent = self.is_equal(from_unit)

        
        original_unit_value = f"{self.scaled_value} {self.original_unit}"

        # Return both the equivalent and original if available
        if equivalent:
            return f"{original_unit_value} (or {equivalent})"
        # There wasn't an equivalent so return the original unit and its value
        else:
            return original_unit_value
        
    def is_equal(self, from_unit) -> str | None:
        base_value = from_unit.to_base(self.scaled_value)

        for unit in self.unit_options:
            # Skip the original unit
            if unit.unit_name == from_unit.unit_name:
                continue

            converted = unit.from_base(base_value)
            
            if unit.base_size > from_unit.base_size and converted >= 0.125:
                return f"{round(converted, 2)} {unit.unit_name}"

        return None
