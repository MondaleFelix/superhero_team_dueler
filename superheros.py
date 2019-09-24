import random

class Ability:

	def __init__(self, name , max_damage):
		self.name = name
		self.max_damage = max_damage

	def attack(self):
		attack_value = random.randint(0, self.max_damage)
		return attack_value 



class Armor:

	def __init__(self, name, max_block):
		self.name = name
		self.max_block = max_block

	def block(self):
		block_value = random.randint(0, self.max_block)
		return block_value

class Hero:

	def __init__(self, name, starting_health = 100):
		self.name = name
		self.starting_health = starting_health
		self.abilities = []
		self.armors = []
		self.current_health = starting_health


	def add_ability(self, ability):
		self.abilities.append(ability)

	def attack(self):
		attack_total = 0
		for ability in self.abilities:
			attack_total += ability.attack()
		return attack_total


	def defend(incoming_damage):
		pass

	def take_damage(damage):
		pass

	def is_alive():
		pass

	def fight(opponent):
		pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())