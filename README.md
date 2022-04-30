## ATM Controller

```python
from atm_controller import AtmController
db = Database() # 사용자 데이터베이스 연결
atm_controller = AtmController(db.cursor) # 컨트롤러 호출
```

***

### Assumption

1. 가상의 데이터베이스 객체 생성

```python
            'service':'sql'|'orm'...,
            'data':[
                {'name':'John','balance':10000,'pin':'0000-aaaa','oid':0},
                {'name':'Lee', 'balance':5000,'pin':'1212-abab','oid':1},
                {'name':'Choi', 'balance':3000,'pin':'0000-aaaa','oid':2}
            ]
```

2. Methods내에서 sql, orm 등에 따른 각 DB 접근은 실제 호출이 아닌 가정된 코드로 진행 

***

### Methods

- **verify_pin_num(input_pin: str)**

  <static method>

  입력받은 핀 번호의 유효성 검사를 진행 후 경우에 따라 True 또는, 커스텀 예외를 반환합니다.

  유효성 검사는 다음과 같은 과정을 거칩니다.

  1. 매개변수의 타입 체크
  2. 매개변수의 포맷 일치 여부 확인

  ```python
  try:
  	AtmController.verify_pin_num(input_pin=input_pin)
  except MyError as e:
  	print(e)
      return False
  ```

  

- **find_accounts(pin: str, service: str, query: str = '')**

  검증을 통과한 핀 번호와 연결된 계정 정보를 조회합니다.

  사용 DB에 맞게 함수 내에서 데이터를 조회합니다.

  ```python
  # pin: 핀 번호
  # service: 사용 DB
  # query: sql 사용시 입력 쿼리문
  # return: [{}]
  # return: False => 예외 발생
  accounts = atm_controller.find_accounts(input_pin, 'sql', query) #or
  accounts = atm_controller.find_accounts(input_pin, 'orm')
  
  # 복수 할당인 경우 첫번째 계정을 선택한다고 가정
  selected_account = accout[0]
  ```

  

- **deposit(account:dict, money:int, service:str, query:str='')**

  선택된 계정에 금액을 입금합니다.

  사용 DB에 맞게 함수 내에서 입금을 진행합니다.

  ```python
  # pin: 핀 번호
  # service: 사용 DB
  # query: sql 사용시 입력 쿼리문
  # account => {'pin':'0000-xxxx', 'oid':0, 'name':'lee'}
  # return: {'name': 'John', 'balance': 15000, 'pin': '0000-aaaa', 'oid': 0}
  # return: False => 예외 발생
  atm_controller.deposit(selected_account, 10000, 'sql', query)
  ```

  

- **withdraw(account:dict, money:int, service:str, query:str='')**

  선택된 계정에 금액을 출금합니다.

  사용 DB에 맞게 함수 내에서 출금을 진행합니다.

  ```python
  # pin: 핀 번호
  # service: 사용 DB
  # query: sql 사용시 입력 쿼리문
  # account => {'pin':'0000-xxxx', 'oid':0, 'name':'lee'}
  # return: {'name': 'John', 'balance': 15000, 'pin': '0000-aaaa', 'oid': 0}
  # return: False => 예외 발생
  atm_controller.withdraw(selected_account, 5000, 'sql', query)
  ```

  

- **get_balance(account:dict, service:str, query:str='')**

  선택된 계정의 잔고를 조회합니다.

  사용 DB에 맞게 함수 내에서 데이터를 조회합니다.

  ```python
  # pin: 핀 번호
  # service: 사용 DB
  # query: sql 사용시 입력 쿼리문
  # account => {'pin':'0000-xxxx', 'oid':0, 'name':'lee'}
  # return: False => 예외 발생
  atm_controller.get_balance(selected_account, 'sql', query)
  ```



***

### Exceptions

- type_exceptions: 매개변수의 타입이 올바르지 않음

  ```python
  Exception: Invalid Type
   => Required type is 'str' type, but type of variable 'input_pin' is '<class 'int'>'
   => Please check the type of variable
  ```

  

- length_exceptions: 핀 번호의 문자열 길이 포맷이 유효하지 않음

  ```python
  Exception: Invalid Format: Length
   => A variable 'input_pin' of length '8' is required, but this variable is length 10
   => Please check the format of a variable 'input_pin'
  ```

  

- format_exceptions: 핀 번호의 문자열 포맷이 유효하지 않음

  ```python
  Exception: Invalid Format
   => Please check the format of a variable 'input_pin'
   => The value of a 'input_pin' is '0000-1111'
  ```

  

- unmatch_db: 데이터베이스가 일치하지 않음

  ```python
  Exception: Unmatch Database
  => Need to use 'SQL' not 'ORM'
  ```

- no_users: 조회된 내역이 없음

  ```python
  Exception: No user in Database
  ```

  

- lack_of_ balance: 출금 가능 잔액이 부족함

  ```python
  Exception: Account balance is insufficient
   => Account balance is '20000'
   => Withdrawal amount is '35000'
  ```

  

- invalid_params: 매개변수의 개수가 다름

  ```python
  Exception: Invalid Parameters
   => This function requires '1' variables
   => but only '2' variable is passed
  ```

  

