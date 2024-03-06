"""A simple lexical analyzer."""

# Standard library
from collections import namedtuple
from enum import Enum

# 3rd Party library

# Project library
from calculator.token import Token, TokenType
#---------------------------------------------------------------------------------
class Lexer:
   """A simple lexical analyzer."""

   def get_number(self, text, pos):
      """Extract number from text starting at pos.

      Args:
            text (str): Text to be scanned.
            pos (int): The starting position to scan.

     Retuns:
         token: The extracted token
         pos:   The position after the scanning.

        Gramer:
            Number = Digit { Digit }
            Digit = "0" | ... | "9" 
      """
      lexeme = ""
      length = len(text)
      if pos >= length:
         return Token(TokenType.EMPTY, lexeme), pos
      

      if not text[pos].isdigit():
         return Token(TokenType.ERROR, lexeme), pos
      while pos < length and text[pos].isdigit():
         lexame = lexame + text[pos]
         pos = pos + 1

         return Token(TokenType.NUMBER, lexeme), pos
      
   def get_token(self, text, pos):
        """Extract token from text starting at pos."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos].isdigit():
            return self.get_number(text, pos)
        elif text[pos] in ['+', '-', '*', '/', '^', '(', ')']:
            lexeme = text[pos]
            return Token(TokenType.from_symbol(lexeme), lexeme), pos + 1
        else:
            return Token(TokenType.ERROR, lexeme), pos + 1
      

   def get_add_op(self, text, pos):
      """Extract an addition operator."""
      lexeme = ""
      length = len(text)
      if pos >= length:
         return Token(TokenType.EMPTY, lexeme), pos
      
      if text[pos] == "+":
         lexeme = text[pos]
         pos = pos +1
         return Token(TokenType.ADD_OP, lexeme), pos
      elif text[pos] == "-":
         lexeme = text[pos]
         pos = pos +1
         return Token(TokenType.ADD_OP, lexeme), pos
      else :
         return Token(TokenType.ERROR, lexeme), pos