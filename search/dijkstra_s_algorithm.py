"""
狄克斯特拉算法（针对图，图由节点和路径组成）
找出 A-B 的最快路径, 即总权重最小的路径
每条路径都有一个关联的数字，成为权重
带权重的图成为加权图，不带的就是非加权图
计算非加权图的最短路径使用广度优先算法
计算加权图的最短路径使用狄克斯特拉算法
图可能由环 A->B->C->A
本算法只适应于有向无环图
不能用于包含负权边的图（应该用贝尔曼·福德算法）
"""


def find_lowest_cost_node(costs, processed):
    """
    找出开销最低的节点
    """
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if node not in processed and cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def dijkstra_s_algorithm(graph, costs, parents, processed):
    """
    狄克斯特拉算法
    :param graph: 散列图
    :param costs: 开销散列图
    :param parents: 父节点散列图
    :param processed: 已处理节点列表
    :return:
    """
    node = find_lowest_cost_node(costs, processed)  # 在未处理的节点中找到开销最小的节点

    while node is not None:  # 当节点没有处理完时进行循环
        cost = costs[node]
        neighbors = graph[node]  # 获取该节点的邻居散列表
        for n in neighbors.keys():  # 遍历该节点的邻居节点
            new_cost = cost + neighbors[n]  # 获取到该邻居节点的开销
            if costs[n] > new_cost:  # 如果当前节点前往邻居节点的权重更小
                costs[n] = new_cost  # 更新邻居节点开销
                parents[n] = node  # 更新邻居节点的父节点

        processed.append(node)  # 标记该节点为处理过的节点

        node = find_lowest_cost_node(costs, processed)


def test():
    """
    start ----- 6 -----> A
    start ----- 2 -----> B
    A ----- 1 -----> fin
    B ----- 3 -----> A
    B ----- 5 -----> fin
    :return:
    """
    # noinspection PyDictCreation
    graph = {}
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    graph['a'] = {}
    graph['a']['fin'] = 1
    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    graph['fin'] = {}

    infinity = float('inf')  #
    # noinspection PyDictCreation
    cost = {}  # 开销表，开销指从起点到该节点需要到时长
    cost['a'] = 6
    cost['b'] = 2
    cost['fin'] = infinity  # 未知到达该节点的开销，假设无穷大

    # noinspection PyDictCreation
    parents = {}  # 存储父节点到散列图
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None

    processed = []  # 记录处理过的节点

    dijkstra_s_algorithm(graph, cost, parents, processed)

    get_list = ['fin']
    node = parents['fin']
    get_list.insert(0, node)
    while node != 'start':
        node = parents[node]
        get_list.insert(0, node)
    print(get_list)


if __name__ == '__main__':
    test()
