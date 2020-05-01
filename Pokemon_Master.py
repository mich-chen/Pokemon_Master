class Pokemon:
  def __init__(self, name, level, type, maximum_health, current_health, is_knocked_out):
    self.name = name
    self.level = level
    self.type = str(type)
    self.max_health = self.level * 10
    self.health = current_health
    self.is_knocked_out = is_knocked_out
    #types we are coding will only be fire, water, grass
  
  def lose_health(self, health_lost):
    self.health_lost = health_lost
    self.new_lost_health = self.health - self.health_lost
    return self.name + " has lost " + str(self.health_lost) + " health! Now the health is " + str(self.new_lost_health) + "!"
  
  def regain_health(self):
    return self.name + " has regained health to " + str(self.max_health) + "!" 
  
  def knock_out(self):
    #when health became 0
    if self.health < 0:
      return self.name + " is knocked out!"   
    
  def revive(self):
    #revives knocked out pokemon
    if self.is_knocked_out is True:
      return self.name + " has been revived!" 
    
  def attack(self, other):
    if (self.type == "Fire" and other.type == "Grass") or (self.type == "Water" and other.type == "Fire") or (self.type == "Grass" and other.type == "Water"):
      amount_damage = 2 * self.level
      other_new_health = other.health - amount_damage
      return self.name + " has attacked " + other.name + " and caused " + str(amount_damage) + " damage, now " + other.name + " has " + str(other_new_health) + " health left!"
    elif (self.type == other.type) or (self.type == "Fire" and other.type == "Water") or (self.type == "Water" and other.type == "Grass") or (self.type == "Grass" and other.type == "Fire"): 
      amount_damage = (1/2) * self.level
      other_new_health = other.health - amount_damage
      return self.name + " has attacked " + other.name + " and caused " + str(amount_damage) + " damage, now " + other.name + " has " + str(other_new_health) + " health left!"

class Trainer:
  def __init__(self, name, potions, pokemons, current_active_pokemon):
    self.name = name
    self.potions = potions
    #potions is number of potions
    self.pokemons = pokemons
    #pokemons is a LIST of STRINGS of pokemon
    self.current_pokemon = pokemons[current_active_pokemon]
    #current_active_pokemon is a number, a number that is representing the pokemon in the LIST (ie. the index/position of that pokemon)
    
  def use_potion(self, num_potions_used):
    potion = 20
    total_potion_add = potion * num_potions_used
    self.potions -= num_potions_used
    self.potioned_health = self.current_pokemon.health  +  total_potion_add
    if self.potioned_health >= self.current_pokemon.max_health:
      return str(num_potions_used) + " potions were used. " + str(self.current_pokemon.name) + "'s HP is now " + str(self.current_pokemon.max_health) + "."
    else:
      return str(num_potions_used) + " potions were used. " + str(self.current_pokemon.name) + "'s HP is now " + str(self.potioned_health) + "."
    #need a way to stop adding potion to health after max health is reached
    
  def attack_other_trainer(self, other_trainer):
    return self.name + " has attacked " + other_trainer.name + "! " + self.current_pokemon.attack(other_trainer.current_pokemon)
   #current active pokemon will add damage to other trainer's current active pokemon self.current_pokemon.attack(other.current_pokemon)
  def switch_pokemon(self, switch):
    self.switch = self.pokemons[switch]
    self.current_pokemon = self.switch
    return self.name + " has switched to " + str(self.current_pokemon.name) + "!"
    
    
Charmander = Pokemon('Charmander', 5, 'Fire', 50, 25, 'no')
#print(Charmander.lose_health(5))
Squirtle = Pokemon('Squirtle', 10, 'Water', 100, 75, 'no')
#print(Squirtle.attack(Charmander))
#print(Squirtle.lose_health(5))
Bulbasaur = Pokemon('Bulbasaur', 5, "Grass", 50, 75, 'no')

#print(Squirtle.max_health)

