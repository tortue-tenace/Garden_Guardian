def garden_operations(operation_number: int) -> None:
    """
    0: ValueError
    1: ZeroDivisionError
    2: FileNotFoundError
    3: TypeError
    """
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("non_existent_garden_log.txt", "r")
    elif operation_number == 3:
        "tomato" + 5
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for operation_number in (0, 1, 2, 3, 4):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")

    print()
    print("Testing multi-catch with a single try block...")
    for operation_number in (0, 1):
        try:
            garden_operations(operation_number)
        except (ValueError, ZeroDivisionError) as e:
            print(f"Caught a ValueError or ZeroDivisionError: {e}")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
