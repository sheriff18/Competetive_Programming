https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/submissions/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        i = 0
        j = n-1
        reference_sum = skill[0] + skill[n-1]
        arr = []

        while i < j:
            if skill[i] + skill[j] == reference_sum:
                arr.append(skill[i]*skill[j])
                i += 1
                j -= 1
            else:
                return -1
        return sum(arr)
