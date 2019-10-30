from chepy import Chepy


def test_reverse():
    assert Chepy("abcdefg").reverse().output == "gfedcba"


def test_count_occurances():
    assert (
        Chepy("AABCDADJAKDJHKSDAJSDdaskjdhaskdjhasdkja").count_occurances("ja").output
        == 2
    )