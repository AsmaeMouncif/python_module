class Plant:
    """A class representing a plant that can age and grow."""

    def __init__(self, name: str, height: int, age_days: int) -> None:
        """Initialize a Plant with name, height, and age.

        Args:
            name: The name of the plant.
            height: The height of the plant in centimeters.
            age_days: The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age_days = age_days

    def age(self) -> None:
        """Increment the plant's age by one day."""
        self.age_days += 1

    def grow(self) -> None:
        """Increment the plant's height by one centimeter."""
        self.height += 1

    def get_info(self) -> None:
        """Display information about the plant."""
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


plant = Plant("Rose", 25, 30)
initial_height = plant.height


print("=== Day 1 ===")
plant.get_info()

day = 0
while day < 6:
    plant.age()
    plant.grow()
    day += 1

print("=== Day 7 ===")
plant.get_info()

print(f"Growth this week: +{plant.height - initial_height}cm")
