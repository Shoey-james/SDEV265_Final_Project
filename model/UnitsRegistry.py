from Units import Volume, Weight

class UnitsRegistry:

    cup = Volume("cup", "cup", 1.0)
    tbsp = Volume("tablespoon", "tbsp", 1.0 / 16)
    tsp = Volume("teaspoon", "tsp", 1.0 / 48)
    fl_oz = Volume("fluid ounce", "fl oz", 1.0 / 8)

    volume_group = [cup, tbsp, tsp, fl_oz]

    oz = Weight("ounce", "oz", 16.0)
    lb = Weight("pound", "lb", 1.0)

    weight_group = [lb, oz]