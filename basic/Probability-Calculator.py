import random
import copy


def are_in_list(list1, list2):
    new_list2 = copy.deepcopy(list2)
    result = []
    for item in list1:
        if item in new_list2:
            result.append(True)
            new_list2.remove(item)
        else:
            result.append(False)

    return all(result)


class Hat():
    def __init__(self, **colors):
        self.colors = colors
        self.contents = []
        for item, num in colors.items():
            while num > 0:
                self.contents.append(item)
                num = num - 1

    def draw(self, remove):
        removed_balls = []
        while remove > 0:
            if len(self.contents) == 0:
                return removed_balls
            removed_element = random.choice(self.contents)
            self.contents.remove(removed_element)
            removed_balls.append(removed_element)
            remove = remove - 1
        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    list_expected_balls = []
    for key, val in expected_balls.items():
        while val > 0:
            list_expected_balls.append(key)
            val = val - 1

    M = 0
    i = num_experiments
    while i > 0:
        new_hat = copy.deepcopy(hat)
        drawing = new_hat.draw(num_balls_drawn)
        if are_in_list(list_expected_balls, drawing):
            M = M + 1
        i = i - 1
    
    return M / num_experiments



hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=5,
    num_experiments=3000)
print("Probability:", probability)