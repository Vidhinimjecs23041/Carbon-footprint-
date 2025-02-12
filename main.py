from calculator import CarbonFootprintCalculator
import visualization as vis
import json
from datetime import datetime

def get_user_input():
    print("\n=== Carbon Footprint Calculator ===")
    transport = {}
    transport["car"] = float(input("Miles driven by car this month: "))
    transport["bus"] = float(input("Miles by bus: "))
    transport["train"] = float(input("Miles by train: "))
    transport["plane"] = float(input("Miles by plane: "))

    diet = input("Diet type (meat_lover/vegetarian/vegan): ")
    energy = float(input("Household electricity usage (kWh): "))
    return transport, diet, energy

def save_user_data(name, total):
    data = {
        "name": name,
        "total_co2": round(total, 2),
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    with open("data/user_data.json", "a") as f:
        json.dump(data, f)
        f.write("\n")

def main():
    name = input("Enter your name: ")
    transport, diet, energy = get_user_input()
    
    calculator = CarbonFootprintCalculator()
    total = calculator.total_footprint(transport, diet, energy)
    
    print(f"\n{name}, your monthly carbon footprint: {total:.2f} kg CO2e")
    vis.plot_footprint_breakdown(transport, diet, energy)
    
    save_user_data(name, total)
    vis.plot_progress(name)

if __name__ == "__main__":
    main()
