class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name # изменил, чтобы в возращаемый словарь добавлялось только имя объекта Ranner
                    place += 1
                    self.participants.remove(participant)

        return finishers


all_results = {}


def setUp():
    runner_1 = Runner("Усэйн", 10)
    runner_2 = Runner("Андрей", 9)
    runner_3 = Runner("Ник", 3)
    return runner_1, runner_2, runner_3


def tearDownClass():
    print(*all_results)


distance_90 = Tournament(90, *setUp()[0:3])
print(distance_90.participants)
all_results.update(distance_90.start())
print(all_results)

