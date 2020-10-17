class Unit:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self,name,hp,damage):
        Unit.__init__(self, name,hp)
        self.damage = damage

    def attack(self, location):
        print('{name} : {location} 방향으로 적군을 공격합니다. [공격력 {damage}]'
              .format(name=self.name, location=location, damage = self.damage))

    def damaged(self, damage):
        print('{name} : {damage} 데미지를 입었습니다.'.format(name=self.name,damage=damage))
        self.hp -= damage
        print('{name}: 현재 체력은 {hp} 입니다.'.format(name=self.name,hp=self.hp))
        if self.hp <= 0:
            print('{name}: 파괴되었습니다.'.format(name=self.name))

# 드랍쉽: 공중 유닛, 수송기, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{name}: {location} 방향으로 날아갑니다. [속도 {flying_speed}]'
              .format(name=name, location=location,flying_speed=self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name,hp,damage)
        Flyable.__init__(self, flying_speed)

# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.fly(valkyrie.name, '3시')

