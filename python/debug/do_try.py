#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 异常处理
"""
try:
    10/0
except Exception as e:
    print('result:',e)
    #raise #ValueError('value not allowed zero!!!')
finally:
    print('finally')

# 调试

# 1. print()
# 2. assert 断言

# 3. logging
import logging
#logging.basicConfig(level=logging.INFO)
s = '01'
n = int(s)
logging.info('n=%d' % n)
print(10/n)

# 4. pdb

# 5. pdb.set_trace()
import pdb
s = '1'
n = int(s)
pdb.set_trace()
print(10/n)
"""

def fact(n):
    '''
    simple test
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(1)
    1
    >>> fact(2)
    2
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
