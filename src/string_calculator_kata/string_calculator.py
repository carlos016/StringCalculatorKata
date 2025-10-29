class StringCalculator:
    def add(self, numbers: str = "") -> int:
        total = 0
        if numbers:
            try:
                for number in numbers.split(","):
                    total += int(number)
            except ValueError:
                print(
                    f"Invalid input encountered: {number},"
                    f" only numbers are allowed."
                )
                raise ValueError(
                    f"Invalid input: {number}," f" only numbers are allowed."
                )

        return total
