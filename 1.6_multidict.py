# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import defaultdict

#type : list multidict
d=defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(2)
d['b'].append(4)
print d


#type : set multidict
b=defaultdict(set)
b['a'].add(1)
b['a'].add(2)
b['a'].add(2)   #set not same element
b['b'].add(1)
print b

#setdefault()  可以避免使用multidict 但是又可以动态添加element
m={}
m.setdefault('a',[]).append(1)
m.setdefault('a',[]).append(2)
m.setdefault('b',[]).append(4)
print m