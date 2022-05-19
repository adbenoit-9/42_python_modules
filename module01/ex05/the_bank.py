class Account(object):
    
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    '''The bank'''
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def find_by_id(self, id):
        for account in self.account:
            if account.id == id:
                return account

    def find_by_name(self, name):
        for account in self.account:
            if account.name == name:
                return account

    def get_account(self, info):
        if isinstance(info) is int:
            return self.find_by_id(info)
        elif isinstance(info) is str:
            return self.find_by_name(info)
        else:
            return info

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        origin = self.get_account(origin)
        dest = self.get_account(dest)
        if isinstance(origin) is not Account or isinstance(origin) is not Account:
            return False
        if amount < 0 or amount < origin.balance:
            return False
        print(dir(origin))


    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return True if success, False if an error occured
        """

John = Account("John Smith", balance=2000)
Gerard = Account("Gerard Smith", balance=2000)

bank = Bank()

bank.transfer(John, Gerard, 200)
