def water_plants(plant_list: list) -> None:
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None or not isinstance(plant, str) or len(plant) == 0:
                raise ValueError(
                    f"Error: Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")

    except ValueError as e:
        print(e)

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    try:
        print("Testing normal watering...")
        plants = ["tomato", "lettuce", "carrots"]
        water_plants(plants)
        print("Watering completed successfully!")
        print()
        print("Testing with error...")
        plants_with_error = ["tomato", None, "carrots"]
        water_plants(plants_with_error)
        print()
    finally:
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
