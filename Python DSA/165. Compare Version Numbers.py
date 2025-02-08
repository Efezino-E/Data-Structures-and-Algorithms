class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings into lists of integers
        ver1 = list(map(int, version1.split(".")))
        ver2 = list(map(int, version2.split(".")))

        # Compare each element in version 1 and return when less or greater
        for i in range(len(ver1)):
            v1 = ver1[i]
            if i > len(ver2) - 1:
                v2 = 0
            else:
                v2 = ver2[i]
            
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
    
        # Compare the remaining elements in version 2 and return when lesser
        if i < len(ver2) - 1:
            for j in range(i + 1, len(ver2)):
                v2 = ver2[j]
                if 0 < v2:
                    return -1

        # if all comparisons are not greater of lesser, return equality
        return 0