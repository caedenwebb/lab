class Account:
    def __init__(self, name: str) -> None:
        '''
        Creates a new account for money to be deposited or withdrawn. Balance starts at $0.
        :param name: This is the name on the account.
        :return None
        '''

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: int) -> None:
        '''
        This function deposits a sum of money into an account.
        :param amount: The amount to be deposited.
        :return: None
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance + amount
            return True
    def withdraw(self, amount: int) -> None:
        '''
        This function withdraws a sum of money from an account.
        :param amount: The integer amount to be withdrawn.
        :return: None
        '''
        if (amount <= 0 or amount > self.__account_balance):
            return False
        else:
            self.__account_balance = self.__account_balance - amount
            return True
    def get_balance(self) -> int:
        '''
        This function returns the balance of the account.
        :return: Account Balance
        '''
        return self.__account_balance
    def get_name(self) -> str:
        '''
        This function returns the name of the account
        :return: Name of the Account
        '''
        return self.__account_name
