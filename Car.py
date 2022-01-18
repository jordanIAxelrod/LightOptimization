import time

import Road


class Car:
    TIMEDELTA = 4 / 3600
    CAR_WIDTH = 14.7 / 5160

    def __init__(self, speed_limit: int, trip: list[Road.Road]):
        self.start = time.time()
        self.position = 0
        self.length = trip[0].length
        self.speed_limit = speed_limit
        self.trip = trip
        self.current = 0

    def move(self, light, oth=None):
        """
        Move the car through the road system
        :param light: whether the light is green
        :param oth: car infront of this one on the road.
        :return: New road and the car if the car is changing roads otherwise
        """
        possible_pos = self.position + self.speed_limit * self.TIMEDELTA
        if oth and oth.position - self.CAR_WIDTH < possible_pos:
            self.position = oth.position - self.CAR_WIDTH
        elif oth:
            self.position = possible_pos
        elif not oth:

            if possible_pos > self.length and light:
                if self.current + 1 > len(self.trip):
                    return -1
                if self.trip[self.current + 1].queue[-1].position <= self.CAR_WIDTH:
                    self.position = self.length
                else:
                    # On the next update this car will be at 0 on the next road,
                    # but it may have been further into the road. Don't want to do the calculation of
                    # finding the amount time left to multiply by the new speed limit.
                    self.current += 1
                    return self, self.trip[self.current]
            elif possible_pos < self.length and light:
                self.position = possible_pos
            elif possible_pos > self.length and not light:

                self.position = self.length
        else:

            self.position = possible_pos
        return None

    def trip_over(self):
        return time.time() - self.start
