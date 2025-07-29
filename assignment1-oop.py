class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self.__secret_identity = secret_identity  # Encapsulated attribute
        self.power_level = power_level

    def reveal_secret(self):
        return f"My real identity is {self.__secret_identity}"

    def power_up(self):
        self.power_level += 10
        return f"{self.name} powers up to {self.power_level}!"

    def __str__(self):
        return f"{self.name} (Power: {self.power_level})"

# Inherited class
class TechHero(Superhero):
    def __init__(self, name, secret_identity, power_level, gadget):
        super().__init__(name, secret_identity, power_level)
        self.gadget = gadget

    def use_gadget(self):
        return f"{self.name} deploys {self.gadget}!"

    # Polymorphic method override
    def power_up(self):
        self.power_level += 15  # Tech heroes get bigger boost
        return f"SYSTEM OVERDRIVE! {self.name} now at {self.power_level}"

# Usage
hero1 = Superhero("Solarflare", "Alex Johnson", 85)
hero2 = TechHero("Circuit", "Jamie Chen", 90, "Nanobot Swarm")

print(hero1.power_up())  # Solarflare powers up to 95!
print(hero2.use_gadget())  # Circuit deploys Nanobot Swarm!
print(hero2.power_up())  # SYSTEM OVERDRIVE! Circuit now at 105
print(hero1.reveal_secret())  # My real identity is Alex Johnson