import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from middlewares.verify_pin_number import verify_pin_num
from controllers.atm_controller import atm
from models.db import Database

'''
가상의 url을 통해 API 호출이 진행됐다는 가정하에 진행
'''
"""Check the balance for the entered account"""
def main():
    res = {} # 가상의 response 객체
    # 입력받은 핀번호 및 검증
    input_pin = "0000-aaaa"
    pin = verify_pin_num(res, input_pin)

    # 가상의 데이터베이스 객체 
    # (구현 대상은 아니지만 샘플 코드의 실행을 위해서 간단하게 구현했다 가정) 
    """ 데이터베이스 객체 연결 구현하기"""
    # CASH_BIN = Database() 

    # # 컨트롤러 호출 및 데이터베이스 연동
    # atm_controller = atm(CASH_BIN)

    # # 계정 선택
    # accounts = atm_controller.find_accounts(pin)
    # selected_account = accounts[0]

    # # 해당 계정의 잔고 호출
    # print("%s's Valance: %s \n" % (
    #     selected_account,
    #     atm_controller.get_balance(selected_account)
    # ))

if __name__ == '__main__':
    main()