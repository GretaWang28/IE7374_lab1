# src/temp_converter.py

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Converts Celsius to Kelvin."""
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    return celsius + 273.15

def convert_all(celsius):
    """Converts Celsius to all other units."""
    return {
        'fahrenheit': celsius_to_fahrenheit(celsius),
        'kelvin': celsius_to_kelvin(celsius)
    }