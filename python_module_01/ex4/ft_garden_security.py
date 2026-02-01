class SecurePlant:
    """
    A secure plant class demonstrating encapsulation principles.

    This class protects plant data using private attributes and
    controlled access through getters and setters with validation.

    Attributes:
        name (str): The public name of the plant.
        __height (int): Private attribute for plant height in cm.
        __age (int): Private attribute for plant age in days.
    """

    def __init__(self, name: str, starting_height: int,
                 starting_age: int) -> None:
        """
        Initialize a SecurePlant with validated height and age.

        Args:
            name: The name of the plant.
            starting_height: Initial height in centimeters.
            starting_age: Initial age in days.
        """
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")
        self.set_height(starting_height)
        self.set_age(starting_age)
        print()

    def get_height(self) -> int:
        """
        Get the current height of the plant.

        Returns:
            The height of the plant in centimeters.
        """
        return self.__height

    def set_height(self, height: int) -> None:
        """
        Set the plant height with validation.

        Rejects negative values to maintain data integrity.

        Args:
            height: The desired height in centimeters.
        """
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm "
                  "[REJECTED]")
            print("Security: Negative height rejected")

    def get_age(self) -> int:
        """
        Get the current age of the plant.

        Returns:
            The age of the plant in days.
        """
        return self.__age

    def set_age(self, age: int) -> None:
        """
        Set the plant age with validation.

        Rejects negative values to maintain data integrity.

        Args:
            age: The desired age in days.
        """
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days "
                  "[REJECTED]")
            print("Security: Negative age rejected")

    def get_info(self) -> None:
        """Display the current state of the plant."""
        print()
        print(f"Current plant: {self.name} "
              f"({self.__height}cm, {self.__age} days)")


print("=== Garden Security System ===")
plant = SecurePlant("Rose", 25, 30)

plant.set_height(-5)

plant.get_info()
