from typing import List


class Solution:
    """
    https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            """
            DFS检测环
            :param i: 当前节点编号
            :param adjacency: 邻接表
            :param flags: 储存节点状态的flag数组：
                            1. 未被DFS访问: i == 0
                            2. 已被其他节点启动的DFS访问: i == -1
                            3. 已被当前节点启动的DFS访问: i == 1
            :return: True: 当前路径是可行的；False: 当前路径是不可信的
            """
            if flags[i] == -1:  # 如果当前节点已经被别的节点访问过
                return True
            if flags[i] == 1:  # 如果当前节点已经被自己访问过（出现环）
                return False
            flags[i] = 1  # 更新flags为当前节点启动的DFS
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):  # 如果又一个节点发现了环
                    return False
            flags[i] = -1  # 更新节点为其他节点启动的DFS
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):  # 如果所有节点的DFS都有合法路径
                return False
        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        BFS： 依次删除入度为0的节点，如果存在环，则一定有节点的入度始终不为0
        若有节点的入度为0，则代表该节点已经没有前置课程，可以出队，最后计算无法出队的课程数目
        :param numCourses:
        :param prerequisites:
        :return:
        """
        import collections
        indegrees = [0 for _ in range(numCourses)]  # 入度表
        adjacency = [[] for _ in range(numCourses)]  # 领接表
        queue = collections.deque()
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:  # 构建入度表和领接表
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)  # 将所有入度为0的课程入队（先修）
        # BFS TopSort.
        while queue:
            pre = queue.popleft()
            numCourses -= 1  # 当前节点出队，剩下的课程数量减一
            for cur in adjacency[pre]:
                indegrees[cur] -= 1  # 对所有相邻课程的入度-1
                if not indegrees[cur]:  # 如果当前课的入度为0，则继续入队
                    queue.append(cur)
        return not numCourses


test = Solution()
test.canFinish(
    5,
    [[1, 4], [2, 4], [3, 1], [3, 2]])
