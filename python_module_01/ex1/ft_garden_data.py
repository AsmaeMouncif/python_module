class Plant:
    """A class representing a plant with basic attributes."""

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
        """Display information about the plant."""
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]

print("=== Garden Plant Registry ===")

for i in plants:
    i.get_info()
