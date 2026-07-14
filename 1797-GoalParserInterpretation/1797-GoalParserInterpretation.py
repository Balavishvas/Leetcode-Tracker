# Last updated: 7/14/2026, 2:15:50 PM
class Solution:
    def interpret(self, command: str) -> str:
        command=command.replace("()","o")
        command=command.replace("(al)","al")
        return command