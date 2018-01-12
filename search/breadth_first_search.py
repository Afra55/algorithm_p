"""
广度优先算法,用于图，先遍历最近关系节点，再遍历深层节点
先判断是否有 A-B 的路径，再找出最短路径
O(V+E) V：定点数，E：边数

"""
from collections import deque


def is_the_point_wanted(point):
    if point[-1] == 'c':
        return True
    else:
        return False


def breadth_first_search(relation_map, key):
    search_queue = deque()  # 双端队列, FIFO 先进先出
    search_queue += relation_map[key]
    searched = []  # 用于记录检查过端元素

    while search_queue:
        point = search_queue.popleft()
        if point not in searched:  # 当这个元素没有被检查过时才去检查
            if is_the_point_wanted(point):
                print('Yes, i found this one:', point)
                return True
            else:
                search_queue += relation_map[point]  # 当这个元素不是所需元素时，把这个元素的关系加入队列
                searched += point  # 记录这个元素为检查过的元素


# noinspection PyDictCreation
graph = {}  # 朋友关系图，无向图
graph['me'] = ['bob', 'aob', 'cob']
graph['bob'] = ['me', 'cc', 'boy', 'ce']
graph['aob'] = ['me', 'baby', 'boy', 'buy']
graph['cob'] = ['me', 'nice', 'note', 'nb']
graph['cc'] = ['bob']
graph['ce'] = ['bob']
graph['baby'] = ['aob']
graph['boy'] = ['bob', 'aob']
graph['buy'] = ['aob']
graph['nice'] = ['cob']
graph['note'] = ['cob']
graph['nb'] = ['cob']

breadth_first_search(graph, 'me')
