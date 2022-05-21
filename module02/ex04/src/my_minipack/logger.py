import time
from random import randint
import os
import functools


def log(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        f = open("machine.log", "a")
        name = function.__name__
        name = ' '.join(name.split('_')).title().ljust(15)
        start_time = time.perf_counter()
        ret = function(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        unit = "s"
        if run_time < 1:
            run_time *= 1000
            unit = "ms"
        f.write('({user})Running: {name}[ exec-time = {time:.3f} {unit} ]\n'
                .format(user=os.getenv('USER'), name=name, time=run_time,
                        unit=unit))
        f.close()
        return ret
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
