# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import heapq
class PriorityQueue(object):
	"""简单的优先级队列"""
	def __init__(self):
		self._queue=[]
		self._index=0

	def push(self,item,priority):
		heapq.heappush(self._queue,(-priority,self._index,item))
		self._index+=1

	def pop(self):
		# return heapq.heappop(self._queue)[-1]	
		return heapq.heappop(self._queue)[-1]	

class Item:
	def __init__(self,name):
		self.name=name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)   #format

q=PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)
