def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and type errors.
    
    Args:
        numerator (float): The number to be divided.
        denominator (float): The number to divide by.
    
    Returns:
        float: The result of the division or None if an error occurs.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of dividing {num} by {denom} is {result}"
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError:
        print("Error: Both numerator and denominator must be numbers.")
    return None 
         