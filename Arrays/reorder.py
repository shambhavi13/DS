"""
you have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.
Then, either:
1. Each word after the identifier will consist only of lowercase letters, or;
2. Each word after the identifier will consist only of digits.
3. We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier,
with the identifier used in case of ties.  The digit-logs should be put in
their original order.

Return the final order of the log
"""


class Solution(object):
    def reorderLogFiles(self, logs):
        """
        input_logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
        output_logs = ['g1 act car', 'a8 act zoo', 'ab1 off key dog', 'a1 9 2 3 1', '
        """

        letters = []
        digits = []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(
            key=lambda x: x.split()[0])  # sort by identifier if its a tie
        letters.sort(key=lambda x: x.split()[1:])  # sort by suffix

        result = letters + digits

        return result
