def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")

    if temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")

    if temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")

    print(f"Temperature {temp}°C is perfect for plants!")
    return temp


def test_temperature_input() -> None:
    test_cases = ["25", "abc", "100", "-50"]

    for temp_str in test_cases:
        print(f"Testing temperature: {temp_str}")
        try:
            check_temperature(temp_str)
        except ValueError as e:
            print(e)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature_input()
