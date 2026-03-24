# 💧 Smart Water Quality Monitoring System (Software Simulation)

import random
import time
from datetime import datetime

class WaterQualitySystem:

```
def __init__(self):
    self.history = []

def generate_sensor_data(self):
    """Simulate sensor readings"""
    data = {
        "pH": round(random.uniform(6.0, 9.0), 2),
        "turbidity": round(random.uniform(1, 10), 2),
        "temperature": round(random.uniform(20, 35), 2),
        "time": datetime.now().strftime("%H:%M:%S")
    }
    return data

def analyze_water(self, data):
    """Analyze water quality based on parameters"""
    if 6.5 <= data["pH"] <= 8.5 and data["turbidity"] < 5:
        return "SAFE"
    else:
        return "NOT SAFE"

def display_report(self, data, status):
    """Display formatted output"""
    print("\n========== Water Quality Report ==========")
    print(f"Time         : {data['time']}")
    print(f"pH Level     : {data['pH']}")
    print(f"Turbidity    : {data['turbidity']} NTU")
    print(f"Temperature  : {data['temperature']} °C")
    print("------------------------------------------")
    print(f"Water Status : {status}")
    print("==========================================")

def save_history(self, data, status):
    """Store readings for future analysis"""
    record = data.copy()
    record["status"] = status
    self.history.append(record)

def show_summary(self):
    """Show summary of all readings"""
    print("\n====== Summary ======")
    total = len(self.history)
    safe_count = sum(1 for r in self.history if r["status"] == "SAFE")

    print(f"Total Readings : {total}")
    print(f"Safe Water     : {safe_count}")
    print(f"Unsafe Water   : {total - safe_count}")
    print("=====================")

def run(self):
    """Main loop"""
    print("Starting Smart Water Quality Monitoring System...\n")

    try:
        while True:
            data = self.generate_sensor_data()
            status = self.analyze_water(data)

            self.display_report(data, status)
            self.save_history(data, status)

            time.sleep(5)

    except KeyboardInterrupt:
        print("\n\nSystem stopped by user.")
        self.show_summary()
```

# Run the system

if **name** == "**main**":
system = WaterQualitySystem()
system.run()
