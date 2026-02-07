class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self):
        self.plants = []
        self.watering_system_open = False

    def add_plant(
        self,
        plant_name: str,
        water_level: int = 0,
        sunlight_hours: int = 0
    ) -> None:
        if (plant_name is None or
                not isinstance(plant_name, str) or
                len(plant_name) == 0):
            raise PlantError(
                "Error adding plant: Plant name cannot be empty!"
            )

        plant = Plant(plant_name, water_level, sunlight_hours)
        self.plants.append(plant)
        print(f"Added {plant_name} successfully")

    def water_plants(self, water_amounts: dict = None) -> None:
        print("Opening watering system")
        self.watering_system_open = True

        try:
            for plant in self.plants:
                if water_amounts and plant.name in water_amounts:
                    water_level = water_amounts[plant.name]

                    if water_level < 1 or water_level > 10:
                        if water_level < 1:
                            raise WaterError(
                                f"Error watering plant: Water amount "
                                f"{water_level} is too low (min 1)"
                            )
                        else:
                            raise WaterError(
                                f"Error watering plant: Water amount "
                                f"{water_level} is too high (max 10)"
                            )

                    plant.water_level = water_level
                    print(f"Watering {plant.name} - success")
        finally:
            self.watering_system_open = False
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str) -> str:
        plant = None
        for p in self.plants:
            if p.name == plant_name:
                plant = p
                break

        if plant is None:
            raise PlantError(f"Plant {plant_name} not found in garden")

        if plant.water_level < 1 or plant.water_level > 10:
            if plant.water_level < 1:
                raise WaterError(
                    f"Error checking {plant.name}: Water level "
                    f"{plant.water_level} is too low (min 1)"
                )
            else:
                raise WaterError(
                    f"Error checking {plant.name}: Water level "
                    f"{plant.water_level} is too high (max 10)"
                )

        if plant.sunlight_hours < 2 or plant.sunlight_hours > 12:
            if plant.sunlight_hours < 2:
                raise PlantError(
                    f"Error checking {plant.name}: Sunlight hours "
                    f"{plant.sunlight_hours} is too low (min 2)"
                )
            else:
                raise PlantError(
                    f"Error checking {plant.name}: Sunlight hours "
                    f"{plant.sunlight_hours} is too high (max 12)"
                )

        return (
            f"{plant.name}: healthy "
            f"(water: {plant.water_level}, sun: {plant.sunlight_hours})"
        )


def water_check() -> None:
    raise GardenError("Not enough water in tank")


def test_garden_management() -> None:
    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 0, 8)
    except PlantError as e:
        print(e)

    try:
        garden.add_plant("lettuce", 0, 6)
    except PlantError as e:
        print(e)

    try:
        garden.add_plant("", 0, 6)
    except PlantError as e:
        print(e)

    print()
    print("Watering plants...")
    try:
        garden.water_plants({"tomato": 5, "lettuce": 7})
    except WaterError as e:
        print(e)

    for plant in garden.plants:
        if plant.name == "lettuce":
            plant.water_level = 15

    print()
    print("Checking plant health...")
    try:
        health_status = garden.check_plant_health("tomato")
        print(health_status)
    except (PlantError, WaterError) as e:
        print(e)

    try:
        health_status = garden.check_plant_health("lettuce")
        print(health_status)
    except (PlantError, WaterError) as e:
        print(e)

    print()
    print("Testing error recovery...")
    try:
        water_check()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    print()
    test_garden_management()
