class MyError(Exception):
    res ={
        'msg':'',
        'status':False
    }
    def __init__(self, msg):
        self.res['msg'] = msg

    def length_exception(needs:int, input:int, v:str):
        msg = f"Exception: Invalid Format: Length\n => A variable '{v}' of length '{needs}' is required, but this variable is length {input}\
            \n => Please check the format of a variable '{v}'"
        raise MyError(msg)

    def format_exception(input:str, v:str):
        msg = f"Exception: Invalid Format\
            \n => Please check the format of a variable '{v}'\
            \n => The value of a '{v}' is {input}'"
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

    def invalid_params(needs, input):
        msg = f"Exception: Invalid Parameters\
            \n => This function requires '{needs}' variables\
            \n => but only '{input}' variable is passed"
        raise MyError(msg)