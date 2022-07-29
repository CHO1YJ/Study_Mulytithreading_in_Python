# 은행 게좌에 돈을 저금할 수도 있고 인출을 할 수도 있다.
# 은행 계좌를 간단하게 클래스(Account)로 정의해 보자
# 현재 잔액(balance)을 필드로 정의한다.
# 기본 생성자를 정의하고 입금(deposit) 메서드와 출금(withdraw) 메서드를 정의한다.
# 출력결과는 다음과 같다.
# 출력결과
# 통장에 1,000,000원이 입금됨
# 현재잔액 : 1,000,000원
# 통장에 200,000원이 출금됨
# 현재잔액 : 800,000원
#------------------------------------------------------------------------------

class Account:
    __balance = 0
    
    def __init__(self):
        self.__balance = 0
    
    # 입출금 메서드 정의 필요
    def deposit(self, money):
        self.__balance = self.__balance + money
        print("통장에 " + format(money, ',') + "원이 입금됨")
    def withdraw(self, money):
        if self.__balance - money > 0:
            print("통장에 " + format(money, ',') + "원이 출금됨")
            self.__balance = self.__balance - money
        else:
            print("계좌에 잔액이 없습니다.")
            
    def getBalance(self):
        return self.__balance
    
    def __str__(self):
        print("현재 잔액 :", format(self.getBalance(), ',') + "원")
    
def main():
    account1 = Account()
    account1.deposit(1000000)
    account1.__str__()
    account1.withdraw(200000)
    account1.__str__()
    
    account1.withdraw(900000)
    account1.__str__()
    account1.deposit(400000)
    account1.__str__()

if __name__ == "__main__":
    main()
