def garden_operations(operation_number):
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


def test_error_types():
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"[Caught ValueError]: Bad data provided to int(). Details: {e}")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"[Caught ZeroDivisionError]: Attempted to divide by zero. Details: {e}")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"[Caught FileNotFoundError]: Tried opening a missing file. Details: {e}")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"[Caught TypeError]: Invalid type mixing attempted. Details: {e}")
    for op in [0, 1]:
        try:
            print(f"Executing operation {op} inside the multi-catch block...")
            garden_operations(op)
        except (ValueError, ZeroDivisionError) as e:
            print(f"  [Multi-Catch Triggered]: Safely intercepted a ValueError or ZeroDivisionError!")

if __name__ == "__main__":
    test_error_types()