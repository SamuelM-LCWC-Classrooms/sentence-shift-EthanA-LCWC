import pytest
from task import shift_sentence

def test_1():
    assert shift_sentence("create a function") == "freate c aunction"

def test_2():
    assert shift_sentence("it should shift the sentence") == "st ihould shift she tentence"

def test_3():
    assert shift_sentence("the output is not very legible") == "lhe tutput os iot nery vegible"

def test_4():
    assert shift_sentence("edabit") == "edabit"