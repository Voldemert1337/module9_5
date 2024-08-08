class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self._start = start
        self._stop = stop
        self._step = step
        self._pointer = start

    def __iter__(self):
        self._pointer = self._start
        return self

    def __next__(self):
        if (self._step > 0 and self._pointer >= self._stop) or (self._step < 0 and self._pointer <= self._stop):
            raise StopIteration

        current = self._pointer
        self._pointer += self._step
        return current

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

print()
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()