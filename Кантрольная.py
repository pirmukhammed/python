from random import randint  
from math import floor

level_dragon = 10
level_hero = 8

strength_dragon = 20 #сила
strength_hero = 18

dexterity_dragon = 10 #ловкость
dexterity_hero = 12

constitution_dragon = 16 #телосложение
constitution_hero = 14

intelligence_dragon = 8 #интиллект 
intelligence_hero = 8

wisdom_dragon = 20 #мудрость
wisdom_hero = 10

charisma_dragon = 8 #харизма
charisma_hero = 8

max_hp_hero = 10 + constitution_hero + randint(1, 11) * level_hero
max_hp_dragon = 10 + constitution_dragon + randint(1, 11) * level_dragon

hp_hero = max_hp_hero
hp_dragon = max_hp_dragon 

dragon_attack = randint(1, 13) + strength_dragon
hero_attack = randint(1, 13) + strength_hero
	

print("start fight")

while True:

	if randint(0, 1) == 0:	
		hp_hero = max_hp_hero - dragon_attack
		print("Удар Дракона 0")

	elif randint(0, 1) == 1:
		hp_dragon = max_hp_dragon - hero_attack
		print("Удар Героя 1")

	elif hp_hero > hp_dragon:
		print("Герой победил",  "hp_hero: ",hp_hero)
		print("Дракон умер")
		break
	else:
		print("Дракон победил", "hp_dragon: ",hp_dragon)
		print("Герой умер")
		break
