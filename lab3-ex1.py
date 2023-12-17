# Variable total_courses represents the number of courses you have to take in one semester, labelled from 0 to total_courses - 1. Now you are given an array of prerequisites where prerequisites[i] = [ai, bi]  indicates that you must take course bi  first if you want to take course ai.
# For example, the pair [0,1], indicates that to take course 0 you have to first take course 1. 
# Return true if you can finish all courses. Otherwise, return false.

def findOrder(numCourses, prerequisites):
    adjList = {}
    indegree = [0] * numCourses

    topologicalOrder = [0] * numCourses
    for i in range(len(prerequisites)):
        dest = prerequisites[i][0]
        src = prerequisites[i][1]

        if src in adjList:
            adjList[src].append(dest)
        else:
            adjList[src] = [dest]

        indegree[dest] += 1
    q = []

    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    i = 0
    while q:
        node = q.pop(0)
        topologicalOrder[i] = node
        i += 1

        if node in adjList:
            for neighbor in adjList[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

    if i == numCourses:
        return True

    return False

numCourses = int(input("numCourses = "))
prerequisites = eval(input("prerequisites = "))
print(findOrder(numCourses, prerequisites))

