class Plant:
    """A class representing a plant in the factory."""

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

    def get_info(self) -> None:
        """Display information about the created plant."""
        print(f"Created: {self.name} ({self.height}cm, {self.age_days} days)")


plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120),
]

print("=== Plant Factory Output ===")

count = 0
for i in plants:
    i.get_info()
    count += 1

print()
print(f"Total plants created: {count}")
