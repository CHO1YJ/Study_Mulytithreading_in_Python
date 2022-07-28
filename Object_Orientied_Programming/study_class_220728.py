# 원을 클래스로 표시해보자.
# 원에는 반지름(radius)이라는 필드가 있다.
# 원의 넓이와 둘레를 계산하는 메서드를 정의한다.
# 생성자는 매개변수가 존재하는 생성자를 정의한다.
# 출력결과는 다음과 같다.
# 출력결과
# 원의 반지름 : 10
# 원의 넓이 : 314.16
# 원의 둘레 : 62.83
#------------------------------------------------------------------------------

# 모듈 추가
import numpy as np

# 클래스 정의
class Circle:
    # 필드 정의
    __radius = 0
    __space = 0
    __perimeter = 0
    
    # 매개변수가 포함된 생성자 정의
    def __init__(self, radius):
        self.__radius = radius
        self.__space = np.pi * np.power(radius, 2)
        self.__perimeter = 2 * np.pi * radius
    
    # getter() 메서드 정의
    def getRadius(self):
        return self.__radius
    def getSpace(self):
        return self.__space
    def getPerimeter(self):
        return self.__perimeter
    
    # setter() 메서드 정의
    def setCircle(self, radius):
        self.__radius = radius
        self.__space = np.pi * np.power(radius, 2)
        self.__perimeter = 2 * np.pi * radius
    
    # 출력 메서드 정의
    def __str__(self):
        print("출력 결과")
        print("원의 반지름 :", self.getRadius())
        print("원의 넓이 :", np.round(self.getSpace(), 2))
        print("원의 둘레 :", np.round(self.getPerimeter(), 2))

# 메인함수 정의
def main():
    Circle1 = Circle(10)
    Circle1.__str__()
    print("--------------------------------")
    print("반지름 변경")
    Circle1.setCircle(1)
    Circle1.__str__()

# 파일의 시점 정의
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        