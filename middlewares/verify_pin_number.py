# pin number 검증

'''
1. 각 은행은 pin number를 전송한다.
2. ATM_Controller에서 정의한 format이 아닌 경우 예외 반환처리
3. ATM_Controller에서 제공하는 pin_number 포맷팅은 "(숫자)XXXX-(영문 대소문자)XXXX"로 가정
'''
from utils.error_util import ErrorUtil
from utils.exception_util import Exception
import re

def verify_pin_num(res, pin_num):
    # verification process
    # 1. type check => Allow only for strings - clear
    # 2-1. format check => regex verification
    # 2-2. exception check

    # Type Check
    if not isinstance(pin_num, str): # isinstance => 특정 객체가 해당 클래스의 인스턴스인지도 확인 가능
        res = ErrorUtil.badRequest(Exception.type_exception(type(pin_num))) # 에러 객체 반환
        return res # 클라이언트로 응답함을 가정

    # Format Check
    # ATM_Controller에서 제공하는 pin_number 포맷팅은 영문 대소문자 + 숫자로 가정
    if len(pin_num) > 9:
        res = ErrorUtil.badRequest(Exception.length_exception(pin_num))
        print(res)
        return res 

    regex = re.compile(r'(\d{4})-([a-zA-Z]{4})')
    if not regex.search(pin_num):
        res = ErrorUtil.badRequest(Exception.format_exception(pin_num))
        print(res)
        return res 

