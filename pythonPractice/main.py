class Car:

    def __init__(self, name, color, price, dire):
        self.name = name
        self.color = color
        self.price = price
        self.dire = dire

    def info(self):
        print(f"이름 : {self.name}")
        print(f"색깔 : {self.color}")
        print(f"가격 : {self.price}")
        print(f"방향 : {self.dire}")
        print()

    def move(self, num):
        print(self.dire[num])


Car1 = Car('벤츠', '흰색', 300, ['오른쪽', '왼쪽', '정지'])
Car2 = Car('아우디', '검은색', 150, ['오른쪽', '왼쪽', '정지'])
Car3 = Car('BMW', '빨간색', 180, ['오른쪽', '왼쪽', '정지'])

Car1.info()
Car2.info()
Car3.info()

Car1.move(1)
Car2.move(2)
Car3.move(0)