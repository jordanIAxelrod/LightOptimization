class NoRoomException(Exception):

    def __init__(self, car, message='Car too close'):
        self.car = car
        self.message = message
        super().__init__(self.message)
