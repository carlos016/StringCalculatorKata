class StringCalculator:
    def __init__(self) -> None:
        self.call_count = 0

    # Method to extract separators and numbers from the input string
    def extract_separators_and_numbers(self, numbers: str) -> tuple:
        main_separator = ","
        secondary_separator = "\n"

        if numbers.startswith("//"):
            # Custom separator specified. Example:("//;\n1;2")
            main_separator = numbers[2 : numbers.index("\n")]
            if numbers.startswith("//["):
                # Custom separator specified. Example:("//[;]\n1;2")
                main_separator = numbers[3 : numbers.index("]")]
                if "][" in numbers:
                    secondary_separator = numbers[
                        numbers.index("][") + 2 : numbers.index("]\n")
                    ]

            numbers = numbers[numbers.index("\n") + 1 :]

        return main_separator, secondary_separator, numbers

    # Method to add numbers in a string
    def add(self, numbers: str = "") -> int:
        total = 0
        if numbers:
            main_separator, secondary_separator, numbers = (
                self.extract_separators_and_numbers(numbers)
            )
            numbers = numbers.replace(secondary_separator, main_separator)
            try:
                negative_numbers = []
                for number in numbers.split(main_separator):
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
