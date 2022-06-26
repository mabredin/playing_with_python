class Snow:
    def __init__(self, count=10):
        self.count_snowflake = round(count)

    def __add__(self, n):
        return self.count_snowflake + n

    def __sub__(self, n):
        return self.count_snowflake - n

    def __mul__(self, n):
        return self.count_snowflake * n

    def __truediv__(self, n):
        return round(self.count_snowflake / n)

    def __call__(self, n):
        self.count_snowflake = n

    @staticmethod
    def add_snowflake_in_list(resultList, count, snowflake, number):
        result = ''
        for i in range(number):
            result = result + snowflake
            count += 1
        resultList.append(result)
        return resultList, count, snowflake

    def makeSnow(self, n):
        if 0 < n <= self.count_snowflake:
            snowflake = '*'
            resultList = []
            count = 0
            while count != self.count_snowflake:
                c = self.count_snowflake - count
                if c >= n:
                    resultList, count, snowflake = self.add_snowflake_in_list(resultList, count, snowflake, n)
                else:
                    resultList, count, snowflake = self.add_snowflake_in_list(resultList, count, snowflake, c)
            return repr('\n'.join(resultList))
        else:
            return "Error! Invalid argument value passed!"


x = Snow(50)
print(x.makeSnow(5))
print(x.makeSnow(4))
print(x.makeSnow(7))
print(x.makeSnow(0))
print(x.makeSnow(57))

x(100)
print(x.count_snowflake)