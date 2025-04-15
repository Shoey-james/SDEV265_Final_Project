from model.Units import Volume, Weight

class UnitsRegistry:

    cup = Volume("cup", "cup", 1.0)
    tbsp = Volume("tablespoon", "tbsp", 1 / 16.0)
    tsp = Volume("teaspoon", "tsp", 1 / 48.0)
    fl_oz = Volume("fluid ounce", "fl oz", 1 / 8.0)

    volume_group = [cup, tbsp, tsp, fl_oz]

    oz = Weight("ounce", "oz", 1 / 16.0)
    lb = Weight("pound", "lb", 1.0)

    weight_group = [lb, oz]
    
