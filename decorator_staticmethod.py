class Planet:
    @staticmethod
    def is_big_planet(diameter):
        if diameter > 10000:
            return True
        return False

Planet.is_big_planet(100)
