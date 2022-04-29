class Validation():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def isStr(*args):
        for arg in args:
            if not isinstance(arg,str):
                return False
        return True

    @staticmethod
    def isInt(*args):
        for arg in args:
            if not isinstance(arg,int):
                return False
        return True

    @staticmethod
    def isBoolean(*args):
        for arg in args:
            if not isinstance(arg,bool):
                return False
        return True

    @staticmethod
    def isDict(*args):
        for arg in args:
            if not isinstance(arg,dict):
                return False
        return True
