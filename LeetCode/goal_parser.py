https://leetcode.com/problems/goal-parser-interpretation/submissions/978773825/

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')
        
