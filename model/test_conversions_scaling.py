import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.PortionScaler import PortionScaler
from model.UnitsRegistry import UnitsRegistry
from model.Units import Volume, Weight



# Test: scaling 1 tablespoon by 4 (should suggest 0.25 cup)
print("Test one: Scaling 1 tablespoon to 4.")
scaler = PortionScaler(
    original_unit="tablespoon",
    original_value=1,
    scale_factor=4
)

scaled = scaler.scale_ingredient()
print("Scaled value:", scaled)

result = scaler.get_equivalents()
print("Suggested equivalent:", result)

# Test: All Volume Units
print("Test two: All volume units")
for unit in UnitsRegistry.volume_group:
    scaler = PortionScaler(unit.unit_name, 1, 4)
    scaler.scale_ingredient()
    print(f"{unit.unit_name} → {scaler.get_equivalents()}")

# Test: Skipping small values
print("Test three: skip small values")
scaler = PortionScaler("cup", 1, 0.1)  # 0.1 cup = 1.6 tbsp
scaler.scale_ingredient()
assert "tablespoon" not in scaler.get_equivalents()  # filtered out

# Test: No Equivalents
print("Test four: No equivalents.")
scaler = PortionScaler("cup", 1, 1)
scaler.scale_ingredient()
assert "cup" in scaler.get_equivalents()
assert "or" not in scaler.get_equivalents()  # no better suggestion
