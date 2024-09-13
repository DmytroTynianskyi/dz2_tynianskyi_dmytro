class Celsius:
    def __init__(self, temperature=0):
        # when creating the object, the setter method is called automatically
        self.temperature = temperature

    def to_fahrenheit(self):
        # convert the temperature to Fahrenheit
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value:int):
        print("Setting value...")
        # ensure the temperature does not go below absolute zero
        if value < -273.15:
            raise ValueError("Temperature below -273.15°C is not possible")
        self._temperature = value


# create an object with a valid temperature
human = Celsius(37)

# print the temperature in Celsius
print(human.temperature())

# print the temperature in Fahrenheit
print(human.to_fahrenheit())

# attempting to create an object with a temperature below -273.15°C will raise an exception
try:
    coldest_thing = Celsius(-300)
except ValueError as e:
    print(e)
