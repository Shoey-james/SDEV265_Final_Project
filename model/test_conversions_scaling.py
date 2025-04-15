import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.PortionScaler import PortionScaler
from model.UnitsRegistry import UnitsRegistry
from model.Units import Volume, Weight



# Test: scaling 1 tablespoon by 4 (should suggest 0.25 cup)
scaler = PortionScaler(
    original_unit="tablespoon",
    original_value=1,
    scale_factor=4
)

scaled = scaler.scale_ingredient()
print("Scaled value:", scaled)

result = scaler.get_equivalents()
print("Suggested equivalent:", result)