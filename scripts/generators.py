"""


"""
# Аннотация кода (описание абстрактного класса)
from typing import Optional


class BaseGenerator:
    def reset(self) -> None:
        raise NotImplementedError  # специальная ошибка, которая обозначает, что ф-я не реализована

    def generate(self) -> Optional[str]:  # optional обознач, что может вернуться строка, а может None
        raise NotImplementedError


class PopPasswordGenerator(BaseGenerator):  # наследование
    def __init__(self):
        with open('pop_pas.txt') as f:
            content = f.read()

        self.passwords = content.split("\n")

        self.i = 0

    # фу-я, которая сбрасывает счетчик
    def reset(self):
        self.i = 0

    # фу-я, которая каждый раз возврщает новый пароль
    def generate(self):
        if self.i > len(self.passwords):
            return None

        password = self.passwords[self.i]
        self.i += 1
        return password


# generator1 = PopPasswordGenerator()
# generator2 = PopPasswordGenerator()
#
# print(generator1.generate())
# print(generator2.generate())
#
# print(generator1.generate())
# print(generator1.generate())
# print(generator1.generate())
#
# print(generator1.i)
# print(generator2.i)

# g = PopPasswordGenerator()
# print(g.generate())
# print(g.generate())
# print(g.reset())
# print(g.generate())
# print(g.generate())
