#import json

class Stage:
    def __init__(self):
        self.title = "untitled"
        self.stage_blocks = {}
        self.stage_entities = {}

    def add_block(self, block: str, location: tuple[int], tags: set = set()):
        if not self.is_location_taken(location):
            self.stage_blocks[location] = (block, tags)
            print("block: " + block + " placed")
        else:
            print("that location is already taken")

    def add_entity(self, entity: str, location: tuple[int], tags: set):
        if not is_location_taken(location):
            self.stage_entities[location] = (entity, tags)

    def delete(self, location):
        if is_location_taken(location):
            try:
                del self.stage_blocks[location] 
            except:
                del self.stage_entities[location]
            
    def is_location_taken(self, location: tuple[int]):
        return  location  in self.stage_blocks or location  in self.stage_entities

class StageManager:
    def __init__(self):
        self.stages = []

