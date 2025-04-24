from typing import List


def main():
    args = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    solution = Solution()
    result = solution.findCircleNum(args)
    print(result)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        result = 0

        def _checkConnected(city_index: int):
            city = isConnected[city_index]

            for target_city_index in range(cities):
                target_city = isConnected[target_city_index]

                if city_index == target_city_index:
                    city[target_city_index] = 0
                else:
                    if city[target_city_index] == 0:
                        continue
                    city[target_city_index] = 0
                    target_city[city_index] = 0
                    _checkConnected(target_city_index)

        for city_index in range(cities):
            if 1 in isConnected[city_index]:
                result += 1
            _checkConnected(city_index)

        return result

        # set approach
        # cities = len(isConnected)
        # visited = [False] * cities
        # province_count = 0

        # def _dfs(city_i):
        #     visited[city_i] = True
        #     city_conn = isConnected[city_i]

        #     for i,v in enumerate(city_conn):
        #         if v == 1 and visited[i] == False:
        #             _dfs(i)

        # for city_i in range(cities):
        #     if visited[city_i] == False:
        #         province_count += 1
        #         _dfs(city_i)

        # return province_count


if __name__ == '__main__':
    main()
