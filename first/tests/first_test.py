from first.first import greeting

# write unit tests for the function greeting(name, language) in first/first.py
# include different test cases by writing different unit tests
# their names should reflect the test case, e.g. test_greeting_eng() if english is selected
# use assert to check that your output matches your expectation: assert greeting(name, language) == "expected string"
# when you have new tests ready, try to run pytest to see if they clear: pytest
# if you like, add other languages to your greeting() function and test for them
# add your changes: git add first/tests/first_test.py
# commit your changes using commit message conventions (https://inpred.github.io/24-03_bioinfo_ws/#19): git commit -m "test: <your commit message>"

def test_unknown_language():
    assert greeting("somename", "French") == "I don't speak your language!"

def test_english():
    assert greeting("Sam", "English") == "Hello Sam!"

def test_norwegian():
    assert greeting("Sam", "Norwegian") == "Hei Sam!"

