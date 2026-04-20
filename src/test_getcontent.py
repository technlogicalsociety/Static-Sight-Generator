import unittest
from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_extract_title(self):
        result = extract_title("# Hello")
        self.assertEqual(result, "Hello")

    def test_extract_title_longer(self):
        result = extract_title("# My cool website")
        self.assertEqual(result, "My cool website")

    def test_extract_title_no_h1(self):
        with self.assertRaises(Exception):
            extract_title("No header here")
