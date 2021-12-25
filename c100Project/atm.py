class atm(object):

# self is used to access the properties of an object
# init means to initialize the attributes
#def = function (in python format)

    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    
    def CashWithdrawl (self):
        print('cash withdrawed')

    def BalanceEnquiry(self):
        print('balance enquiried')


Info = atm("123456","432789")
print(Info.cardNumber)
print(Info.pinNumber)



    