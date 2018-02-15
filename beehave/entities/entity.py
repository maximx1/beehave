class Entity:
    def __init__(self, entity_id, components):
        self.entity_id = entity_id
        self.components = components
        self.setup()
        self.is_current_player_controllable = False
        self.is_displayable = False
        self.is_collidable = False
        self.speed = 0
        self.is_active = True

    def setup(self):
        return

    def update(self, game_time):
        for component in self.components:
            component.update(self, game_time)
