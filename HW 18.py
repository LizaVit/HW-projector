#Write a test for the Bank class that we wrote in 14 lesson. You should write a test for the open_account method. Ensure that the account is opened and has balance.
#Test update method. It should check that code added interest and sent a message (print function was called).

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self._interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self._balance * self._interest_rate
        self._balance += interest_amount


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self._balance < 0:
            print(f"Letter sent to account {self._account_number}: You are in overdraft.")


class Bank:
    def __init__(self):
        self._accounts = []

    def open_account(self, account):
        self._accounts.append(account)

    def close_account(self, account_number):
        self._accounts = [acc for acc in self._accounts if acc.get_account_number() != account_number]

    def pay_dividend(self, dividend):
        for account in self._accounts:
            account.deposit(dividend)

    def update(self):
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def __str__(self):
        return '\n'.join(str(account) for account in self._accounts)


savings_acc = SavingsAccount(1000, 'SA001', 0.05)
current_acc = CurrentAccount(500, 'CA001', -1000)
normal_acc = Account.create_account('NA001')

bank = Bank()
bank.open_account(savings_acc)
bank.open_account(current_acc)
bank.open_account(normal_acc)

print("Accounts before update:")
print(bank)

bank.update()

print("\nAccounts after update:")
print(bank)

bank.pay_dividend(50)
print("\nAccounts after paying dividend:")
print(bank)



import unittest

class TestBank(unittest.TestCase):
    def test_open_account(self):
        bank = Bank()
        initial_balance = 1000
        account_number = 'SA001'
        interest_rate = 0.05

        savings_acc = SavingsAccount(initial_balance, account_number, interest_rate)

        bank.open_account(savings_acc)

        self.assertIn(savings_acc, bank._accounts)
        self.assertEqual(savings_acc.get_balance(), initial_balance)

    def test_update_method(self):
        bank = Bank()
        initial_balance = 1000
        account_number = 'SA001'
        interest_rate = 0.05

        savings_acc = SavingsAccount(initial_balance, account_number, interest_rate)
        bank.open_account(savings_acc)

        initial_balance_current = 500
        account_number_current = 'CA001'
        overdraft_limit = -1000

        current_acc = CurrentAccount(initial_balance_current, account_number_current, overdraft_limit)
        bank.open_account(current_acc)

        with unittest.mock.patch('builtins.print') as mock_print:
            bank.update()

        mock_print.assert_called_once_with("Letter sent to account CA001: You are in overdraft.")
        self.assertAlmostEqual(savings_acc.get_balance(), initial_balance * (1 + interest_rate))


if __name__ == '__main__':
    unittest.main()
