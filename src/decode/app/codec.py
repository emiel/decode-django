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
    assert fst >= 0
    assert snd >= 0
    buf = str(fst) + str(snd)
    return int(buf)


def combos(lst, acc=(), depth=0):
    """
    Find all combinations recursively. Returns a generator.

    :param lst:
        Input list of natural numbers
    :param acc:
        Path accumulator
    """
    # print(depth * "-", "combo", lst, acc)
    length = len(lst)

    # Base case
    if length == 0:
        yield acc

    # Left node (single-digits)
    if length >= 1:
        digit = lst[0]
        if digit != 0:
            new_acc = (*acc, lst[0])
            for c in combos(lst[1:], new_acc, depth + 1):
                yield c

    # Right node (double-digits)
    if length >= 2:
        # Only build nodes which fall within our encoding (1-26)
        fst, snd = lst[0], lst[1]
        if fst in (1, 2) and snd <= 6:
            num = join_int(fst, snd)
            new_acc = (*acc, num)
            for c in combos(lst[2:], new_acc, depth + 1):
                yield c


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
        A string containing only digits (0-9)
    """
    lst = [int(c) for c in buf]

    for t in combos(lst):
        res = [decode_int(n) for n in t]
        yield "".join(res)
