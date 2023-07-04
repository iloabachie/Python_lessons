class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            print()
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item, value in self.data_map[index]:
                if item == key:
                    # print(item, ": ", value)
                    return value
        # print(key, ": ", None)       
        return None
    
    def key_list(self):
        list_of_keys = []
        for item in self.data_map:
            if item is not None:                
                for key, value in item:
                    list_of_keys.append(key)
        # print(list_of_keys)
        return list_of_keys
                
 
my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 520)
my_hash_table.set_item("lumber", 70)
my_hash_table.set_item("hammer", 8)

from random import randint
building_items = []
building_items = ['brick', 'concrete', 'steel', 'glass', 'wood', 'cement', 'tiles', 'plaster', 'paint', 'door',
                  'window', 'roofing', 'insulation', 'wiring', 'plumbing', 'foundation', 'beam', 'column', 'stairs',
                  'elevator', 'HVAC system', 'fire sprinkler', 'interior wall', 'exterior wall', 'flooring',
                  'ceiling', 'lighting fixture', 'furniture', 'façade panel', 'balcony railing', 'balustrade',
                  'security system', 'painting', 'drywall', 'air duct', 'ventilation fan', 'bathroom fixture',
                  'kitchen appliance', 'handrail', 'guardrail', 'skylight', 'window frame', 'siding', 'gutter',
                  'downspout', 'chimney', 'waterproofing membrane', 'plumbing fixture', 'reinforcement bar',
                  'scaffolding', 'solar panel', 'fire alarm system', 'floor plan', 'blueprint', 'foundation slab',
                  'glass facade', 'steel beam', 'wooden door', 'rooftop', 'balcony', 'plumbing pipe', 'light switch',
                  'electrical outlet', 'security camera', 'staircase', 'elevator shaft', 'air conditioning unit',
                  'heating system', 'fire escape', 'paint roller', 'tile adhesive', 'gypsum board', 'bricks',
                  'lumber', 'copper pipe', 'light bulb', 'toilet', 'sink', 'shower head', 'kitchen sink', 'countertop',
                  'cabinetry', 'floor tile', 'wall paint', 'flooring material', 'window blinds', 'curtain rod',
                  'door handle', 'fire extinguisher', 'emergency exit sign', 'power generator', 'excavator',
                  'crane', 'scaffolding plank', 'surveying equipment', 'concrete mixer', 'safety helmet',
                  'construction vest', 'work gloves', 'drill machine', 'paintbrush', 'leveling tool',
                  'measuring tape', 'screwdriver', 'hammer', 'wrench', 'pliers', 'utility knife', 'saw', 'ladder',
                  'nail', 'bolt', 'screw', 'nut', 'anchor bolt', 'angle bracket', 'cable tie', 'duct tape',
                  'caulking gun', 'trowel', 'paint scraper', 'safety glasses', 'dust mask', 'hard hat']

print(len(building_items))
for _ in building_items:
    my_hash_table.set_item(_, randint(200, 800))

my_hash_table.print_table()

print(my_hash_table.get_item("washers"))
print(my_hash_table.get_item("pipes"))

print(my_hash_table.key_list())

import logging


