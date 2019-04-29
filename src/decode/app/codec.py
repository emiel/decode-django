import string


def join_int(fst, snd):
    """
    Join two independent ints together
    - 1, 2 -> 12
    - 12, 34 -> 1234

    :param fst:
        First number
    :param snd:
        Second number
    """
    assert fst > 0
    assert snd > 0
    buf = str(fst) + str(snd)
    return int(buf)


class Node:
    def __init__(self, tail=[], acc=[], left=None, right=None):
        self.tail = tail
        self.acc = acc
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def __repr__(self, level=0, indent="--"):
        s = level * indent + repr(self.tail) + "|" + repr(self.acc)
        if self.left:
            s = s + "\n" + self.left.__repr__(level + 1, indent)
        if self.right:
            s = s + "\n" + self.right.__repr__(level + 1, indent)
        return s


def tree(lst, acc=[]):
    left = None
    right = None

    n = len(lst)

    if n >= 1:
        num = lst[0]
        left = tree(lst[1:], acc + [num])

    if n >= 2:
        num = join_int(lst[0], lst[1])
        if num <= 26:
            right = tree(lst[2:], acc + [num])

    return Node(lst, acc, left=left, right=right)


def leaves(t):
    if t.is_leaf():
        yield t

    if t.left is not None:
        for leaf in leaves(t.left):
            yield leaf

    if t.right is not None:
        for leaf in leaves(t.right):
            yield leaf


def decode_int(n):
    """
    Decode integer as follows:

    1 -> A
    2 -> B
    ..
    26 -> Z

    Anything above 26 returns an underscore.

    :param n:
        The integer to decode
    :returns:
        The decoded integer
    """
    return string.ascii_uppercase[n - 1] if n <= 26 else "_"


def decode(buf):
    """
    decode("12") -> ["AB", "L"]
    decode("226") -> ["BZ", "VF", "BBF"]

    :param buf:
        A string containing only digits (1-9)
    """
    lst = [int(c) for c in buf]

    for combo in leaves(tree(lst)):
        res = [decode_int(n) for n in combo.acc]
        yield "".join(res)
