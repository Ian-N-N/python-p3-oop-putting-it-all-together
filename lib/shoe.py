#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        # Note: condition is NOT set here, created only after repair

    # brand property
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or not value.strip():
            print("Brand must be a non-empty string.")
            self._brand = "Unknown"
        else:
            self._brand = value.strip()

    # size property
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            print("size must be an integer")
            self._size = 0
        elif value <= 0:
            print("size must be a positive integer")
            self._size = 0
        else:
            self._size = value

    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    def __str__(self):
        cond = getattr(self, "condition", "Unknown")  # fallback if not repaired yet
        return f"{self.brand} shoe of size {self.size}, condition: {cond}"
