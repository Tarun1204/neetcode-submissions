class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # Courses currently in the DFS path
        visiting = set()

        def dfs(course):
            # A cycle was found
            if course in visiting:
                return False

            # No prerequisites remain for this course
            if graph[course] == []:
                return True

            visiting.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # Mark as completely processed
            visiting.remove(course)
            graph[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        