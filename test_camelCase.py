from unittest import TestCase 
import camelCase 

class TestCamelCase(TestCase):

    def test_camelcase_sentance(self):
        self.assertEqual('helloWorld', camelCase.camelcase('Hello World'))
        self.assertEqual('myNameIsJosh', camelCase.camelcase('My name is josh'))

    def test_camelcase_one_word(self):
        self.assertEqual('hello', camelCase.camelcase('HELLO'))

    def test_strings_with_whitespace_at_end(self):
        self.assertEqual('helloWorld', camelCase.camelcase('Hello World  '))

    def test_empty_string(self):
        self.assertEqual('', camelCase.camelcase(''))

    def test_camelcase_string_with_numbers(self):
        self.assertEqual('helloWorld13', camelCase.camelcase('Hello World 1 3'))
        
    def test_camelcase_more_than_one_space(self):
        self.assertEqual('helloWorld', camelCase.camelcase('Hello    World'))

    def test_camelcase_with_new_lines(self):
        self.assertEqual('helloWorldHelloWorld', camelCase.camelcase('Hello World \n Hello World'))

       



    





