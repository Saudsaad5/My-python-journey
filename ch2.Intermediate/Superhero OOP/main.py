from superhero import Superhero




superhero1 = Superhero("Bruce Wayne", "Batman", "Riches and Gadgets", "Gotham City")

superhero2 = Superhero("Clark Kent", "Superman", "Flight and Super Strength", "Metropolis")

superhero3 = Superhero("Diana Prince", "Wonder Woman", "Superhuman Strength and Agility", "Themyscira")


print(superhero1.name)
print(superhero1.alias)
print(superhero1.superpower)
print(superhero1.city)


superhero1.use_power()
superhero2.change_identity("Diana of Themyscira")
superhero3.reveal_identity()
superhero3.describe()