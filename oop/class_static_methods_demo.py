class Calculator:
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(x,y):
        return x + y 
    
    @classmethod
    def multiply(cls, x,y):
        print(f"Performing {cls.calculation_type}")
        return x * y 
    
