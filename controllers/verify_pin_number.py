'''
<가정>
- ATM_Controller에서 제공하는 pin_number 포맷팅은 "(숫자)XXXX-(영문 대소문자)XXXX"로 가정
'''
from utils.exception_util import MyError
import re

def verify_pin_num(pin_num:any):
    ''' 
    <Verification process>
    1. Type check => Allow only for strings
    2-1. Format check => Verify regex and length
    2-2. Exception check
    '''
    
    # Type Check
    if not isinstance(pin_num, str):
        MyError.pinType_exception(type(pin_num))

    # Format Check
    if len(pin_num) > 9:
        MyError.length_exception(pin_num)

    regex = re.compile(r'(\d{4})-([a-zA-Z]{4})')
    if not regex.search(pin_num):
        MyError.format_exception(pin_num)

    return True

