class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' en ' + self.galaxy

class luna:
    pass

sun = Star("Sol", "Vía Láctea")
lunita=luna()
print(lunita)