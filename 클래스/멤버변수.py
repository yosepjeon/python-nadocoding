class Unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{name}이 생성 되었습니다.'.format(name=self.name))
        print('체력 {hp}, 공격력 {damage}'.format(hp=self.hp,damage=self.damage))

class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{name}이 생성 되었습니다.'.format(name=self.name))
        print('체력 {hp}, 공격력 {damage}'.format(hp=self.hp,damage=self.damage))

    def attack(self, location):
        print('{name} : {location} 방향으로 적군을 공격합니다. [공격력 {damage}]'
              .format(name=self.name, location=location, damage = self.damage))

    def damaged(self, damage):
        print('{name} : {damage} 데미지를 입었습니다.'.format(name=self.name,damage=damage))
        self.hp -= damage
        print('{name}: 현재 체력은 {hp} 입니다.'.format(name=self.name,hp=self.hp))
        if self.hp <= 0:
            print('{name}: 파괴되었습니다.'.format(name=self.name))

# 파이어뱃: 공격 유닛, 화염방사기.
firebat1 = AttackUnit('파이어벳',50,16)
firebat1.attack('5시')

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)