import unittest

from scraper import get_question_content, get_question_header
from utils import given_html_with_complex_header, given_html_without_header, given_simple_html


class TestScraper(unittest.TestCase):
    def test_extracts_simple_header(self):
        html_content = given_simple_html()
        expected_header = "How do I python?"
        actual_header = self.when_extracting_header(html_content)
        self.then_finds_correct_header(actual_header, expected_header)

    def test_returns_none_if_no_header(self):
        html_content = given_html_without_header()
        actual_header = self.when_extracting_header(html_content)
        self.then_finds_correct_header(actual_header, None)

    def test_extracts_complex_header(self):
        html_content = given_html_with_complex_header()
        expected_header = "This <> is a super complex HEADER || since it contains {} signs"
        actual_header = self.when_extracting_header(html_content)
        self.then_finds_correct_header(actual_header, expected_header)

    def test_extracts_simple_content(self):
        html_content = given_simple_html()
        expected_content = ('I know that some other languages, such as PHP, support a concept of "variable variable '
                            'names" - that is, the contents of a string can be used as part of a variable name. I '
                            'heard that this is a bad idea in general, but I think it would solve some problems I '
                            'have in my Python code. Is it possible to do something like this in Python? What can go '
                            'wrong?')
        actual_content = self.when_extracting_question_content(html_content)
        self.then_finds_correct_header(actual_content, expected_content)

    def when_extracting_header(self, html_content):
        return get_question_header(html_content)

    def when_extracting_question_content(self, html_content):
        return get_question_content(html_content)

    def then_finds_correct_header(self, actual_header, expected_header):
        self.assertEqual(actual_header, expected_header)


if __name__ == '__main__':
    unittest.main()
