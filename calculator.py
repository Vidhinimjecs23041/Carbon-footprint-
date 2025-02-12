import json

class CarbonFootprintCalculator:
    def __init__(self):
        with open("data/emission_factors.json", "r") as f:
            self.factors = json.load(f)

    def calculate_transportation(self, miles: dict) -> float:
        total = 0
        for vehicle, distance in miles.items():
            total += distance * self.factors["transportation"][vehicle]
        return total

    def calculate_diet(self, diet_type: str) -> float:
        return self.factors["diet"][diet_type] * 30  # Monthly estimate

    def calculate_energy(self, kwh: float) -> float:
        return kwh * self.factors["energy"]["electricity"]

    def total_footprint(self, transport_miles, diet_type, energy_kwh):
        transport = self.calculate_transportation(transport_miles)
        diet = self.calculate_diet(diet_type)
        energy = self.calculate_energy(energy_kwh)
        return transport + diet + energy
