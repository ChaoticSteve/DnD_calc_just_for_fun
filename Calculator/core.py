class Character():
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def attack(self, other):
        if self.roll_dice('1d20') > other.armor:
            other.health = other.health - self.roll_dice(self.damage)
            print('hit')
        return other.health

    @staticmethod
    def roll_dice(roll):
        import random
        roll = roll.split('d')
        result = [random.randint(1, int(roll[1])) for _ in range(int(roll[0]))]
        return sum(result)

    def winner(self, other):
        turn = True
        i = 1
        while self.health > 0 or other.health > 0:
            if turn:
                self.attack(other)
                print(f'{i} round:{self.name} attack {other.name}')
                turn = False
            else:
                other.attack(self)
                print(f'{i} round:{other.name} attack {self.name}')
                turn = True
            i += 1


if __name__ == '__main__':
    hero = Character('Jhon', 10, 15, '1d8')
    villain = Character('Mike', 15, 10, '1d6')
    hero.winner(villain)
