import random


class Team:

	def __init__(self, name):
		self.name = name
		self.heroes = []

	def add_hero(self, hero):
		self.heroes.append(hero)

	def remove_hero(self, fired_hero):
		for hero in self.heroes:
			if hero == fired_hero:
				self.heroes.pop(index(hero))

	def view_all_heroes(self):
		for hero in self.heroes:
			print(hero)



class Ability:

	def __init__(self, name , max_damage):
		self.name = name
		self.max_damage = max_damage

	def attack(self):
		attack_value = random.randint(0, self.max_damage)
		return attack_value 



# class Weapon will inherit from class Ability
class Weapon(Ability):
	def attack(self):
		return random.randint(self.max_damage * 0.05, self.max_damage)


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
		else:
			print(opponent.name + " won")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)