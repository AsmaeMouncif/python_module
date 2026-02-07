def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> str:
    if (plant_name is None or not isinstance(plant_name, str) or
            len(plant_name) == 0):
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1 or water_level > 10:
        if water_level < 1:
            raise ValueError(
                f"Error: Water level {water_level} is too low (min 1)"
            )
        else:
            raise ValueError(
                f"Error: Water level {water_level} is too high (max 10)"
            )
    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours < 2:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        else:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too high "
                f"(max 12)"
            )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("Testing good values...")
    try:
        result: str = check_plant_health("tomato", 5, 6)
        print(result)
    except ValueError as e:
        print(f"{e}")
    print()
    print("Testing empty plant name...")
    try:
        result: str = check_plant_health("", 5, 6)
        print(result)
    except ValueError as e:
        print(f"{e}")
    print()
    print("Testing bad water level...")
    try:
        result: str = check_plant_health("rose", 15, 6)
        print(result)
    except ValueError as e:
        print(f"{e}")
    print()
    print("Testing bad sunlight hours...")
    try:
        result: str = check_plant_health("cactus", 5, 0)
        print(result)
    except ValueError as e:
        print(f"{e}")
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    print()
    test_plant_checks()
