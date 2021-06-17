# Import all required modules

from unittest import TestCase
from src.email_parser import EmailParser


class TestEmailParser(TestCase):

    def setUp(self):
        self.test_case = EmailParser()

    def test_parse(self):
        self.assertEqual(self.test_case.parse(
            'johndoe@gmail.com'), {"username": "johndoe", "domain": "gmail.com"})

    def test_parse_2(self):
        self.assertEqual(self.test_case.parse('john@doe@gmail.2com'), None)

    def test_parse_3(self):
        self.assertEqual(self.test_case.parse(
            'john+doe@gmail.com'), {"username": "john+doe", "domain": "gmail.com"})

    def test_parse_4(self):
        self.assertEqual(self.test_case.parse(
            'williem@yahoo.com'), {"username": "williem", "domain": "yahoo.com"})

    def test_parse_5(self):
        self.assertEqual(self.test_case.parse('2johndoe@gmail.2com'), None)

    def test_parse_6(self):
        self.assertEqual(self.test_case.parse('abraham_doe@gmail.com'), None)

    def test_parse_7(self):
        self.assertEqual(self.test_case.parse('+eze@gmail.com'), None)

    def test_parse_8(self):
        self.assertEqual(self.test_case.parse('actionbitters+gmail.com'), None)

    def test_parse_9(self):
        self.assertEqual(self.test_case.parse('muza iza@xyz.com'), None)

    def test_parse_10(self):
        self.assertEqual(self.test_case.parse('manofGod.com'), None)
