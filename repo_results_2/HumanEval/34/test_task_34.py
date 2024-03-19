import doctest
from task_34 import unique

def test_unique():
	doctest.run_docstring_examples(unique, globals(), verbose=True)
