class StringCalculator:
    def add(self, numbers: str = "") -> int:
        total = 0
        if numbers:
            for number in numbers.split(","):
                total += int(number)

        return total
