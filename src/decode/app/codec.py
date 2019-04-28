import string


def join_int(fst, snd):
    assert fst > 0
    assert snd > 0
    buf = str(fst) + str(snd)
    return int(buf)


def combos(lst, acc=(), depth=0):
    """
    Find all combinations.

    Recursive

    :lst:
        Input list of natural numbers
    :acc:
        Accumulator
    """
    # print(depth * "-", "combo", lst, acc)
    length = len(lst)

    if length == 0:
        yield acc

    if length >= 1:
        new_acc = (*acc, lst[0])
        for c in combos(lst[1:], new_acc, depth + 1):
            yield c

    if length >= 2:
        new_acc = (*acc, join_int(lst[0], lst[1]))
        for c in combos(lst[2:], new_acc, depth + 1):
            yield c


def decode_int(n):
    """
    Decode integer as follows:

    1 -> A
    2 -> B
    ..
    26 -> Z

    > 26 -> _
    """
    return string.ascii_uppercase[n - 1] if n <= 26 else "_"


def decode(buf):
    """
    :buf:
        A string containing only digits


    decode("12") -> ["AB", "L"]
    decode("226") -> ["BZ", "VF", "BBF"]

    XXX Should combos > 26 be eliminated? Sure
    decode("34") -> ["_"]
    """
    lst = [int(c) for c in buf]

    for t in combos(lst):
        res = [decode_int(n) for n in t]
        yield "".join(res)
