class StringCalculator:
    def add(self, numbers: str = "") -> int:
        if numbers != "" and numbers != "0":
            return sum(int(num) for num in numbers.split(","))

        return 0
