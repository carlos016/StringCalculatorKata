class StringCalculator:
    def add(self, numbers: str = "") -> int:
        total = 0
        if numbers:
            separatorDefault = ","
            if numbers.startswith("//"):
                # Custom separator specified. Example:("//;\n1;2")
                separatorDefault = numbers[2 : numbers.index("\n")]
                numbers = numbers[numbers.index("\n") + 1 :]

            numbers = numbers.replace("\n", separatorDefault)
            try:
                for number in numbers.split(separatorDefault):
                    if int(number) < 0:
                        raise ValueError("Negative numbers are not allowed. ")
                    total += int(number)

            except ValueError:
                raise ValueError(
                    f"Invalid input: {number}, only positive numbers are allowed."
                )

        return total
