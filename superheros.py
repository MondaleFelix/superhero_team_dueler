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
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
