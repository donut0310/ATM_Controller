import sys
import os

from utils.exception_util import MyError
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from controllers.atm_controller import AtmController
from models.db import Database

def main():
    # 입력받은 핀번호 검증
    input_pin = "0000-aaaa"
    try:
        AtmController.verify_pin_num(input_pin=input_pin)
    except MyError as e:
        print(e)
        return False
        
    # 가상의 데이터베이스 객체 
    # 사용자는 각자 사용하는 데이터베이스 맞게 객체를 생성했다고 가정
    db = Database('sql') # sql cursor 생성
    # db = Database('orm') # orm cursor 생성

    # 컨트롤러 호출 (각자 사용하는 데이터베이스에 맞게 메소드 호출)
    atm_controller = AtmController(db.cursor) # sql
    # atm_controller = AtmController(db.cursor) # orm 등

    # 계정 선택
    selected_account = None
    try:
        # sql인 경우에만 query변수에 sql문 할당
        query = f'select * from users where pin = {input_pin}'
        accounts = atm_controller.find_accounts(input_pin, 'sql', query)
        # accounts = atm_controller.find_accounts(input_pin, 'orm')
        
        selected_account = accounts[0] # 복수 할당인 경우 첫번째 원소를 선택한다고 가정
    except MyError as e:
        print(e)
        return False

    # 계정 입금
    try:
        query = f'update users set money=money+{10000}'
        selected_account = atm_controller.deposit(selected_account, 10000, 'sql', query)
        # selected_account = atm_controller.deposit({}, 10000, 'sql', query)
    except MyError as e:
        print(e)
        return False

    # 계정 출금
    try:
        query = f'update users set money=moeny-{5000}'
        selected_account = atm_controller.withdraw(selected_account, 5000, 'sql', query)
    except MyError as e:
        print(e)
        return False

    # 계정 잔고 조회
    try:
        query = f"select pin,balance from users where pin={selected_account['pin']} and oid={selected_account['oid']}"
        acc_balance = atm_controller.get_balance(selected_account, 'sql', query)
        print(f"{selected_account['name']}'s Valance: {acc_balance}")
    except MyError as e:
        print(e)
        return False

if __name__ == '__main__':
    main()