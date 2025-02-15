import unittest
import tkinter as tk
from calculator import click_button, clear, calculate

class TestCalculator(unittest.TestCase):
    def setUp(self):

        self.root = tk.Tk()
        self.entry = tk.Entry(self.root)
        self.entry.pack()

    def tearDown(self):

        self.root.destroy()

    def test_click_button(self):

        click_button(self.entry, "1")
        self.assertEqual(self.entry.get(), "1")
        click_button(self.entry, "2")
        self.assertEqual(self.entry.get(), "12")
        click_button(self.entry, "+")
        self.assertEqual(self.entry.get(), "12+")
        click_button(self.entry, "3")
        self.assertEqual(self.entry.get(), "12+3")

    def test_clear(self):

        self.entry.insert(0, "123")
        clear(self.entry)
        self.assertEqual(self.entry.get(), "")

    def test_calculate_valid_expression(self):

        self.entry.insert(0, "2+2")
        calculate(self.entry)
        self.assertEqual(self.entry.get(), "4")

        self.entry.delete(0, tk.END)
        self.entry.insert(0, "10/2")
        calculate(self.entry)
        self.assertEqual(self.entry.get(), "5")

    def test_calculate_invalid_expression(self):

        self.entry.insert(0, "2/0")
        calculate(self.entry)
        self.assertEqual(self.entry.get(), "Ошибка")

        self.entry.delete(0, tk.END)
        self.entry.insert(0, "2+")
        calculate(self.entry)
        self.assertEqual(self.entry.get(), "Ошибка")

    def test_calculate_with_decimals(self):

        self.entry.insert(0, "2.5+2.5")
        calculate(self.entry)
        self.assertEqual(self.entry.get(), "5")

if __name__ == "__main__":
    unittest.main()