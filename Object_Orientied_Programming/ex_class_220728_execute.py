# Monitor 클래스를 이용한 실습
from ex_class_220728 import Monitor # 해당 파일로부터 저 클래스만 import
# from ex_class_220728 import * # 해당 파일로부터 모든 함수 및 클래스를 import

if __name__ == "__main__":
    # 매개변수가 있는 생성자를 호출하는 방법
    monitor1 = Monitor("삼성", 14, 340000, "검정색")
    monitor1.color = "흰색" # private한 필드에 대해서는 반응 없음
    monitor1.__str__()
    
    print("--------------------------")
    # 아래와 같이 setter()를 통하여 기존에 생성자로 생성했던 값을 변경
    monitor1.setCompany(("LG"))
    monitor1.setInch(32)
    monitor1.setPrice(500000)
    monitor1.setColor("흰색")
    monitor1.__str__()

