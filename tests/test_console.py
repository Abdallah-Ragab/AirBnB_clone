import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.console.onecmd('')
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        self.console.onecmd('quit')
        self.assertEqual(mock_stdout.getvalue(), '')
        self.assertTrue(self.console.quit)

    # Add more test methods for other commands

if __name__ == '__main__':
    unittest.main()
