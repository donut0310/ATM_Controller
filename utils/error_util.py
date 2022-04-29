class ErrorUtil:
    '''
        status: http status code
        message: error message
    '''
    res = {
        'status': None,
        'message': None,
    }

    def __init__(self, status, msg):
        self.res['status'] = status
        self.res['message'] = msg

    @staticmethod
    def badRequest(msg):
        return ErrorUtil(400,msg).res

    @staticmethod
    def unAuthorized( msg ):
        return ErrorUtil(401, msg).res

    @staticmethod
    def forbidden(msg):
        return ErrorUtil(403, msg).res

    @staticmethod
    def resourceNotFound(msg):
        return ErrorUtil(404, msg).res
    
    @staticmethod
    def conflict(msg):
        return ErrorUtil(409, msg).res
    
    @staticmethod
    def internal(msg):
        return ErrorUtil(500, msg).res
