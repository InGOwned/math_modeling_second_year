class Planet:
    def init(self, name, radius, mass):
        self.name = name
        self.radius = radius
        self.mass = mass

    @staticmethod
    def description():
        return "Этот класс нужен для того, чтобы создавать планеты разного радиуса и объёма"
    
    @classmethod
    def gravitational_force(cls, mass1, mass2, distance):
        G = 6.6743 * 10**(-11)
        force = G * mass1 * mass2 / distance**2
        return force

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        self.name = value

    @property
    def radius(self):
        return self.radius
    
    @radius.setter
    def radius(self, value):
        self.radius = value

    @property
    def mass(self):
        return self.mass

    @mass.setter
    def mass(self, value):
        self.mass = value