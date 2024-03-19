import pytest
from task_1 import separate_paren_groups

def test_separate_paren_groups():
	assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
	assert separate_paren_groups('(( )) (( )( ))') == ['(())', '(()())']
	assert separate_paren_groups('( )') == ['()']
	assert separate_paren_groups('') == []
	assert separate_paren_groups(' ') == []
	assert separate_paren_groups('(( )) (( )( )) ( )') == ['(())', '(()())', '()']
	assert separate_paren_groups('(( )) (( )( )) ( ) ( )') == ['(())', '(()())', '()', '()']
	assert separate_paren_groups('(( )) (( )( )) ( ) ( ) ( )') == ['(())', '(()())', '()', '()', '()']
	assert separate_paren_groups('(( )) (( )( )) ( ) ( ) ( ) ( )') == ['(())', '(()())', '()', '()', '()', '()']
	assert separate_paren_groups('(( )) (( )( )) ( ) ( ) ( ) ( ) ( )') == ['(())', '(()())', '()', '()', '()', '()', '()']
	assert separate_paren_groups('(( )) (( )( )) ( ) ( ) ( ) ( ) ( ) ( )') == ['(())', '(()())', '()', '()', '()', '()', '()', '()']
	assert separate_paren_groups('(( )) (( )( )) ( ) ( ) ( ) ( ) ( ) ( ) ( )') == ['(())', '(()())', '()', '()', '()', '()', '()', '()', '()']
