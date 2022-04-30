from this import d
from unittest import TestCase, main
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from utils.validation import Validation


'''
<가정>
- ATM_Controller에서 제공하는 pin_number 포맷팅은 "(숫자)XXXX-(영문 대소문자)XXXX"로 가정
'''
import re


# 핀번호 검증
def verify_pin_num(**args:str):
    if len(args)!=1:
        print(f"Exception: Invalid Parameters")
        return False
    v = list(args.keys())[0]
    pin = args[v]

    # Type Check
    if not isinstance(pin, str):
        print("Exception: Invalid Type 'str': pin")
        return False

    # Format Check
    if len(pin) > 9:
        print(f"Exception: Invalid Format: Length")
        return False

    regex = re.compile(r'(\d{4})-([a-zA-Z]{4})')
    if not regex.search(pin):
        print(f"Exception: Invalid Forma: Regex")
        return False

    print("success")
    return True

# 계정 선택
def find_accounts(data:dict, pin:str, service:str, query:str=''):
        # verify parameter type
        if not Validation.isStr(pin):
            print(f"Exception: Invalid Type 'str': pin")
            return False
        if not Validation.isStr(service):
            print(f"Exception: Invalid Type 'str': service")
            return False
        if not Validation.isStr(query):
            print(f"Exception: Invalid Type 'str': query")
            return False

        # 아래 코드는 데이터베이스 조회를 가정
        users = []
        if service == 'sql':
            for i in data['data']:
                if i['pin'] == pin:
                    users.append(i)
        elif service == 'orm':
            for i in data['data']:
                if i['pin'] == pin:
                    users.append(i)
        if not users: # 조회된 데이터가 없거나 DB 에러인 경우
            print("Exception: No Users")
            return False
        else: 
            print("success")
            return True

def deposit(data:dict,account:dict, money:int, service:str, query:str=''): 
        # verify parameter type
        if not Validation.isDict(account):
            print(f"Exception: Invalid Type 'dict': account")
            return False
        if not Validation.isInt(money):
            print(f"Exception: Invalid Type 'int': money")
            return False
        if not Validation.isStr(service):
            print(f"Exception: Invalid Type 'str': service")
            return False
        if not Validation.isStr(query):
            print(f"Exception: Invalid Type 'str': query")
            return False

        _service = data['service']

        # verify database type
        if _service != service:
            print("Exception: Unmatch Database")
            return False
        
        if not account.keys():
            print("Exception: No Users")
            return False
        # 아래 코드는 DB 호출을 가정
        user = None
        for i in range(len(data['data'])):
            if data['data'][i]['pin']==account['pin'] and data['data'][i]['oid'] == account['oid']:
                data['data'][i]['balance']-= money
                user = data['data'][i]
                print("success")
                return True
        # DB호출 결과가 없거나 DB상 에러인 경우
        print("Exception: No Users")
        return False

def withdraw(data:dict,account:dict, money:int, service:str, query:str=''):
        # verify parameter type
        if not Validation.isDict(account):
            print(f"Exception: Invalid Type 'dict': account")
            return False
        if not Validation.isInt(money):
            print(f"Exception: Invalid Type 'int', money")
            return False
        if not Validation.isStr(service):
            print(f"Exception: Invalid Type 'str', service")
            return False
        if not Validation.isStr(query):
            print(f"Exception: Invalid Type 'str', query")
            return False
        
        _service = data['service']

        # verify database type
        if _service != service:
            print("Exception: Unmatch Database")
            return False
        
        if not account.keys():
            print("Exception: No Users")
            return False
        # 아래 코드는 DB 호출을 가정
        user = None
        for i in range(len(data['data'])):
            if data['data'][i]['pin']==account['pin'] and data['data'][i]['oid'] == account['oid']:
                acc_balance = data['data'][i]['balance']
                # 잔고보다 적은 경우 
                if acc_balance < money:
                    print("Exception: Lack of balance")
                    return False
                data['data'][i]['balance'] -= money
                user = data['data'][i]     
                print("Success")
                return True
        # DB호출 결과가 없거나 DB상 에러인 경우
        print("Exception: No Users")
        return False

def get_balance(data:dict, account:dict, service:str, query:str=''):
    # verify parameter type
    if not Validation.isDict(account):
        print(f"Exception: Invalid Type: 'dict': account")
        return False
    if not Validation.isStr(service):
        print(f"Exception: Invalid Type 'str': service")
        return False
    if not Validation.isStr(query):
        print(f"Exception: Invalid Type: 'str': query")
        return False

    _service = data['service']

    # verify database type
    if _service != service:
        print("Exception: Unmatch Database")
        return False

    if not account.keys():
        print("Exception: No Users")
        return False
        
    # 아래 코드는 DB 호출을 가정
    for i in range(len(data['data'])):
        if data['data'][i]['pin']==account['pin'] and data['data'][i]['oid'] == account['oid']:
            # return data['data'][i]['balance']
            print("Success")
            return True

    # DB호출 결과가 없거나 DB상 에러인 경우
    print("Exception: No Users")
    return False

        
class MyTests(TestCase):

    # 핀번호 검증
    def test_verify_pin_num(self):
        print("\n핀번호 검증")

        input_pin = "0000-aaaa"
        self.assertTrue(verify_pin_num(input_pin=input_pin))
        input_pin = "0000-aaaass"
        self.assertFalse(verify_pin_num(input_pin=input_pin))
        input_pin = "0000-aa11"
        self.assertFalse(verify_pin_num(input_pin=input_pin))
        input_pin = "aaaa@1111"
        self.assertFalse(verify_pin_num(input_pin=input_pin))
        print('-------------------------------------------------------')

    # 계정 선택
    def test_find_accounts(self):
        print("\n계정 선택")
        data = {
            'service':'',
                'data':[
                    {'name':'John','balance':10000,'pin':'0000-aaaa','oid':0},
                    {'name':'Lee', 'balance':5000,'pin':'1212-abab','oid':1},
                    {'name':'Choi', 'balance':3000,'pin':'0000-aaaa','oid':2}
                ]
        }
        #sql, pass
        data['service'] ='sql'
        input_pin = '0000-aaaa'
        query = f'select * from users where pin = {input_pin}'
        self.assertTrue(find_accounts(data,input_pin, 'sql', query))
        
        # sql, 유저 없는 경우
        input_pin = '0000-gggg'
        self.assertFalse(find_accounts(data,input_pin, 'sql', query))
        
        #orm, pass
        data['service'] = 'orm' 
        input_pin = '0000-aaaa'
        self.assertTrue(find_accounts(data,input_pin, 'orm'))
        
        # orm, 유저 없는 경우
        input_pin = '0000-gggg'
        self.assertFalse(find_accounts(data,input_pin, 'orm'))

    # 입금
    def test_deposit(self):
        print("\n입금")
        data = {
            'service':'',
                'data':[
                    {'name':'John','balance':10000,'pin':'0000-aaaa','oid':0},
                    {'name':'Lee', 'balance':5000,'pin':'1212-abab','oid':1},
                    {'name':'Choi', 'balance':3000,'pin':'0000-aaaa','oid':2}
                ]
        }
        selected_account = {'name': 'John', 'balance': 20000, 'pin': '0000-aaaa', 'oid': 0}
        
        # sql
        data['service'] = 'sql'
        query = f'update users set money=money+{5000}'
        self.assertTrue(deposit(data,selected_account, 10000, 'sql', query))

        # 파라미터 타입 불일치
        self.assertFalse(deposit(data,selected_account,'10000','sql', query))
        
        # orm 
        data['service'] = 'orm'
        self.assertTrue(deposit(data,selected_account, 10000, 'orm'))

        # sql or orm, 선택된 계정이 없는 경우
        selected_account = {}
        self.assertFalse(deposit(data,selected_account, 10000, 'orm'))
        print('-------------------------------------------------------')


    # 출금
    def test_withdraw(self):
        print("\n출금")
        data = {
            'service':'',
                'data':[
                    {'name':'John','balance':10000,'pin':'0000-aaaa','oid':0},
                    {'name':'Lee', 'balance':5000,'pin':'1212-abab','oid':1},
                    {'name':'Choi', 'balance':3000,'pin':'0000-aaaa','oid':2}
                ]
        }
        selected_account = {'name': 'John', 'balance': 20000, 'pin': '0000-aaaa', 'oid': 0}

        # sql
        data['service'] = 'sql'
        query = f'update users set money=money-{5000}'
        self.assertTrue(withdraw(data,selected_account, 10000, 'sql', query))
        data['data'][0]['balance'] += 10000

        # 파라미터 타입 불일치
        self.assertFalse(withdraw(data,selected_account,'10000','sql',query))

        # orm 
        data['service'] = 'orm'
        self.assertTrue(withdraw(data,selected_account, 10000, 'orm'))
        data['data'][0]['balance'] += 10000

        # sql or orm, 금액 부족
        self.assertFalse(withdraw(data, selected_account, 30000, 'orm'))
        selected_account['balance'] +=30000

        # sql or orm, 선택된 계정이 없는 경우
        selected_account = {}
        self.assertFalse(withdraw(data,selected_account, 10000, 'orm'))
        print('-------------------------------------------------------')

    # 잔고 조회
    def test_get_balance(self):
        print("\n잔고 조회")
        data = {
            'service':'',
                'data':[
                    {'name':'John','balance':10000,'pin':'0000-aaaa','oid':0},
                    {'name':'Lee', 'balance':5000,'pin':'1212-abab','oid':1},
                    {'name':'Choi', 'balance':3000,'pin':'0000-aaaa','oid':2}
                ]
        }
        selected_account = {'name': 'John', 'balance': 20000, 'pin': '0000-aaaa', 'oid': 0}
        query = f"select pin,balance from users where pin={selected_account['pin']} and oid={selected_account['oid']}"
        # sql
        data['service'] = 'sql'
        self.assertTrue(get_balance(data, selected_account,'sql',query))

        # 파라미터 타입 불일치
        self.assertFalse(get_balance(data,[],'sql',query))

        # orm
        data['service'] = 'orm'
        self.assertTrue(get_balance(data,selected_account,'orm',query))

        # sql or orm, 선택된 계정이 없는 경우
        selected_account = {}
        self.assertFalse(get_balance(data, selected_account, 'orm'))
        print('-------------------------------------------------------')

if __name__ == '__main__':
    main()