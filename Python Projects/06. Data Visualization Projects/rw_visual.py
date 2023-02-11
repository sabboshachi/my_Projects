import matplotlib.pyplot as pylt


class RWalk():
    def __init__(self, number_of_points=500):
        self.number_of_points = number_of_points
        self.xvalues = [0]
        self.yvalues = [0]

    def fil_walk(self):
        while len(self.xvalues) < self.number_of_points:
            # Choose a route and how far you want to go in that way.
            x_route = choice([1, -1])
            x_length = choice([0, 1, 2, 3, 4])
            x_move = x_route * x_length

            y_route = choice([1, -1])
            y_length = choice([0, 1, 2, 3, 4])
            y_move = y_route * y_length

            # discard walks that go nowhere.
            if x_move == 0 and y_move == 0:
                continue

            succeeding_x = self.xvalues[-1] + x_move
            succeeding_y = self.yvalues[-1] + y_move

            self.xvalues.append(succeeding_x)
            self.yvalues.append(succeeding_y)


rwalk = RWalk()
rwalk.fil_walk()

pylt.scatter(rwalk.xvalues, rwalk.yvalues, s=14)  # s is size of dots
pylt.show()