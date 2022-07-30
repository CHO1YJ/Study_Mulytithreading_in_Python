# 인스턴스 변수 : 인스턴스를 생성해야 비로소 사용할 수 있는 변수
# 인스턴스 변수는 메모리 공간에 독립적으로 공간을 차지하고 있어서 해당
# 인스턴스에게만 영향을 미침
# 인스턴스 변수의 접근 방법 : (인스턴스명).(인스턴스 변수명)

# 클레스 변수 : 클래스가 로딩이 되면서 메모리 상당(메서드 영역, 클래스 영역)
# 미리 공간을 항당하고 저장되고 클래스 변수는 모든 인스턴스에게 공유되는 변수
# 클래스 변수의 접근 방법 : (클래스명).(클래스 변수명(권장사항))
# 클래스 변수의 값의 변경은 모든 인스턴스에 영향을 미침
# 클래스 변수는 인스턴스 생성이 없이도 접근이 가능하다.

# 클래스 정의
class Car:
    # # Car 클래스의 필드 정의
    color = ""  # 인스턴스 변수
    speed = 0   # 인스턴스 변수
    count = 0   # 클래스 변수는 반드시 필드로 선언해 줘야 한다.
    # JAVA에서는 "static count = 0"으로 클래스 변수를 표현
    
    # 기본 생성자 정의
    def __init__(self):
        self.color = "노랑"
        self.speed = 0
        Car.count += 1
    
    # 출력 메서드 정의
    def __str__(self):
        print("color :", self.color)
        print("speed :", self.speed)
        # 아래는 클래스 변수에 접근하는 방법 2가지
        print("count :", Car.count)
        # print("count :", self.count) # 권장하지는 않지만 다음도 가능

# 메인 함수 정의
def main():
    # print(Car.count) # 인스턴스 없이도 호출이 가능! 저장된 메모리 공간이 다름!
    print(id(Car.count)) # 클래스 Car를 통한 호출 주소
    
    # 인스턴스 생성
    car1 = Car()
    car1.__str__()
    print(id(car1.count)) # 인스턴스 car1를 통한 호출 주소
    # 파이썬에서는 인스턴스를 생성하면 메모리의 값이 새로 할당
    print(id(Car.count)) # 인스턴스를 생성하면 클래스 변수의 호출 주소를 재할당!
    
    car2 = Car()
    car2.__str__()
    print(id(car2.count)) # 인스턴스 car2를 통한 호출 주소

# 파일 실행의 시점
if __name__ == "__main__":
    main()        
    
    
    
    
    
    
    
    
    
    
    