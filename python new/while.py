def divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ValueError("Cannot divide by zero.")
        print("Result:", numerator / denominator)
    except ValueError as error:
        print("Error:", error)
    finally:
        print("Calculation done.")


divide(10, 2)  
divide(10, 0)  
