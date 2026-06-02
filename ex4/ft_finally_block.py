class GardenError(Exception):
    def __init__(self, message="A general garden error occurred."):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error."):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown watering error."):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name[0] != plant_name.capitalize()[0]:
        raise PlantError(f"Invalid plant name to water:  '{plant_name}'")
    print(f"Watering {plant_name}:  [OK]")


def test_watering_system(*plants: str) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError:  {e}")
        print("..  ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system("Tomato", "Lettuce", "Carrots")
    print()
    print("Testing invalid plants...")
    test_watering_system("Tomato", "lettuce")
    print()
    print("Cleanup always happens, even with errors!")
