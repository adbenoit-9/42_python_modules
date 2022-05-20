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
        if isinstance(account, Account) is False:
            raise ValueError("Invalid Type")
        if self.find_by_name(account.name) is not None:
            account.name += "_{id}"
            account.name = account.name.format(id=account.id)
        self.account.append(account)

    def find_by_id(self, id):
        for account in self.account:
            if account.id == id:
                return account
        return None

    def find_by_name(self, name):
        for account in self.account:
            if account.name == name:
                return account
        return None

    def get_account(self, account):
        if isinstance(account, int) is True:
            return self.find_by_id(account)
        elif isinstance(account, str) is True:
            return self.find_by_name(account)
        return None

    def is_corrupted(self, account):
        attr = dir(account)
        if len(attr) % 2 == 0 or \
                'name' not in attr or \
                'id' not in attr or \
                'value' not in attr:
            return True
        ret = True
        for elem in attr:
            if elem.startswith('b') is True:
                return True
            if elem.startswith('zip') is True or \
                    elem.startswith('addr') is True:
                ret = False
        return ret

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        origin = self.get_account(origin)
        dest = self.get_account(dest)
        if origin is None or dest is None:
            return False
        elif self.is_corrupted(origin) is True:
            return False
        elif self.is_corrupted(dest) is True:
            return False
        if isinstance(amount, float) is False and \
                isinstance(amount, int) is False:
            return False
        elif amount < 0 or amount > origin.value:
            return False
        return True

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return True if success, False if an error occured
        """
        tofix = self.get_account(account)
        if tofix is None:
            return False
        attr = dir(tofix)
        attr_zip = 0
        for elem in attr:
            if elem.startswith('b') is True:
                delattr(tofix, elem)
            if elem.startswith('zip') is True or \
                    elem.startswith('addr') is True:
                attr_zip = 1
        if attr_zip == 0:
            setattr(tofix, 'zipcode', '1234')
        if 'id' not in attr:
            setattr(tofix, 'id', tofix.ID_COUNT)
            Account.ID_COUNT += 1
        if 'name' not in attr:
            setattr(tofix, 'name', 'unknown{}'.format(tofix.id))
        if 'value' not in attr:
            setattr(tofix, 'value', 0)
        if len(attr) % 2 == 0:
            setattr(tofix, 'useless', 0)
        return True
