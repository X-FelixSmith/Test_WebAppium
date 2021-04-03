import yaml


class Bicycle:
    mileage = 0

    def run(self,miles):
        print(f"骑行了 {miles}km")

class EBicycle(Bicycle):
    battery_level:int

    def __init__(self,battery):
        self.battery_level = battery

    def fill_charge(self,vol):
        self.battery_level += vol

    def run(self,km):
        miles = km - self.battery_level * 10
        if miles > 0 :
            print("电不够用")
            print(f"使用电骑行了{self.battery_level*10}km")
            print(f"还需脚蹬{miles}km")
            # Bicycle().run(miles)
            super().run(miles)
        else:
            print("电够用")
            print(f"用电骑行了{km}km")

with open("../demo_datas/demo_01.yaml",encoding="utf-8") as f:
    datas = yaml.safe_load(f)
data = datas['default']

# print(data)


el = EBicycle(data['battery'])
el.run(data['km'])

# b1 = Bicycle()
# b1.run(10)