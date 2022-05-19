from the_bank import Bank, Account


bank = Bank()
John = Account("John Smith",
               value=2000,
               zipvalue='qwertyuio',
               ok=1
               )
Gerard = Account("Gerard Smith")
print(John.__dict__)
print(Gerard.__dict__)
bank.add(John)
bank.add(Gerard)
ret = bank.transfer(John, Gerard, 200)
print("tranfert John to Gerard: {}".format(ret))

print('delete Gerard attributes: ')
delattr(Gerard, 'name')
delattr(Gerard, 'id')
print(Gerard.__dict__)

print('fix Gerard: ')
print(bank.fix_account(Gerard))
print(bank.fix_account(['ok']))
print(Gerard.__dict__)
ret = bank.transfer(John, Gerard, 200)
print("tranfert John to Gerard: {}".format(ret))
ret = bank.transfer("John Smith", 3, 200)
print("tranfert John to Gerard: {}".format(ret))
ret = bank.transfer("John Smith", Gerard.name, 200)
print("tranfert John to Gerard: {}".format(ret))
ret = bank.transfer("John Smith", 4, 200)
print("tranfert error: {}".format(ret))
ret = bank.transfer("John", 3, 200)
print("tranfert error: {}".format(ret))
ret = bank.transfer(1, 2, 200)
print("tranfert error: {}".format(ret))
