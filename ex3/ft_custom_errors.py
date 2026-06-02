class GardenError(Exception):
    def __init__(self, message="A general garden error occurred."):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error."):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown watering error."):
        super().__init__(message)

def errors_raising(value: str):
    if value == "wilted":
        raise PlantError("Caught Planterror: The plant has completely wilted!")
    elif value == "unknown_issue":
        raise PlantError()
    if value == "0.0":
        raise WaterError("Caught WaterError: Water level at the lowest")
    if value == "unknown_issuse":
        raise GardenError("Caught GardenError: Something bad happened in the garden")

def test_errors():
    try: errors_raising("wilted")
    except PlantError as e:
        print(f"{e}")
    try: errors_raising("0.0")
    except WaterError as e:
        print(f"{e}")
    try: errors_raising("0.0")
    except GardenError as e:
        print(f"{e}")

if __name__ == "__main__":
    test_errors()