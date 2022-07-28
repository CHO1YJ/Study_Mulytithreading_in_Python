# 매개변수가 있는 생성자에 대한 실습
class Monitor:
    # __(핃드명) ; 캡슐화(은닉; private)가 된 필드 _ 외부에서의 접근이 제한적
    # 필드 선언
    __company = ""
    __inch = 0
    __price = 0
    __color = ""
    
    # # 파이썬에서는 1개 이상의 생성자를 만들 수가 없음
    # # 오버로딩 : 같은 메서드명으로 다른 일을 하게끔 만드는 작업
    #     # 매개변수의 타입과 개수에 따라서 같은 이름의 메서드라도 
    #     # 다른 메서드가 호출이 되는 형태를 지칭
    # def __init__(self):
    #     print("기본 생성자 호출")
    
    # 매개변수가 4개 존재하는 생성자
    def __init__(self, company, inch, price, color):
        # self.company는 멤버변수를 칭함
        # company는 외부에서 생성자를 호출할 때 매개변수 값으로 들어오는 것을 의미
        self.__company = company
        self.__inch = inch
        self.__price = price
        self.__color = color
    
    # getter() 메서드; 값만 읽어가도록 해주는 메서드
    def getCompany(self):
        return self.__company
    def getInch(self):
        return self.__inch
    def getPrice(self):
        return self.__price
    def getColor(self):
        return self.__color
    
    # setter() 메서드; 멤버변수의 값을 변경시켜주는 메서드
    # 실습을 위해서일 뿐 외부에서 접근하지 못하도록 해야함!; 물론 상황에 따라!! 
    def setCompany(self, company):
        self.__company = company
    def setInch(self, inch):
        self.__inch = inch
    def setPrice(self, price):
        self.__price = price
    def setColor(self, color):
        self.__color = color
    
    # 멤버변수들의 값을 찍어보기 위한 메서드
    def __str__(self):
        print("제조사 :", self.getCompany())
        print("인치 :", self.getInch())
        print("가격 :", self.getPrice())
        print("색상 :", self.getColor())
    
    # # private한 필드의 변경된 값을 확인 불능
    # # 멤버변수들의 값을 찍어보기 위한 메서드
    # def __str__(self):
    #     print("제조사 :", self.__company)
    #     print("인치 :", self.__inch)
    #     print("가격 :", self.__price)
    #     print("색상 :", self.__color)
        
        
        
        
        
        
        
        