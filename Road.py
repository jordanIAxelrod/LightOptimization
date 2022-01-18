"""
simulates a road. Given length, width, speed limit, create a queue of cars on the road
"""
import Car
import RoadQueue


class Road:

    def __init__(self, length, width, speed_limit, name):
        self.length = length
        self.width = width
        self.speed_limit = speed_limit
        self.name = name
        self.queue = RoadQueue.RoadQueue()

    def update(self, light):
        return self.queue.move_each(light)

    def add_car(self, new_car):
        self.queue.enqueue(new_car, self.speed_limit, self.length)
