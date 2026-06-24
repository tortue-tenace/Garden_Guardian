class GardenError(Exception):
    def __init__(
        self, message: str = "A general garden error occurred."
    ) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error.") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown watering error.") -> None:
        super().__init__(message)


def errors_raising(value: str) -> None:
    if value == "wilted":
        raise PlantError("The tomato plant is wilting!")
    elif value == "unknown_plant":
        raise PlantError()
    elif value == "empty_tank":
        raise WaterError("Not enough water in the tank!")
    elif value == "unknown_water":
        raise WaterError()
    else:
        raise GardenError("Something bad happened in the garden")


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        errors_raising("wilted")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        errors_raising("empty_tank")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    for value in ("wilted", "empty_tank"):
        try:
            errors_raising(value)
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
