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
		self.deaths = 0
		self.kills = 0

	def add_kills(self, num_kills)
		self.kills += num_kills


	def add_deaths(self, num_deaths)
		self.deaths += num_deaths

		

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
		return incoming_damage - block_amount

	def take_damage(self, damage):
		self.current_health = self.current_health - self.defend(damage)

	def is_alive(self):
		return self.current_health > 0

	def fight(self, opponent):
		while self.is_alive() and opponent.is_alive():
			opponent.current_health -= self.attack()
			self.current_health -= opponent.attack()

		if self.is_alive():
			print(self.name + " won")
			self.add_kills(1)
			opponent.add_deaths(1)
		else:
			print(opponent.name + " won")
			self.add_deaths(1)
			opponent.add_kills(1)
			
# class Weapon will inherit from class Ability
class Weapon(Ability):
	def attack(self):
		return random.randint(self.max_damage // 2, self.max_damage)			


class Team:

	def __init__(self, name):
		self.name = name
		self.heroes = []

	def add_hero(self, hero):
		self.heroes.append(hero)

	def remove_hero(self, fired_hero):
		for hero in self.heroes:
			self.heroes.remove(hero)
		return 0
		

	def view_all_heroes(self):
		for hero in self.heroes:
			print(hero.name)			

if __name__ == "__main__":
