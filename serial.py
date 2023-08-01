"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)
    
    >>> serial 
    <SerialGenerator start=100 next=101>

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.serial_number = start

    def __repr__(self) -> str:
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"
    
    def generate(self):
        self.serial_number += 1
        return self.serial_number - 1
    
    def reset(self):
        self.serial_number = self.start