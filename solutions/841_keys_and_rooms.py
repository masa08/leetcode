from typing import List


def main():
    args = [[1], [2], [3], []]
    solution = Solution()
    result = solution.canVisitAllRooms(args)
    print(result)


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        # check visited room
        def checkCanVisitRooms(room_index: int):
            if visited[room_index] == True:
                return

            visited[room_index] = True
            for key in rooms[room_index]:
                checkCanVisitRooms(key)

        checkCanVisitRooms(0)

        # return true if all values are true in visited else false
        return all(visited)


if __name__ == '__main__':
    main()
