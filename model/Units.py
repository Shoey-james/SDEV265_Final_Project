from fractions import Fraction

class Units:
    def __init__(self, unit_name, abbreviation, base_size):
        self.unit_name: str = unit_name
        self.abbreviation: str = abbreviation
        self.base_size: float = base_size

    
    def to_base(self, value: float) -> float:
        return value * self.base_size

    def from_base(self, base_value:float) -> float:
        return base_value / self.base_size

    def convert_to(self, target_unit: "Units", value:float):
        base_value = self.to_base(value)
        target_unit.from_base(base_value)
        return target_unit, base_value

    """ Converts a string fraction from UI or input to a float value for conversions. """
    @staticmethod
    def to_decimal(value:str) -> float:
        value = value.strip() # Removes whitespace

        # If the fraction is a mixed fraction..
        if ' ' in value:
            whole, fraction = value.split() # Split the whole number from the fraction. Example: "1", "1.3"
            result = float(Fraction(int(whole)) + Fraction(fraction)) # Example: 1.33
        # If the fraction is a simple fraction..
        else:
            result = float(Fraction(value)) # Example: 1/3 will be 0.33
        return round(result, 2) # Rounds to two decimal places because some fractions will continue on forever.

    """ Converts the float value to a fraction for readability for the user."""   
    @staticmethod
    def to_fraction(value: float):
        # Get the value and use the built in Fraction class to convert from float to fraction
        fraction = Fraction(value).limit_denominator(8) # Limits the denominators that can be outputted to a max of 8
        # Get the whole number from the fraction by dividing the numerator from the denominator
        whole = fraction.numerator // fraction.denominator # Example: 4 // 3 = 1
        # Get the remainder of the fraction by subtracting the fraction by the whole number.
        remainder = fraction - whole # Example: Fraction of 4/3 - 1 = 1/3

        if whole == 0:
            return str(remainder)
        elif remainder == 0:
            return str(whole)
        else:
            return f"{whole} {remainder}" # Example cont: 1 1/3

class Volume(Units):
    def _init__(self, unit_type):
        self.unit_type = unit_type

class Weight(Units):
    def _init__(self, unit_type):
        self.unit_type = unit_type
    
