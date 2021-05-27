#DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(isConnected, i, visited):
            for j in range(cities): #
                if (isConnected[i][j] == 1 and j not in visited):   
                    #如果连通而又没有访问过
                    visited.add(j)  #则加入访问过的列表
                    dfs(isConnected, j, visited)    #并进行DFS
                    #这里比较tricky的点是当i=j时isConnected[i][j] 一定等于 1
                    #但是本题目并不影响，因为不管该点
            
        visited = set() #标记已经访问过的城市
        cities = len(isConnected)   #所有城市数目
        province = 0    #province数目，起始为0

        for i in range(cities): #遍历所有城市
            if i not in visited:    #如果城市没有访问过
                province += 1   #省份数目+1
                dfs(isConnected, i, visited)    #以该省份进行遍历，寻找所有链接的点
        return province

#BFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = set()
        province = 0
        
        for i in range(cities): #选择一个城市
            if i not in visited:    #如果城市没有被访问过
                Q = collections.deque([i])  #添加到队列
                while Q:    #当队列不为空时
                    j = Q.popleft() #选择队列头的城市出队列（准备访问）
                    visited.add(j)  #访问过后
                    for k in range(cities): #选择J城市为起点开始访问
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k) #把访问到与J城市相连的K城市加入队列准备访问
                    #直到队列清空后所有相连的城市访问完毕
                province += 1
        return province
