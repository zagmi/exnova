import unittest
import os
from exnova.stable_api import ExNova

email = os.getenv("email")
password = os.getenv("password")


class TestLogin(unittest.TestCase):

    def test_login(self):
        I_want_money = ExNova(email, password)
        I_want_money.change_balance("PRACTICE")
        I_want_money.reset_practice_balance()
        self.assertEqual(I_want_money.check_connect(), True)
