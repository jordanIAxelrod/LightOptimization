import Car
import Road

class CarTest:

    def __init__(self):
        self.road = Road.Road(400, 1, 35, 'first')
        self.car = Car.Car(35, [self.road])
        self.oth = Car.Car(35, [self.road])
        self.road.add_car(self.car)
        while self.car.position < self.car.CAR_WIDTH:
            self.car.move(1)
            print(self.car.position)
        print(self.car.position)
        self.road.add_car(self.oth)

    def test_move(self):
        orig = self.car.position
        self.car.move(1)
        print('car width', self.car.CAR_WIDTH)
        print('car position', self.car.position)
        assert self.car.position == 35 * 4 / 3600 + orig

        while self.oth.position < self.car.position - self.car.CAR_WIDTH:
            self.oth.move(1, self.car)
        assert self.oth.position == self.car.position - self.car.CAR_WIDTH, f"Should be {self.car.position - self.car.CAR_WIDTH} and is {self.oth.position} "
        print(self.car.CAR_WIDTH)
        print('all tests passed')


def main():
    CarTest().test_move()


if __name__ == '__main__':
    main()