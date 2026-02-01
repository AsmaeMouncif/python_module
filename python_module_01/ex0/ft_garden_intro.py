def show_info() -> None:
    """Display information about a plant."""
    name: str = "Rose"
    height: int = 25
    age: int = 30

    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    show_info()
    print()
    print("=== End of Program ===")
