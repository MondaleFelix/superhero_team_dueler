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

	def __init__(name, starting_health):
		self.name = name
		self.starting_health = 100

	def add_ability(Ability):
		pass

	def attack():
		pass

	def defend(incoming_damage):
		pass

	def take_damage(damage):
		pass

	def is_alive():
		pass

	def fight(opponent):
		pass


if __name__ == "__main__":
	ability  = Ability("Debugging Ability", 20)
	print(ability.name)
	print(ability.attack())
