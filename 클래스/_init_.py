class Unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{name}이 생성 되었습니다.'.format(name=self.name))
        print('체력 {hp}, 공격력 {damage}'.format(hp=self.hp,damage=self.damage))

marine1 = Unit('마린',40,5)
marine2 = Unit('마린',40,5)
tank = Unit('탱크',150,35)

# 레이스: 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit('레이스',80,5)
print('유닛 이름: {name}, 공격력: {damage}'.format(name=wraith1.name,damage=wraith1.damage))

# 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit('레이스',80,5)
wraith2.clocking = True

if wraith2.clocking == True:
    print('{name}는 현재 클로킹 상태입니다.'.format(name=wraith2.name))