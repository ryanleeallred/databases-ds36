# 302 characters
select_all = 'SELECT * FROM charactercreator_character;'
# new_query = 'some query stuff'
items_per_character = '''
    SELECT charactercreator_character.name, COUNT(armory_item.name)
    FROM charactercreator_character 
    JOIN charactercreator_character_inventory
    ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
    JOIN armory_item
    ON charactercreator_character_inventory.item_id = armory_item.item_id
    GROUP BY charactercreator_character.name'''
