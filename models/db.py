class Database():
    '''
    <가정>
    - 데이터베이스 객체에 가상의 유저 3명의 정보가 등록되어 있다고 가정
    '''
    cursor = {}
    def __init__(self, service):
        self.cursor = {
            'service':service,
            'data':[
                {'name':'John','balance':10000,'pin':'0000-aaaa','oid':0},
                {'name':'Lee', 'balance':5000,'pin':'1212-abab','oid':1},
                {'name':'Choi', 'balance':3000,'pin':'0000-aaaa','oid':2}
            ]
        }
    
    