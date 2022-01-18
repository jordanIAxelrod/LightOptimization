from ProjectExceptions import NoRoomException


class RoadQueue:
    CAR_WIDTH = 14.7 / 5160

    def __init__(self, cars=[]):
        self.list = []
        for car in cars:
            self.list.append(car)

    def move_each(self, light):
        """
        move each car from the first to the last
        :param light: whether the light is green or not
        :return: cars that need to be moved to a different road
        """
        result = []
        for i, car in enumerate(self.list):
            to_intersection = car.move(light, self.list[i - 1])
            if to_intersection == -1:
                self.list.remove(car)
            if to_intersection:
                result.append(to_intersection)
                self.list.remove(to_intersection[1])

        return result

    def enqueue(self, car, speed_limit, length):
        """
        add the car to the queue of the road
        :param car: the car to add
        :param speed_limit: the speed limit of the road
        :param length: the length of the road
        :return:
        """
        if len(self.list) and self.list[-1].position <= self.CAR_WIDTH:
            raise NoRoomException(self.list[-1], f"Car is only {self.list[-1].position} from entrance")

        car.length = length
        car.position = 0
        car.speed_limit = speed_limit
        self.list.append(car)
