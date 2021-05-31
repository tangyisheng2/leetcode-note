class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        思路：
        对所有节点进行深度优先遍历
        flag == 0: 说明节点还没有遍历过
        flag == 1: 说明节点在由其节点开始的DFS中被遍历
        flag == 2: 说明节点遍历完成
        """
        edges = collections.defaultdict(lsit)
        visited = [0 for _ in range(numCourses)]
        valid = True


        def dfs(prerequsites, course_label):
            nonlocal valid
