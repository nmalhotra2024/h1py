class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        # Base fare calculation
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        # Get base fare using the parent class method
        base_fare = super().fare()
        # Add 10% extra for bus
        total_fare = base_fare + (0.10 * base_fare)
        return total_fare


# Example usage
bus = Bus(50)
print(f"Total Bus fare: {bus.fare()}")