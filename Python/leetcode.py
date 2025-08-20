import logging
from typing import List

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)
log = logging.getLogger(__name__)


class LeetCode:
    """
    Class containing LeetCode solution methods.
    """

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Method to solve the two sum problem.

        Args:
            nums (List[int]): List of numbers.
            target (int): Target value.

        Returns:
            List[int]: Indices of solution numbers.
        """

        num_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [i, num_map[diff]]
            num_map[num] = i
        return []

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Method to solve the three tum problem.

        Args:
            nums (List[int]): List of numbers.

        Returns:
            List[List[int]]: List of lists of numbers that add up to
            the target value (0).
        """
        result = []
        n = len(nums)

        # Sorting the list for the two pointer approach.
        nums.sort()

        # Iterating through the list.
        for i in range(n):

            # Removing duplicates for i.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Creating left and right pointers.
            left_pointer, right_pointer = i + 1, n - 1
            while left_pointer < right_pointer:
                total = (
                    nums[i] + nums[left_pointer] + nums[right_pointer]
                )  # Calculating sum.

                # If sum < 0, move left pointer forward.
                if total < 0:
                    left_pointer += 1
                # If sum > 0, move right pointer backward.
                elif total > 0:
                    right_pointer -= 1
                # If sum = 0, append the values to set and move both pointers.
                else:
                    result.append([nums[i], nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1
                    # Removing duplicates for the left and right pointers.
                    while (
                        left_pointer < right_pointer
                        and nums[left_pointer] == nums[left_pointer - 1]
                    ):
                        left_pointer += 1
                    while (
                        left_pointer < right_pointer
                        and nums[right_pointer] == nums[right_pointer + 1]
                    ):
                        right_pointer -= 1
        return result

    def zigzag_conversion(self, input: str, num_rows: int) -> str:
        """
        Method for the Zigzag Conversion Problem.

        Args:
            input (str): Input String.
            num_rows (int): Number of rows.

        Returns:
            str: Output string.
        """

        n = len(input)
        log.info(f"[*] Input string length: {n}")

        if num_rows == 1 or num_rows >= n:
            return input

        current_row = 0
        rows = [""] * num_rows
        direction = 1

        for char in input:
            rows[current_row] += char
            if current_row == num_rows - 1:
                direction = -1
            elif current_row == 0:
                direction = 1
            current_row += direction

            log.info(f"[*] Row: {current_row}, String: {rows[current_row]}")

        return "".join(rows)

    def roman_to_int(self, input: str) -> int:
        """
        Method to solve the Roman to Int problem.

        Args:
            input (str): Input strring. A VALID Roman Numeral in the range [0. 3999],
            all uppercase.

        Returns:
            int: The input Roman Numeral in integer format.
        """

        value_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        n = len(input)
        log.info(f"[+] Input: {input}")
        log.info(f"[+] Length: {n}")
        for i in range(n):
            next_val = value_dict[input[i + 1]] if i + 1 < n else 0
            current_val = value_dict[input[i]]
            if current_val < next_val:
                result -= current_val
            else:
                result += current_val
        return result
