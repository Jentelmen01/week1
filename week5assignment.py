from abc import ABC, abstractmethod

class Scaler(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def scale(self, value):
        pass
    def describe(self, value):
        result = f"{self.name}: {value} -> {self.scale(value)}"
        return result
class InchesToCentimeters(Scaler):
    def __init__(self):
        super().__init__("InchesToCentimeters")
    def scale(self, value):
        result = round(value * 2.54, 2)
        return result
    
class GallonsToLiters(Scaler):
    def __init__(self,):
        super().__init__("GallonsToLiters")
    def scale(self, value):
        result = round(value * 3.78541, 2)
        return result
    
class MilesToKilometers(Scaler):
    def __init__(self):
        super().__init__("MilesToKilometers")
    def scale(self, value):
        result = round(value * 1.60934, 2)
        return result
    
class CustomScaler:
    def __init__(self, name, factor):
        self.name = name
        self.factor = factor
    def scale(self, value):
        result = round(value * self.factor, 2)
        return result
    def describe(self, value):
        result = f"{self.name}: {value} -> {self.scale(value)}"
        return result
    
class ScalingHistory:
    def __init__(self):
        self._entries = []
    def record(self, scaler_name, original, scaled):
        result = f"{scaler_name}: {original} -> {scaled}"
        self._entries.append(result)
    def show(self):
        for entry in self._entries:
            print(entry)

class Workshop:
    def __init__(self, name):
        self.name = name
        self.scalers = []
        self.history = ScalingHistory()
    def add_scaler(self, scaler):
        self.scalers.append(scaler)
    def scale_all(self, value):
        print(f"=== {self.name} ===")
        for scaler in self.scalers:
            dscrb = scaler.describe(value)
            print(dscrb)
            scaled_value = scaler.scale(value)
            self.history.record(scaler.name, value, scaled_value)
    def show_history(self):
        print(f"--- History for {self.name} ---") 
        self.history.show()


workshop = Workshop('Engineering Bay')
workshop.add_scaler(InchesToCentimeters())
workshop.add_scaler(GallonsToLiters())
workshop.add_scaler(MilesToKilometers())
workshop.add_scaler(CustomScaler('OuncesToGrams', 28.3495))

workshop.scale_all(10)
print()
workshop.scale_all(25)
print()
workshop.show_history()

try:
    s = Scaler('test')
except TypeError:
    print('Cannot instantiate abstract class')
