# -*- coding: utf-8 -*-
from __future__ import unicode_literals

prices={
	'ACME':45.23,
	'AAPL':612,
	'IBM':205,
	'HPQ':37.20,
	'FB':10.75
}
print prices
print '`````````'
print min(prices,key=lambda k:prices[k])
print '`````````'
print min(prices)
print '`````````'
print min(prices.values())
