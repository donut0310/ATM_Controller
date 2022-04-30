'''
<가정>
- ATM_Controller에서 제공하는 pin_number 포맷팅은 "(숫자)XXXX-(영문 대소문자)XXXX"로 가정
'''
from utils.exception_util import MyError
import re

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

