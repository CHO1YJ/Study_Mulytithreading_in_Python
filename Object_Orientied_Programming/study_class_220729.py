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
        self.balance = 0
    
    # 입출금 메서드 정의 필요
    
def main():
    account1 = Account()
    
    # 은행 업무 코드 필요

if __name__ == "__main__":
    main()