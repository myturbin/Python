import random


class LotoCard:
    def __init__(self, name):
        self.name = name
        card = []
        for i in range(0, 3):
            digit_line = sorted([random.randint(1, 90) for i in range(0, 5)])
            for i in range(0, 5):
                digit_line.insert(random.randint(0, 9), ' ')
            card.append(digit_line)

        print_card = '\n'.join(str(' '.join(str(el) for el in line)) for line in card)
        print(f'{name}:\n----------------------\n{print_card}\n----------------------\n')


human_player = LotoCard('Ваша карточка')
computer_player = LotoCard('Карточка компьютера')


