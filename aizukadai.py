from datetime import datetime

# 誕生日から様々な情報を表示するクラス
class ShowFromBirth:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    #生まれた日から今日までの日数を求める関数
    def FromBirthToToday(self):
        # 現在の日付
        today = datetime.today()
        # 誕生日
        birthday = datetime(self.year,self.month,self.day)

        return today - birthday

    # 星座を求める関数
    def zodiac(self):
        if (self.month == 1 and self.day >= 20) or (self.month == 2 and self.day <= 18):
            return "みずがめ座"
        elif (self.month == 2 and self.day >= 19) or (self.month == 3 and self.day <= 20):
            return "うお座"
        elif (self.month == 3 and self.day >= 21) or (self.month == 4 and self.day <= 19):
            return "おひつじ座"
        elif (self.month == 4 and self.day >= 20) or (self.month == 5 and self.day <= 20):
            return "おうし座"
        elif (self.month == 5 and self.day >= 21) or (self.month == 6 and self.day <= 21):
            return "ふたご座"
        elif (self.month == 6 and self.day >= 22) or (self.month == 7 and self.day <= 22):
            return "かに座"
        elif (self.month == 7 and self.day >= 23) or (self.month == 8 and self.day <= 22):
            return "しし座"
        elif (self.month == 8 and self.day >= 23) or (self.month == 9 and self.day <= 22):
            return "おとめ座"
        elif (self.month == 9 and self.day >= 23) or (self.month == 10 and self.day <= 23):
            return "てんびん座"
        elif (self.month == 10 and self.day >= 24) or (self.month == 11 and self.day <= 22):
            return "さそり座"
        elif (self.month == 11 and self.day >= 23) or (self.month == 12 and self.day <= 21):
            return "いて座"
        else:
            return "やぎ座"
        
    # 干支を求める関数(西暦+9を12で割った余りによって場合分けできる)
    def chinese_zodiac(self):
        if (self.year + 9) % 12 == 1:
            return "子"
        elif (self.year + 9) % 12 == 2:
            return "丑"
        elif (self.year + 9) % 12 == 3:
            return "寅"
        elif (self.year + 9) % 12 == 4:
            return "卯"
        elif (self.year + 9) % 12 == 5:
            return "辰"
        elif (self.year + 9) % 12 == 6:
            return "巳"
        elif (self.year + 9) % 12 == 7:
            return "午"
        elif (self.year + 9) % 12 == 8:
            return "未"
        elif (self.year + 9) % 12 == 9:
            return "申"
        elif (self.year + 9) % 12 == 10:
            return "酉"
        elif (self.year + 9) % 12 == 11:
            return "戌"
        else:
            return "亥"

# main関数
def main():
    # 標準入力受け取り
    year,month,day = map(int,input().split())

    show_from_birth = ShowFromBirth(year, month, day)
    FromBirthToToday = show_from_birth.FromBirthToToday()
    zodiac = show_from_birth.zodiac()
    chinese_zodiac = show_from_birth.chinese_zodiac()

    print("生まれた日から今日までの日数：", FromBirthToToday)
    print("あなたの星座：", zodiac)
    print("あなたの干支：", chinese_zodiac)

if __name__ == "__main__":
    main()