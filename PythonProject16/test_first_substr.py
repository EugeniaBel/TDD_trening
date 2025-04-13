import pytest
from first_substr import first_substr

def test_normal_case():
    """Test normal case with valid substring"""
    assert first_substr("animal", "n") == "nim"
    assert first_substr("banana", "n") == "nan"

def test_no_match():
    """Test when character is not found"""
    assert first_substr("airplane", "x") == None
    assert first_substr("hello", "z") == None

def test_short_word():
    """Test when word is too short"""
    assert first_substr("an", "n") == None
    assert first_substr("a", "a") == None

def test_match_at_end():
    """Test when match is at the end"""
    assert first_substr("python", "n") == None
    assert first_substr("coding", "g") == None

def test_multiple_matches():
    """Test when multiple matches exist"""
    assert first_substr("banana", "a") == "ana"
    assert first_substr("parallel", "a") == "ara"

def test_invalid_input():
    """Test invalid input types"""
    assert first_substr(123, "1") == None
    assert first_substr("hello", 1) == None
    assert first_substr("test", "") == None
    assert first_substr("", "a") == None

def test_case_sensitive():
    """Test case sensitivity"""
    assert first_substr("Python", "P") == "Pyt"
    assert first_substr("Python", "p") == None
    assert first_substr("Hello", "H") == "Hel"
