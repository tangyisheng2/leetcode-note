from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)  # 建立二维字典，存储格式是{src1:{dst1:cost1,dst2:cost2...}}
        for u, v, w in flights:
            graph[u][v] = w  # 建立邻接表存储边的信息

        # 建立队列，方便BFS，记录每层搜索的出发节点们，初始为src，第二个元素是记录走到该节点为止的cost
        queue = [(src, 0)]
        # 记录遍历到某节点所需的cost，若有新线路到该节点的花费更少，才把线路放入队列，再从该节点进行下次遍历
        costlist = [float('inf') for _ in range(100)]
        # count记录走了几个节点，res记录走到终点时最小的花费值
        count, res = 0, float('inf')
        # 开始BFS
        while queue and count <= k:
            tempq = []  # 记录下一层的BFS的queue
            for x in queue:  # 遍历这一层的起点
                tempcost = x[1]  # 记录走到该起点时的已有花费
                for y in graph[x[0]]:  # 遍历从该起点可到达的终点
                    costnow = tempcost + graph[x[0]][y]  # 现在的花费
                    if costnow < costlist[y]:  # 若该线路的花费小于之前的线路的花费，才继续往下走
                        costlist[y] = costnow  # 更新该终点的最小花费
                        if y == dst:  # 若到达终点，则更新到达终点的最小花费
                            res = min(costnow, res)
                        else:
                            tempq.append((y, costnow))  # 将该点加入下一次遍历的节点中
            queue = tempq
            count += 1

        if res == float('inf'):  # 说明到不了dst
            return -1
        return res


test = Solution()
ret = test.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1)
print(ret)
