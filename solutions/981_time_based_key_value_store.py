from typing import Dict, List, Tuple


class TimeMap:
    def __init__(self):
        # key -> list of (timestamp, value) pairs
        self.store: Dict[str, List[Tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Store key-value pair with timestamp"""
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """Get value for key at or before given timestamp using binary search"""
        # Edge case: key doesn't exist
        if key not in self.store:
            return ""

        values = self.store[key]

        # Binary search for largest timestamp <= given timestamp
        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1  # Try to find larger valid timestamp
            else:
                right = mid - 1  # Search in left half

        return result


def main():
    # Test case 1: Basic functionality
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    assert timeMap.get("foo", 1) == "bar", "Should return 'bar' at timestamp 1"
    assert timeMap.get("foo", 3) == "bar", "Should return 'bar' at timestamp 3"

    timeMap.set("foo", "bar2", 4)
    assert timeMap.get(
        "foo", 4) == "bar2", "Should return 'bar2' at timestamp 4"
    assert timeMap.get(
        "foo", 5) == "bar2", "Should return 'bar2' at timestamp 5"

    # Test case 2: Non-existent key
    assert timeMap.get(
        "nonexistent", 1) == "", "Should return empty string for non-existent key"

    # Test case 3: Timestamp before any set
    timeMap2 = TimeMap()
    timeMap2.set("key", "value1", 10)
    assert timeMap2.get(
        "key", 5) == "", "Should return empty string for timestamp before any set"

    # Test case 4: Multiple values
    timeMap3 = TimeMap()
    timeMap3.set("love", "high", 10)
    timeMap3.set("love", "low", 20)
    assert timeMap3.get(
        "love", 5) == "", "Should return empty for timestamp before first set"
    assert timeMap3.get(
        "love", 10) == "high", "Should return 'high' at timestamp 10"
    assert timeMap3.get(
        "love", 15) == "high", "Should return 'high' at timestamp 15"
    assert timeMap3.get(
        "love", 20) == "low", "Should return 'low' at timestamp 20"
    assert timeMap3.get(
        "love", 25) == "low", "Should return 'low' at timestamp 25"

    print("All tests passed!")


if __name__ == "__main__":
    main()
