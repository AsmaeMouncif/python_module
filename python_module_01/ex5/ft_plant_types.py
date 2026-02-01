class Plant:
    """Base class representing a plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant.

        Args:
            name: The name of the plant.
            height: The height in centimeters.
            age: The age in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """A class representing a flowering plant."""

    def __init__(
        self, name: str, height: int, age: int, color: str
    ) -> None:
        """Initialize a Flower.

        Args:
            name: The name of the flower.
            height: The height in centimeters.
            age: The age in days.
            color: The color of the flower.
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Display blooming message."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """A class representing a tree."""

    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        """Initialize a Tree.

        Args:
            name: The name of the tree.
            height: The height in centimeters.
            age: The age in days.
            trunk_diameter: The trunk diameter in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate and display the shade area provided by the tree."""
        radius_m: float = self.trunk_diameter / 10.0
        shade_area: int = int(3.14159 * radius_m * radius_m)
        print(
            f"{self.name} provides {shade_area} square meters of shade"
            )


class Vegetable(Plant):
    """A class representing a vegetable plant."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        """Initialize a Vegetable.

        Args:
            name: The name of the vegetable.
            height: The height in centimeters.
            age: The age in days.
            harvest_season: The harvest season.
            nutritional_value: The main nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def display_nutrition(self) -> None:
        """Display nutritional information."""
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    # Flowers
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 30, 20, "yellow")

    print(
        f"{rose.name} (Flower): {rose.height}cm, "
        f"{rose.age} days, {rose.color} color"
    )
    rose.bloom()
    print()

    # Trees
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 3650, 40)

    print(
        f"{oak.name} (Tree): {oak.height}cm, "
        f"{oak.age} days, {oak.trunk_diameter}cm diameter"
    )
    oak.produce_shade()
    print()

    # Vegetables
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 75, "fall", "vitamin A")

    print(
        f"{tomato.name} (Vegetable): {tomato.height}cm, "
        f"{tomato.age} days, {tomato.harvest_season} harvest"
    )
    tomato.display_nutrition()
