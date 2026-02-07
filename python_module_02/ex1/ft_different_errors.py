def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    try:
        print("Testing ZeroDivisionError...")
        9 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    try:
        print("Testing KeyError...")
        d = {"plant": "rose"}
        d["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    print()

    try:
        print("Testing multiple errors together...")
        int("abc")
        9 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    garden_operations()
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print()
    test_error_types()
