import re

from utils.exception_util import MyError
from utils.validation import Validation

class AtmController():
    data={}
    def __init__(self, db):
        self.data = db
    
    @staticmethod
    # 핀번호 검증
    def verify_pin_num(**args:str):
        ''' 
        <Verification process>
        1. Type check => Allow only for strings
        2-1. Format check => Verify regex and length
        2-2. Exception check
        '''
        if len(args)!=1:
            MyError.invalid_params(1,len(args))
        v = list(args.keys())[0]
        pin = args[v]

        # Type Check
        if not isinstance(pin, str):
            MyError.type_exception('str', type(pin), v)

        # Format Check
        if len(pin) > 9:
            MyError.length_exception(8, len(pin), v)

        regex = re.compile(r'(\d{4})-([a-zA-Z]{4})')
        if not regex.search(pin):
            MyError.format_exception(pin, v)

        return True

    # 계정 선택
    def find_accounts(self, pin:str, service:str, query:str=''):
        # verify parameter type
        if not Validation.isStr(pin):
            MyError.type_exception('str', type(pin), "pin")
        if not Validation.isStr(service):
            MyError.type_exception('str', type(service), "service")
        if not Validation.isStr(query):
            MyError.type_exception('str', type(query), "query")

        # 아래 코드는 데이터베이스 조회를 가정
        users = []
        if service == 'sql':
            for i in self.data['data']:
                if i['pin'] == pin:
                    users.append(i)
        elif service == 'orm':
            for i in self.data['data']:
                if i['pin'] == pin:
                    users.append(i)
        if not users: # 조회된 데이터가 없거나 DB 에러인 경우
            MyError.no_users()
        else: return users

    # 계정 입금
    def deposit(self, account:dict, money:int, service:str, query:str=''): 
        # verify parameter type
        if not Validation.isDict(account):
            MyError.type_exception('dict', type(account), "account")
        if not Validation.isInt(money):
            MyError.type_exception('int', type(money), "money") 
        if not Validation.isStr(service):
            MyError.type_exception('str', type(service), "service")
        if not Validation.isStr(query):
            MyError.type_exception('str', type(query), "query")

        _service = self.data['service']

        # verify database type
        if _service != service:
            MyError.unmatch_db(_service, service) 

        if not account.keys():
            MyError.no_users()

        # 아래 코드는 DB 호출을 가정
        user = None
        for i in range(len(self.data['data'])):
            if self.data['data'][i]['pin']==account['pin'] and self.data['data'][i]['oid'] == account['oid']:
                self.data['data'][i]['balance'] += money
                user = self.data['data'][i]
                return user
        # DB호출 결과가 없거나 DB상 에러인 경우
        MyError.no_users()

    # 계정 출금
    def withdraw(self,account:dict, money:int, service:str, query:str=''):
        # verify parameter type
        if not Validation.isDict(account):
            MyError.type_exception('dict', type(account), "account")
        if not Validation.isInt(money):
            MyError.type_exception('int', type(money), "money") 
        if not Validation.isStr(service):
            MyError.type_exception('str', type(service), "service")
        if not Validation.isStr(query):
            MyError.type_exception('str', type(query), "query")
        
        _service = self.data['service']

        # verify database type
        if _service != service:
            MyError.unmatch_db(_service, service) 

        if not account.keys():
            MyError.no_users()

        # 아래 코드는 DB 호출을 가정
        user = None
        for i in range(len(self.data['data'])):
            if self.data['data'][i]['pin']==account['pin'] and self.data['data'][i]['oid'] == account['oid']:
                acc_balance = self.data['data'][i]['balance']
                # 잔고보다 적은경우     예외 처리 
                if acc_balance < money:
                    MyError.lack_of_balance(acc_balance, money)

                self.data['data'][i]['balance'] -= money
                user = self.data['data'][i]     
                return user
        # DB호출 결과가 없거나 DB상 에러인 경우
        MyError.no_users()

    # 계정 잔고 조회
    def get_balance(self, account:dict, service:str, query:str=''):
        # verify parameter type
        if not Validation.isDict(account):
            MyError.type_exception('dict', type(account), "account")
        if not Validation.isStr(service):
            MyError.type_exception('str', type(service), "service")
        if not Validation.isStr(query):
            MyError.type_exception('str', type(query), "query")

        _service = self.data['service']

        # verify database type
        if _service != service:
            MyError.unmatch_db(_service, service) 

        if not account.keys():
            MyError.no_users()

        # 아래 코드는 DB 호출을 가정
        for i in range(len(self.data['data'])):
            if self.data['data'][i]['pin']==account['pin'] and self.data['data'][i]['oid'] == account['oid']:
                return self.data['data'][i]['balance']

        # DB호출 결과가 없거나 DB상 에러인 경우
        MyError.no_users()
