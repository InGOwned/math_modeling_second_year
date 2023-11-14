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

system = StarSystem(['planet1', 'planet2', 'planet3'], 'StarSystem1')
print(len(system))

system_1 = StarSystem(['planet_1'], 'System_1')
system_1 = system_1 + 'planet_2'
print(system_1.planets)

system_1 = 'planet_3' + system_1
print(system_1.planets)

system_1 = StarSystem(['planet_1'], 'System_1')
system_1 += 'planet_2'
print(system_1.planets)
