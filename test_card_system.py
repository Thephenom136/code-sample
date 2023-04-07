import unittest
from unittest.mock import patch
import card_system
import sys
 
class TestCase(unittest.TestCase):
    def setUp(self):
        self.inFile = sys.argv[1] if len(sys.argv)>1 else ""
        self.clients_limits = {}
        self.clients_accounts = {}
        self.lines = ["Add John Home 4111111111111111 $1000", "Charge John Home $500", "Credit John Home $100"]
 
    def test_add(self):
        expected_clients_limits = {'John_Home': 1000}
        expected_clients_accounts = {'John_Home': 0}
        card_system.add(self.lines[0])
        self.assertEqual(card_system.clients_limits, expected_clients_limits)
        self.assertEqual(card_system.clients_accounts, expected_clients_accounts)
 
    def test_charge(self):
        expected_clients_limits = {'John_Home': 1000}
        expected_clients_accounts = {'John_Home': 500}
        card_system.charge(self.lines[1])
        self.assertEqual(card_system.clients_limits, expected_clients_limits)
        self.assertEqual(card_system.clients_accounts, expected_clients_accounts)
 
    def test_credit(self):
        expected_clients_limits = {'John_Home': 1000}
        expected_clients_accounts = {'John_Home': 400}
        card_system.credit(self.lines[2])
        self.assertEqual(card_system.clients_limits, expected_clients_limits)
        self.assertEqual(card_system.clients_accounts, expected_clients_accounts)

    def test_luhn_check(self):
        self.assertTrue(card_system.luhn_check('4111111111111111'))
        self.assertFalse(card_system.luhn_check('4111111111111112'))
 
if __name__ == '__main__':
    unittest.main()