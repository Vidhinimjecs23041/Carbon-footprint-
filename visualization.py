import matplotlib.pyplot as plt
import json
from collections import defaultdict

def plot_footprint_breakdown(transport, diet, energy):
    labels = ["Transportation", "Diet", "Energy"]
    sizes = [
        sum(transport.values()),
        diet,
        energy
    ]
    
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Carbon Footprint Breakdown")
    plt.show()

def plot_progress(name):
    dates = []
    co2 = []
    with open("data/user_data.json", "r") as f:
        for line in f:
            data = json.loads(line)
            if data["name"] == name:
                dates.append(data["date"])
                co2.append(data["total_co2"])
    
    plt.plot(dates, co2, marker="o")
    plt.xlabel("Date")
    plt.ylabel("CO2e (kg)")
    plt.title(f"{name}'s Carbon Footprint Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
