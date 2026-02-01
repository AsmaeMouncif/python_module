class Plant:
    """Base class for all plants in the garden."""

    def __init__(self, name: str, height: int) -> None:
        """
        Initialize a plant with name and height.

        Args:
            name: The name of the plant
            height: The height of the plant in cm
        """
        self.name = name
        self.height = height

    def grow(self) -> None:
        """Increase plant height by 1cm and print growth message."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> None:
        """Display plant information."""
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """Plant that produces flowers, inherits from Plant."""

    def __init__(
        self, name: str, height: int, flower_color: str, is_blooming: bool
    ) -> None:
        """
        Initialize a flowering plant.

        Args:
            name: The name of the plant
            height: The height of the plant in cm
            flower_color: The color of the flowers
            is_blooming: Whether the plant is currently blooming
        """
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = is_blooming

    def get_info(self) -> None:
        """Display flowering plant information with bloom status."""
        state = "blooming" if self.is_blooming else "not blooming"
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.flower_color} flowers ({state})"
        )


class PrizeFlower(FloweringPlant):
    """Award-winning flowering plant, inherits from FloweringPlant."""

    def __init__(
        self,
        name: str,
        height: int,
        flower_color: str,
        is_blooming: bool,
        prize_points: int,
    ) -> None:
        """
        Initialize a prize flower.

        Args:
            name: The name of the plant
            height: The height of the plant in cm
            flower_color: The color of the flowers
            is_blooming: Whether the plant is currently blooming
            prize_points: Points awarded for this prize flower
        """
        super().__init__(name, height, flower_color, is_blooming)
        self.prize_points = prize_points

    def get_info(self) -> None:
        """Display prize flower information with prize points."""
        state = "blooming" if self.is_blooming else "not blooming"
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.flower_color} flowers ({state}), "
            f"Prize points: {self.prize_points}"
        )


class Garden:
    """Garden that contains and manages a collection of plants."""

    def __init__(self, owner: str) -> None:
        """
        Initialize a garden with an owner.

        Args:
            owner: The name of the garden owner
        """
        self.owner = owner
        self.plants = []
        self.total_plants_added = 0
        self.total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        """
        Add a plant to the garden.

        Args:
            plant: The plant to add to the garden
        """
        self.plants.append(plant)
        self.total_plants_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self) -> None:
        """Make all plants in the garden grow by 1cm each."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def garden_report(self) -> None:
        """Generate and display a comprehensive garden statistics report."""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()

        prize_count = 0
        flowering_count = 0
        plant_count = 0

        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                prize_count += 1
            elif isinstance(plant, FloweringPlant):
                flowering_count += 1
            else:
                plant_count += 1

        print(
            f"\nPlants added: {self.total_plants_added}, "
            f"Total growth: {self.total_growth}cm"
        )
        print(
            f"Plant types: {plant_count} regular, "
            f"{flowering_count} flowering, {prize_count} prize flowers"
        )


class GardenManager:
    """Manager for multiple gardens with analytics capabilities."""

    total_gardens = 0

    def __init__(self) -> None:
        """Initialize the garden manager with an empty garden list."""
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        """
        Add a garden to the manager.

        Args:
            garden: The garden to add to the manager
        """
        self.gardens.append(garden)
        GardenManager.total_gardens += 1

    class GardenStats:
        """Nested helper class for calculating garden statistics."""

        @staticmethod
        def validate_height(height: int) -> bool:
            """
            Validate if height is positive.

            Args:
                height: The height value to validate

            Returns:
                True if height is positive, False otherwise
            """
            return height > 0

        @staticmethod
        def calculate_garden_score(garden: Garden) -> int:
            """
            Calculate total score for a garden.

            The score is based on plant heights plus prize points.

            Args:
                garden: The garden to calculate score for

            Returns:
                The total score for the garden
            """
            score = 0
            for plant in garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points * 4
            return score

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """
        Create a new garden network manager.

        Returns:
            A new GardenManager instance
        """
        return cls()

    @staticmethod
    def get_total_gardens() -> int:
        """
        Get the total number of gardens managed.

        Returns:
            The total number of gardens across all managers
        """
        return GardenManager.total_gardens


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", True, 10)
    maple = Plant("Maple", 92)

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    bob_garden.plants.append(maple)

    print()

    alice_garden.grow_all_plants()
    print()

    alice_garden.garden_report()
    print()

    height_valid = GardenManager.GardenStats.validate_height(oak.height)
    print(f"Height validation test: {height_valid}")

    manager = GardenManager.create_garden_network()
    manager.add_garden(alice_garden)

    bob_garden.total_plants_added += 1
    manager.add_garden(bob_garden)

    alice_score = GardenManager.GardenStats.calculate_garden_score(
        alice_garden
    )
    bob_score = GardenManager.GardenStats.calculate_garden_score(bob_garden)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
