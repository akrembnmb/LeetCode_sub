class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hist = {}
        for e in strs :
            srtd = "".join(sorted(e))
            if srtd in hist:
                hist[srtd].append(e)
            else:hist[srtd]=[e]
        return hist.values()



"""Time Complexity: O(N * K * log K)
N is the number of strings in the input list strs.
K is the maximum length of a string in the strs list."""