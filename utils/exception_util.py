from utils.error_util import ErrorUtil

class Exception():
    def __init__(self, msg):
        self.msg = msg

    @staticmethod
    def type_exception(pin_type):
        msg = f"Exception: Invalid Type\n => The type of variable 'input_pin' is {pin_type}\
            \n => Please check the type of pin number'"
        Exception(msg)
        return msg

    @staticmethod
    def length_exception(pin_num):
        msg = f"Exception: Invalid Format: Length\n => The value of variable is 'input_pin' is {pin_num}\
            \n => Please check the format of pin number'"
        Exception(msg)
        return msg

    @staticmethod
    def format_exception(pin_num):
        msg = f"Exception: Invalid Format\n => The value of variable is 'input_pin' is {pin_num}\
            \n => Please check the format of pin number'"
        Exception(msg) 
        return msg