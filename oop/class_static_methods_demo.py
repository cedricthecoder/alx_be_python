class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers, and print the class's calculation_type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
