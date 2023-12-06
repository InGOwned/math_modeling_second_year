class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __len__(self):
        return len(self.planets)
        
    def __add__(self, other):
        planets_1 = self.planets.copy()
        planets_1.append(other)
        return StarSystem(planets_1, self.name)
    
    def __radd__(self, other):
        planets_1 = self.planets.copy()
        planets_1.insert(0, other)
        return StarSystem(planets_1, self.name)
    
    def __iadd__(self, other):
        self.planets.append(other)
        return self

    def __sub__(self, other):
        if other in self.planets:
            self.planets.remove(other)
        return self

    def __rsub__(self, other):
        if other in self.planets:
            self.planets.remove(other)
        return self

    def __isub__(self, other):
        if other in self.planets:
            self.planets.remove(other)
        return self


solar_system = StarSystem(['Mercury', 'Venus', 'Earth', 'Mars'], 'Solar System')

# __sub__
solar_system = solar_system - 'Mercury'
print(solar_system.planets)

# __rsub__
solar_system = 'Earth' - solar_system
print(solar_system.planets)

# __isub__
new_system = ['Mercury', 'Venus', 'Earth']
for planet in new_system:
    solar_system -= planet

print(solar_system.planets)