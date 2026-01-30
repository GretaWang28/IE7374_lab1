# test/test_pytest.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, convert_all

def test_celsius_to_fahrenheit():
    """Test celsius to fahrenheit conversion."""
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(-40) == -40.0

def test_fahrenheit_to_celsius():
    """Test fahrenheit to celsius conversion."""
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0
    assert round(fahrenheit_to_celsius(98.6), 1) == 37.0

def test_celsius_to_kelvin():
    """Test celsius to kelvin conversion."""
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(100) == 373.15
    assert celsius_to_kelvin(-273.15) == 0.0

def test_convert_all():
    """Test convert_all function."""
    result = convert_all(0)
    assert result['fahrenheit'] == 32.0
    assert result['kelvin'] == 273.15
    
    result = convert_all(100)
    assert result['fahrenheit'] == 212.0
    assert result['kelvin'] == 373.15