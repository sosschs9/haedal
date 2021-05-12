
class idol:
    idol_count = 0

    def __init__(self, name, total, leader, playlist):
        self.name = name
        self.total = total
        self.leader = leader
        self.playlist = playlist
        idol.idol_count += 1

    def info(self):
        print(f'그룹명 : {self.name}')
        print(f'인원수 : {self.total}')
        print(f'리더명 : {self.leader}')
        print(f'플레이리스트 : {self.playlist}')
        print()

idol1 = idol('방탄소년단', 7, 'RM', ['Dynamite', '봄날', 'DNA'])
idol2 = idol('오마이걸', 7, '효정', ['살짝설렜어', '비밀정원', '불꽃놀이'])
idol3 = idol('세븐틴', 13, '에스쿱스', ['예쁘다', '아주NICE', '울고싶지않아'])
idol4 = idol('ITZY', 5, '예지', ['달라달라', 'ICY', 'NOT SHY'])

idol1.info()
idol2.info()
idol3.info()
idol4.info()