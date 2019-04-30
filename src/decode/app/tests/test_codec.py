from django.test import TestCase

from app.codec import join_int, combos, decode


class TestDecode(TestCase):
    def test_join_int(self):
        self.assertEqual(join_int(1, 2), 12)
        self.assertEqual(join_int(12, 34), 1234)
        self.assertEqual(join_int(123, 456), 123456)
        self.assertEqual(join_int(10, 10), 1010)
        self.assertEqual(join_int(0, 10), 10)
        self.assertEqual(join_int(1, 0), 10)

    def test_combos_01(self):
        self.assertEqual(list(combos([0, 1])), [])

    def test_combos_12(self):
        self.assertEqual(list(combos([1, 2])), [(1, 2), (12,)])

    def test_combos_206(self):
        self.assertEqual(list(combos([2, 0, 6])), [(20, 6)])

    def test_combos_226(self):
        self.assertEqual(list(combos([2, 2, 6])), [(2, 2, 6), (2, 26), (22, 6)])

    def test_combos_1234(self):
        self.assertEqual(
            list(combos([1, 2, 3, 4])), [(1, 2, 3, 4), (1, 23, 4), (12, 3, 4)]
        )

    def test_combos_1010(self):
        self.assertEqual(list(combos([1, 0, 1, 0])), [(10, 10)])

    def test_decode_12(self):
        self.assertEqual(list(decode("12")), ["AB", "L"])

    def test_decode_206(self):
        self.assertEqual(list(decode("206")), ["TF"])

    def test_decode_226(self):
        self.assertEqual(list(decode("226")), ["BBF", "BZ", "VF"])

    def test_decode_1234(self):
        self.assertEqual(list(decode("1234")), ["ABCD", "AWD", "LCD"])

    def test_decode_1010(self):
        self.assertEqual(list(decode("1010")), ["JJ"])
