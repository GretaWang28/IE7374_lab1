# test/test_unittest.py

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, convert_all

class TestTempConverter(unittest.TestCase):
    
    def test_celsius_to_fahrenheit(self):
        """Test celsius to fahrenheit conversion."""
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)
    
    def test_fahrenheit_to_celsius(self):
        """Test fahrenheit to celsius conversion."""
        self.assertEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertEqual(fahrenheit_to_celsius(212), 100.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0, places=1)
    
    def test_celsius_to_kelvin(self):
        """Test celsius to kelvin conversion."""
        self.assertEqual(celsius_to_kelvin(0), 273.15)
        self.assertEqual(celsius_to_kelvin(100), 373.15)
        self.assertEqual(celsius_to_kelvin(-273.15), 0.0)
    
    def test_convert_all(self):
        """Test convert_all function."""
        result = convert_all(0)
        self.assertEqual(result['fahrenheit'], 32.0)
        self.assertEqual(result['kelvin'], 273.15)
        
        result = convert_all(100)
        self.assertEqual(result['fahrenheit'], 212.0)
        self.assertEqual(result['kelvin'], 373.15)

if __name__ == '__main__':
    unittest.main()
