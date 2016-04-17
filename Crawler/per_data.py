


class Inf(object):#data为一个list，每一个元素为一个list或元祖都可以
    def __init__(self):
        self.id = 0
        self.name= ''
        self.gender = ''
        self.partner_id = ''
        self.status = ''
        self.date = ''
        self.interation=  ''

    def append(self,id,name,gender,partner_id,status,date):
        self.id = id
        self.name = name
        self.gender = gender
        self.partner_id = partner_id
        self.status =  status
        self.date = date
 

