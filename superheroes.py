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

	def add_kills(self, num_kills):
		self.kills += num_kills


	def add_deaths(self, num_deaths):
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

	def defend(self, incoming_damage = 0):
		block_amount = 0
		for armor in self.armors:
			block_amount += armor.block()
		return block_amount - incoming_damage

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

	def add_weapon(self, weapon):
	    '''Add weapon to self.abilities'''
	    self.add_ability(weapon)
	    # TODO: This method will append the weapon object passed in as an
	    # argument to self.abilities.
	    # This means that self.abilities will be a list of
	    # abilities and weapons.


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

	def is_all_dead(self):
		all_dead = False

		for hero in self.heroes:
			if hero.is_alive():
				all_dead = True

		return all_dead

	def get_random_hero(self):
		return self.heroes[random.randint(0, len(self.heroes) - 1)]

	def attack(self, other_team):
	    ''' Battle each team against each other.'''
	    # TODO: Randomly select a living hero from each team and have

	    while self.is_all_dead() and other_team.is_all_dead():

	    	our_random_hero = self.get_random_hero()
	    	other_teams_hero = other_team.get_random_hero()

	    	if our_random_hero.is_alive() or other_teams_hero.is_alive():
	    		our_random_hero.fight(other_teams_hero)
	    	else:
		    	our_random_hero = self.get_random_hero()
		    	other_teams_hero = other_team.get_random_hero()


	    # them fight until one or both teams have no surviving heroes.
	    # Hint: Use the fight method in the Hero class.


	def revive_heroes(self, health=100):
	    ''' Reset all heroes health to starting_health'''
	    for hero in self.heroes:
	    	hero.current_health = hero.starting_health


	def stats(self):
	    '''Print team statistics'''
	    for hero in self.heroes:
	    	print(hero.name + "has a KD of " + hero.kills + "/" + hero.deaths)


class Arena:
	def __init__(self):
		team_one = None
		team_two = None 

	def create_ability(self):
		ability_name = input("Ability name: ")
		ability_damage = input("Ability damage: ")
		return Ability(ability_name, ability_damage)

	def create_weapon(self):
		weapon_name = input("Weapon name: ")
		weapon_damage = input("Weapon name: ")
		return Weapon(weapon_name, weapon_damage)

	def create_armor(self):
		armor_name = input("Armor name: ")
		armor_amount = input("Armor block amount: ")
		return Armor(armor_name, armor_amount)

	def create_hero(self):
		hero_name = input("Hero name: ")
		hero_health = input("Hero starting health: ")
		return Hero(hero_name, hero_health)

	def build_team_one(self):
	'''Prompt the user to build team_one '''
		team_name = input("Enter a team name: ")
		num_of_heroes = input("Enter a number of heroes: ")

		self.team_one = Team(team_name)

		for i in range(num_of_heroes):
			self.team_one.add_hero(self.create_hero)



	def build_team_two(self):
		team_name = input("Enter a team name: ")
		num_of_heroes = input("Enter a number of heroes: ")

		self.team_two = Team(team_name)

		for i in range(num_of_heroes):
			self.team_two.add_hero(self.create_hero)


    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.

        self.team_one.attack(self.team_two)




if __name__ == "__main__":
    armor = Hero("The Ring", 200)
    for _ in range(0, 500):
        defense = armor.defend()
        assert (defense <= 200 and defense >= 0)

