import unittest


class Solution:
    @staticmethod
    def hamming_weight(n: int) -> int:
        # Solution 1: With binary functions
        return bin(n).count("1")

        # Solution 2: Without binary functions
        # # Find n where n = maximum binary integer taken
        # i = 0
        # while 2**i <= n:
        #     i += 1

        # ones_count = 0
        # i -= 1

        # while i >=0:
        #     if n >= 2**i: # if 11 >= 8
        #         ones_count += 1
        #         n -= 2**i
        #     i -= 1
        # return ones_count


# Tests

class Test(unittest.TestCase):
    def test_sample_input(self):
        actual = Solution().hamming_weight(11)
        expected = 3
        self.assertEqual(actual,expected)

    # def test_one_way_to_make_zero_cents(self):
    #     actual = change_possibilities(0, (1, 2))
    #     expected = 1
    #     self.assertEqual(actual, expected)
    #
    # def test_no_ways_if_no_coins(self):
    #     actual = change_possibilities(1, ())
    #     expected = 0
    #     self.assertEqual(actual, expected)
    #
    # def test_big_coin_value(self):
    #     actual = change_possibilities(5, (25, 50))
    #     expected = 0
    #     self.assertEqual(actual, expected)
    #
    # def test_big_target_amount(self):
    #     actual = change_possibilities(50, (5, 10))
    #     expected = 6
    #     self.assertEqual(actual, expected)
    #
    # def test_change_for_one_dollar(self):
    #     actual = change_possibilities(100, (1, 5, 10, 25, 50))
    #     expected = 292
    #     self.assertEqual(actual, expected)

