class Weapon:
    def __init__(self, name, description, weapon_type):
        self.name = name
        self.description = description
        self.weapon_type = weapon_type
    
    def __str__(self):
        return f'{self.name} ({self.weapon_type}): {self.description}'


class AutoRifle(Weapon):
    def __init__(self, name, description, rpm, weapon_type):
        super().__init__(name, description, weapon_type)
        self.rpm = rpm
    
    def __str__(self):
        return f'{self.name} ({self.rpm} RPM, {self.weapon_type}): {self.description}'


class HandCannon(Weapon):
    def __init__(self, name, description, mag_size, weapon_type):
        super().__init__(name, description, weapon_type)
        self.mag_size = mag_size
    
    def __str__(self):
        return f'{self.name} ({self.mag_size} rounds, {self.weapon_type}): {self.description}'


class PulseRifle(Weapon):
    def __init__(self, name, description, burst_count, weapon_type):
        super().__init__(name, description, weapon_type)
        self.burst_count = burst_count
    
    def __str__(self):
        return f'{self.name} ({self.burst_count}-burst, {self.weapon_type}): {self.description}'


class ScoutRifle(Weapon):
    def __init__(self, name, description, zoom, weapon_type):
        super().__init__(name, description, weapon_type)
        self.zoom = zoom
    
    def __str__(self):
        return f'{self.name} (Zoom {self.zoom}, {self.weapon_type}): {self.description}'

