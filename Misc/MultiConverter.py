import time

def convert_units(start_unit, end_unit, value):
    conversion_factors = {
        "MPH": {"KPH": 1.60934},
        "KPH": {"MPH": 0.621371},
        "Ounces": {"Grams": 28.3495},
        "Grams": {"Ounces": 0.03527396},
        "Gallons": {"Liters": 3.78541},
        "Liters": {"Gallons": 0.264172},
        "LBS": {"KGS": 0.453592},
        "KGS": {"LBS": 2.20462},
    }

    try:
        conversion_factor = conversion_factors[start_unit][end_unit]
        result = value * conversion_factor
        return result
    except KeyError:
        print("Invalid unit conversion.")
        return None


print(convert_units.keys())
start_unit = input("From: ")
end_unit = input("To: ")
value = float(input("Number: "))

converted_value = convert_units(start_unit, end_unit, value)

if converted_value is not None:
    print(converted_value)

time.sleep(0.5)
