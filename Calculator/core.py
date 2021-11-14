class Character():
    def __init__(self, health, armor, damage):
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


hero = Character(10, 15, '1d8')
villain = Character(15, 10, '1d6')
print(hero.attack(villain))
