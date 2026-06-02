def input_temperature(temp_str: str) -> int:
    print(f"Input data '{temp_str}'")
    temp = int(temp_str)
    return print(f"Temperature is now {temp}°C")

def test_temperature():
    try:
        temp_valid = input_temperature("25")
    except ValueError as e:
        print(f"Echec innatendu: {e}")
    try:
        temp_invalid = input_temperature("abc")
    except ValueError as e:
        print(f"La temperature doit etre un nombre: {e}")

if __name__ == "__main__":
    test_temperature()
    print("All tests completed - program didnt crash!")