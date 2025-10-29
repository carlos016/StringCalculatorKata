class StringCalculator:
    def add(self, numbers: str = "") -> int:
        total = 0
        if numbers:
            if numbers.count(",") >= 2:
                raise ValueError(
                    "Invalid input: More than two numbers provided."
                    " Only up to two numbers are allowed."
                )
            for number in numbers.split(","):
                try:
                    total += int(number)
                except ValueError:
                    print(
                        f"Invalid input encountered: {number},"
                        f" only numbers are allowed."
                    )
                    raise ValueError(
                        f"Invalid input: {number}, only numbers are allowed."
                    )

        return total
