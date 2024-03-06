"""Test case for lexical analyzer."""
# Standard library


# 3rd Party library

import pytest

# Project library
from calculator.token import Token, TokenType
from calculator.lexer import Lexer


#-----------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_token, new_pos",
    [
        ("456", 0, Token(TokenType.NUMBER, "456"), 3),
        ("705", 1, Token(TokenType.NUMBER, "05"), 3),
        ("+", 0, Token(TokenType.NUMBER, ""), 0),
    ]
)
def test_get_number(text, pos, expected_token, expected_pos):
    """Extract number from text strating at pos."""

    #Arrange
    lexer = Lexer()
    #Act
    token, new_pos = lexer.get_number(text, pos) 
    #Assert
    assert token == expected_token
    assert new_pos == expected_pos


@pytest.mark.parametrize(
    "text, pos, expected_token, new_pos",
    [
        ("456", 0, Token(TokenType.NUMBER, "456"), 0),
        ("705", 1, Token(TokenType.NUMBER, "05"), 1),
        ("+", 0, Token(TokenType.ADD_OP, "+"), 1),
        ("+-", 1, Token(TokenType.ADD_OP, "-"), 2),
    ]
)
def test_get_add_op(text, pos, expected_token, expected_pos):
    """Extract addition operator from text strating at pos."""

    #Arrange
    lexer = Lexer()
    #Act
    token, new_pos = lexer.get_add_op(text, pos) 
    #Assert
    assert token == expected_token
    assert new_pos == expected_pos

@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("*", 0, Token(TokenType.MUL_OP, "*"), 1),
        ("/", 0, Token(TokenType.MUL_OP, "/"), 1),
    ]
)
def test_get_mul_op(lexer, text, pos, expected_token, expected_pos):
    """Test get_mul_op method."""
    token, new_pos = lexer.get_token(text, pos)
    assert token == expected_token
    assert new_pos == expected_pos

@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("^", 0, Token(TokenType.POWER_OP, "^"), 1),
    ]
)
def test_get_power_op(lexer, text, pos, expected_token, expected_pos):
    """Test get_power_op method."""
    token, new_pos = lexer.get_token(text, pos)
    assert token == expected_token
    assert new_pos == expected_pos

@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("!", 0, Token(TokenType.FAC_OP, "!"), 1),
    ]
)
def test_get_fac_op(lexer, text, pos, expected_token, expected_pos):
    """Test get_fac_op method."""
    token, new_pos = lexer.get_token(text, pos)
    assert token == expected_token
    assert new_pos == expected_pos