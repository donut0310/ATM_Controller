from error_util import ErrorUtil

class ResponseUtil():
    res = {
        'success': None,
        'results': '',
        'code': None,
        'message': ''
    }
    def __init__(self, isSuccess, data, msg, code):
        self.res['success'] = isSuccess
        self.res['data'] = data
        self.res['msg'] = msg
        self.res['code'] = code

    @staticmethod
    def success_true(data:str):
        return ResponseUtil(True, data, '', 200)
        
    @staticmethod
    def success_false(err:ErrorUtil):
        # err: controller에서 생성된 error util 객체
        return ResponseUtil(err.status, None, err.message, err.code)
