"""
The controller of the roads. Passes cars between roads. Controls the lights and passes that to the roads as they change.
"""

class Intersection:

    def __init__(self, incoming_roads, outgoing_roads, light_schedule):
        self.incoming_roads = incoming_roads
        self.outgoing_roads = outgoing_roads
        self.lights = [0 for _ in incoming_roads]
        self.light_schedule = light_schedule

    def update_roads(self):
        for i, road in enumerate(self.incoming_roads):
            road.update(self.lights[i])
