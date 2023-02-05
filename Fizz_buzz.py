class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        List = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                List.append(str("FizzBuzz"))
            elif i % 3 == 0:
                List.append(str("Fizz"))
            elif i % 5 == 0:
                List.append(str("Buzz"))
            else:
                List.append(str(i))
        return List
