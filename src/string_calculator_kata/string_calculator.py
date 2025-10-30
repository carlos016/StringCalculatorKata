class StringCalculator:
    def __init__(self) -> None:
        self.call_count = 0

    # Method to add numbers in a string
    def add(self, numbers: str = "") -> int:
        total = 0
        if numbers:
            mainSeparator = ","
            secondarySeparator = "\n"

            if numbers.startswith("//["):
                # Custom separator specified. Example:("//[;]\n1;2")
                mainSeparator = numbers[3 : numbers.index("]\n")]
                if "][" in numbers:
                    mainSeparator = numbers[3 : numbers.index("][")]
                    secondarySeparator = numbers[
                        numbers.index("][") + 2 : numbers.index("]\n")
                    ]

                numbers = numbers[numbers.index("]\n") + 2 :]

            numbers = numbers.replace(secondarySeparator, mainSeparator)
            try:
                negative_numbers = []
                for number in numbers.split(mainSeparator):
                    if int(number) < 0:
                        negative_numbers.append(number)
                    if int(number) <= 1000:
                        total += int(number)

                if negative_numbers:
                    raise ValueError(
                        f"Negatives not allowed: {', '.join(negative_numbers)}. "
                    )

            except ValueError:
                raise ValueError(
                    f"Invalid input: {number}, only positive numbers are allowed."
                )
        self.call_count += 1
        return total

    # Method to get the number of times 'add' has been called
    def get_call_count(self) -> int:
        return self.call_count
