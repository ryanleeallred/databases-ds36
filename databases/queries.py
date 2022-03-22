# 302 characters
# items_per_character = '''
#     SELECT charactercreator_character.name, COUNT(armory_item.name)
#     FROM charactercreator_character
#     JOIN charactercreator_character_inventory
#     ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
#     JOIN armory_item
#     ON charactercreator_character_inventory.item_id = armory_item.item_id
#     GROUP BY charactercreator_character.name'''

# EXPERIMENTS

CREATE_TEST_TABLE = '''CREATE TABLE IF NOT EXISTS test_table
                      ("id" SERIAL NOT NULL PRIMARY KEY,
                       "name" VARCHAR(200) NOT NULL,
                       "age" INT NOT NULL,
                       "country_of_origin" VARCHAR(200) NOT NULL);'''

INSERT_TEST_TABLE = '''INSERT INTO test_table ("name", "age", "country_of_origin")
                       VALUES ('Ryan Allred asdpoifja;sldkjfpaoisjd;lfijaposdijf;asidjf;oais;dfliajdsf', 30, 'USA');'''

DROP_TEST_TABLE = '''DROP TABLE IF EXISTS test_table'''

GET_TEST_TABLE = '''SELECT * FROM test_table'''

# *****************************************************

# DATA PIPELINE

GET_CHARACTERS = 'SELECT * FROM charactercreator_character;'

DROP_CHARACTER_TABLE = '''DROP TABLE IF EXISTS characters'''

CREATE_CHARACTER_TABLE = '''CREATE TABLE IF NOT EXISTS characters (
                            "character_id" SERIAL NOT NULL PRIMARY KEY,
                            "name" VARCHAR(30) NOT NULL,
                            "level" INT NOT NULL,
                            "exp" INT NOT NULL,
                            "hp" INT NOT NULL,
                            "strength" INT NOT NULL,
                            "intelligence" INT NOT NULL,
                            "dexterity" INT NOT NULL,
                            "wisdom"  INT NOT NULL
                            );'''

INSERT_RYAN = '''INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
                 VALUES ('Ryan Alred', 50, 100, 1000, 9000, 4, -5, 12)'''
