# 클래스 변수와 인스턴스 변수

# 클래스 정의
class Card:
    # 필드 정의
    kind = ""
    number = 0
    width = 100 # 클래스 변수
    height = 250 # 클래스 변수
    
    # 생성자 정의
    def __init__(self, kind, number):
        self.kind = kind
        self.number = number
        
    # 출력 메서드 정의
    def __str__(self):
        print("kind :", self.kind)
        print("number :", self.number)
        print("width :", Card.width)
        print("height :", Card.height)

# 메인 함수 정의
def main():
    # 클래스 변수에 초기화된 값은 공유가 되고 있음을 확인 가능
    # 인스턴스 변수만 입력
    card1 = Card("다이아몬드", 10)
    card1.__str__()
    
    card2 = Card("스페이드", 11)
    card2.__str__()

# 파일 실행의 시점
if __name__ == "__main__":
    main()
