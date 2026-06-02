def input_temperature(temp_str: str) -> int:
    print(f"Input data '{temp_str}'")
    temp = int(temp_str)
    if temp in range(0, 41):
        print(f"Temperature is now {temp}°C")
        return temp
    else:
        raise ValueError(f"Température hors plage (0-40°C) : '{temp_str}'")

def test_temperature():
    try:
        temp_valid = input_temperature("25")
    except ValueError as e:
        print(f"Echec innatendu: {e}")
    try:
        temp_invalid = input_temperature("abc")
    except ValueError as e:
        print(f"La temperature doit etre un nombre: {e}")
    input_temperature("-100")
    input_temperature("15")

if __name__ == "__main__":
    test_temperature()
    print("All tests completed - program didnt crash!")