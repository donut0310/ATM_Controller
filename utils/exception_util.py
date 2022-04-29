class MyError(Exception):
    res ={
        'msg':'',
        'status':False
    }
    def __init__(self, msg):
        self.res['msg'] = msg

    def pinType_exception(pin_type:any):
        msg = f"Exception: Invalid Type\n => The type of variable 'input_pin' is {pin_type}\
            \n => Please check the type of pin number'"
        raise MyError(msg)

    def length_exception(pin_num:str):
        msg = f"Exception: Invalid Format: Length\n => The value of variable is 'input_pin' is {pin_num}\
            \n => Please check the format of pin number'"
        raise MyError(msg)

    def format_exception(pin_num:str):
        msg = f"Exception: Invalid Format\n => The value of variable is 'input_pin' is {pin_num}\
            \n => Please check the format of pin number'"
        raise MyError(msg)

    def unmatch_db(need_type:str, db_type:str):
        msg = f"Exception: Unmatch Database\n=> Need to use '{need_type}' not '{db_type.upper()}'"
        raise MyError(msg)

    def no_users():
        msg = f"Exception: No user in Database"
        raise MyError(msg)
    
    def type_exception(need_type:str, v_type:any, v:str):
        msg = f"Exception: Invalid Type\n => Required type is '{need_type}' type, but type of variable '{v}' is '{v_type}'\
            \n => Please check the type of variable'"
        raise MyError(msg)

    def lack_of_balance(acc_balance, withdrawal):
        msg = f"Exception: Account balance is insufficient\
            \n => Account balance is '{acc_balance}'\
            \n => Withdrawal amount is '{withdrawal}'"
        raise MyError(msg)