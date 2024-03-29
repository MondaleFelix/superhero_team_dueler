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
		self.current_health = int(starting_health)
		self.deaths = 0
		self.kills = 0

	def add_kills(self, num_kills):
		self.kills += num_kills


	def add_deaths(self, num_deaths):
		self.deaths += num_deaths

		

	def add_ability(self, ability):
		self.abilities.append(ability)

	def attack(self):
		attack_total = random.randint(0,9)
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
		return int(self.current_health) > 0

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
		
	def get_alive_heroes(self):
		alive_heroes = []
		for hero in self.heroes:
			if hero.is_alive():
				alive_heroes.append(hero)

		return alive_heroes

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
	    	hero.current_health = health


	def stats(self):
	    '''Print team statistics'''
	    for hero in self.heroes:
	    	print(hero.name + "has a KD of " + hero.kills + "/" + hero.deaths)

	def get_average_kd(self):
		kills = 0
		deaths = 0
		for hero in self.heroes:
			kills += hero.kills
			deaths += hero.deaths
		if deaths == 0:
			return kills
		return kills / deaths

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

		team_name = input("Enter a Team 1 name: ")
		num_of_heroes = int(input("Enter a number of heroes: "))

		self.team_one = Team(team_name)

		for i in range(num_of_heroes):
			self.team_one.add_hero(self.create_hero())



	def build_team_two(self):
		team_name = input("Enter a Team 2 name: ")
		num_of_heroes = int(input("Enter a number of heroes: "))

		self.team_two = Team(team_name)

		for i in range(num_of_heroes):
			self.team_two.add_hero(self.create_hero())


	def team_battle(self):
		self.team_one.attack(self.team_two)



	def show_stats(self):

		if self.team_one.is_all_dead():
			print(self.team_one.name + " is the winner!")
			print("The teams average KD was " + str(self.team_one.get_average_kd()))
			for hero in self.team_one.get_alive_heroes():
				print(hero.name)
		else:
			self.team_two.name + " is the winner!"
			print("The teams average KD was " + str(self.team_two.get_average_kd()))
			for hero in self.team_two.get_alive_heroes():
				print(hero.name)



if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
