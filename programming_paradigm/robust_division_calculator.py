def safe_divide(numerator, denominator):
    """Safely divide two numbers with error handling."""
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Attempt the division
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."