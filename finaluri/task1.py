class Axali:
    def __init__(self):
        self.tp = ()

    def daamate(self, value):
        if value not in self.tp:
            self.tp += (value,)
        else:
            print('element should be unique')

    def washale(self, value):
        if value in self.tp:
            index = self.tp.index(value)
            self.tp = self.tp[:index] + self.tp[index + 1:]
        else:
            print('no such element in tuple')

    def __str__(self):
        result = []
        for i in self.tp:
            result.append(str(i))

        return ', '.join(result)
