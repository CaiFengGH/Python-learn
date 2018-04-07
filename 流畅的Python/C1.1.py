"""
Created on Sat Apr  7 15:42:26 2018
<流畅的Python1.1>
@author: Ethan
"""

import collections

#namedtuple:仅有少数属性而无方法
Card = collections.namedtuple('Card',['rank','suit'])

#有序的纸牌
#Python3中默认继承Object，无需(Object)
#_:私有属性和方法，为规范 __method__:内建方法
class FrenchDeck:
    #ranks:排序 suit:桃色
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits 
                           for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]

suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
#字典升序排序
def ascending(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

#实例化
deck=FrenchDeck()
#返回对象长度 __len__
len(deck)
#随机访问 __getitem__
from random import choice
choice(deck)
#查找A的四个桃色的牌
deck[12::13]
#逆序排名
for card in reversed(deck):
    print(card)
#升序排序扑克牌
sorted(deck,key=ascending)
