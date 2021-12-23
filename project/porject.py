import pyautogui
import time


class Generator:
    def __init__(self, length):
        self.length = length

    def generate(self):
        for _ in range(self.length):
            x, y = pyautogui.position()
            yield (x * y) % 2
            time.sleep(0.4)

    def assemble(self):
        generator = self.generate()
        while True:
            try:
                print(next(generator), end='')
            except StopIteration:
                break


number_generator = Generator(16)

number_generator.assemble()
