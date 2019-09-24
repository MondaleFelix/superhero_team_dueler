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

	def add_armor(self, armor):
		self.armors.append(armor)

	def defend(self, incoming_damage):
		block_amount = 0
		for armor in self.armors:
			block_amount += armor.block()
		return block_amount

	def take_damage(self, damage):
		self.current_health = self.current_health - self.defend(damage)

	def is_alive():
		pass

	def fight(opponent):
		pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)