# sample.py
# Using unit tests included in docstrings 
# See test_sample.py for unit tests that utilize pytest

def pow_of_two(x):
        """Return x to the power of 2.

        >>> pow_of_two(2)
        4
        >>> pow_of_two(-3)
        4
        """
        return x**2

def float_div_by_two(x):
        """Return x divided by 2 in floating point precision.

        >>> float_div_by_two(49)
        24.5
        >>> float_div_by_two(48)
        24.0
        """
        return x / 2.0

if __name__ == '__main__':
        import doctest
        doctest.testmod()