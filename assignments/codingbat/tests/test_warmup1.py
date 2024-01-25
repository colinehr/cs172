import codingbat.warmup1 as warmup1
import pytest


def fail_msg(func_name: str, expected, actual, *args) -> str:
    if len(args) == 1:
        return (
            f"expected {func_name}({args[0]!r}) → {expected!r}, was {actual!r}"
        )
    args_tuple = tuple(args)
    return f"expected {func_name}{args_tuple!r} → {expected!r}, was {actual!r}"


@pytest.mark.parametrize(
    "weekday, vacation, expected",
    [
        (False, False, True),
        (True, False, False),
        (False, True, True),
        (True, True, True),
    ],
)
def test_sleep_in(weekday: bool, vacation: bool, expected: bool):
    result = warmup1.sleep_in(weekday, vacation)
    assert result is expected, fail_msg("sleep_in", expected, result, weekday, vacation)


@pytest.mark.parametrize(
    "a_smile, b_smile, expected",
    [
        (False, False, True),
        (True, False, False),
        (False, True, False),
        (True, True, True),
    ],
)
def test_monkey_trouble(a_smile: bool, b_smile: bool, expected: bool):
    result = warmup1.monkey_trouble(a_smile, b_smile)
    assert result is expected, fail_msg(
        "monkey_trouble", expected, result, a_smile, b_smile
    )


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (3, 2, 5),
        (2, 2, 8),
        (-1, 0, -1),
        (3, 3, 12),
        (0, 0, 0),
        (0, 1, 1),
        (3, 4, 7),
    ],
)
def test_sum_double(a: int, b: int, expected: int):
    result = warmup1.sum_double(a, b)
    assert result == expected, fail_msg("sum_double", expected, result, a, b)


@pytest.mark.parametrize(
    "n, expected",
    [
        (19, 2),
        (10, 11),
        (21, 0),
        (22, 2),
        (25, 8),
        (30, 18),
        (0, 21),
        (1, 20),
        (2, 19),
        (-1, 22),
        (-2, 23),
        (50, 58),
    ],
)
def test_diff21(n: int, expected: int):
    result = warmup1.diff21(n)
    assert result == expected, fail_msg("diff21", expected, result, n)


@pytest.mark.parametrize(
    "talking, hour, expected",
    [
        (True, 6, True),
        (True, 7, False),
        (False, 6, False),
        (True, 21, True),
        (False, 21, False),
        (False, 20, False),
        (True, 23, True),
        (False, 23, False),
        (True, 20, False),
        (False, 12, False),
    ],
)
def test_parrot_trouble(talking: bool, hour: int, expected: bool):
    result = warmup1.parrot_trouble(talking, hour)
    assert result is expected, fail_msg(
        "parrot_trouble", expected, result, talking, hour
    )


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (9, 10, True),
        (9, 9, False),
        (1, 9, True),
        (10, 1, True),
        (10, 10, True),
        (8, 2, True),
        (8, 3, False),
        (10, 42, True),
        (12, -2, True),
    ],
)
def test_makes10(a: int, b: int, expected: bool):
    result = warmup1.makes10(a, b)
    assert result is expected, fail_msg("makes10", expected, result, a, b)


@pytest.mark.parametrize(
    "n, expected",
    [
        (93, True),
        (90, True),
        (89, False),
        (100, True),
        (110, True),
        (111, False),
        (121, False),
        (-101, False),
        (189, False),
        (190, True),
        (191, True),
        (200, True),
        (209, True),
        (210, True),
        (211, False),
        (0, False),
        (5, False),
        (290, False),
    ],
)
def test_near_hundred(n: int, expected: bool):
    result = warmup1.near_hundred(n)
    assert result is expected, fail_msg("near_hundred", expected, result, n)


@pytest.mark.parametrize(
    "string, index, expected",
    [
        ("kitten", 1, "ktten"),
        ("kitten", 0, "itten"),
        ("kitten", 4, "kittn"),
        ("Hi", 0, "i"),
        ("Hi", 1, "H"),
        ("code", 0, "ode"),
        ("code", 1, "cde"),
        ("code", 2, "coe"),
        ("code", 3, "cod"),
        ("chocolate", 8, "chocolat"),
    ],
)
def test_missing_char(string: str, index: int, expected: str):
    result = warmup1.missing_char(string, index)
    assert result == expected, fail_msg("missing_char", expected, result, string, index)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("code", "eodc"),
        ("ab", "ba"),
        ("a", "a"),
        ("abc", "cba"),
        ("", ""),
        ("Chocolate", "ehocolatC"),
        ("Python", "nythoP"),
        ("hello", "oellh"),
    ],
)
def test_front_back(string: str, expected: str):
    result = warmup1.front_back(string)
    assert result == expected, fail_msg("front_back", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("Python", "PytPytPyt"),
        ("Chocolate", "ChoChoCho"),
        ("abc", "abcabcabc"),
        ("ab", "ababab"),
        ("a", "aaa"),
        ("", ""),
    ],
)
def test_front3(string: str, expected: str):
    result = warmup1.front3(string)
    assert result == expected, fail_msg("front3", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("cat", "tcatt"),
        ("Hello", "oHelloo"),
        ("a", "aaa"),
        ("abc", "cabcc"),
        ("boo", "obooo"),
        ("read", "dreadd"),
    ],
)
def test_back_around(string: str, expected: str):
    result = warmup1.back_around(string)
    assert result == expected, fail_msg("back_around", expected, result, string)


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, True),
        (10, True),
        (8, False),
        (15, True),
        (5, True),
        (9, True),
        (4, False),
        (7, False),
        (6, True),
        (17, False),
        (18, True),
        (19, False),
        (20, True),
        (21, True),
        (22, False),
        (45, True),
        (99, True),
        (100, True),
        (101, False),
        (121, False),
        (122, False),
        (123, True),
    ],
)
def test_or35(n: int, expected: str):
    result = warmup1.or35(n)
    assert result == expected, fail_msg("or35", expected, result, n)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("kitten", "kikittenki"),
        ("Ha", "HaHaHa"),
        ("abc", "ababcab"),
        ("ab", "ababab"),
        ("a", "aaa"),
        ("", ""),
    ],
)
def test_front22(string: str, expected: str):
    result = warmup1.front22(string)
    assert result == expected, fail_msg("front22", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("hi there", True),
        ("hi", True),
        ("hello hi", False),
        ("he", False),
        ("", False),
        ("ha hi", False),
        ("hi ha", True),
    ],
)
def test_start_hi(string: str, expected: str):
    result = warmup1.start_hi(string)
    assert result == expected, fail_msg("start_hi", expected, result, string)


@pytest.mark.parametrize(
    "temp1, temp2, expected",
    [
        (120, -1, True),
        (-1, 120, True),
        (2, 120, False),
        (-1, 100, False),
        (-2, -2, False),
        (120, 120, False),
    ],
)
def test_icy_hot(temp1: int, temp2: int, expected: bool):
    result = warmup1.icy_hot(temp1, temp2)
    assert result == expected, fail_msg("icy_hot", expected, result, temp1, temp2)


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (13, 20, 10, True),
        (20, 19, 10, True),
        (20, 10, 13, True),
        (1, 20, 12, False),
        (19, 20, 12, True),
        (12, 20, 19, True),
        (12, 9, 20, False),
        (12, 18, 20, True),
        (11, 22, 22, False),
    ],
)
def test_has_teen(a: int, b: int, c: int, expected: bool):
    result = warmup1.has_teen(a, b, c)
    assert result == expected, fail_msg("has_teen", expected, result, a, b, c)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (13, 99, True),
        (21, 19, True),
        (13, 13, False),
        (14, 20, True),
        (20, 15, True),
        (16, 17, False),
        (16, 9, True),
        (16, 18, False),
        (13, 19, False),
        (12, 20, False),
    ],
)
def test_lone_teen(a: int, b: int, expected: bool):
    result = warmup1.lone_teen(a, b)
    assert result == expected, fail_msg("lone_teen", expected, result, a, b)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("adelbc", "abc"),
        ("adelHello", "aHello"),
        ("adedbc", "adedbc"),
        ("abcdel", "abcdel"),
        ("add", "add"),
        ("del", "del"),
        ("adel", "a"),
        ("aadelbb", "aadelbb"),
    ],
)
def test_del_del(string: str, expected: str):
    result = warmup1.del_del(string)
    assert result == expected, fail_msg("del_del", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("mix snacks", True),
        ("pix snacks", True),
        ("piz snacks", False),
        ("nix", True),
        ("ni", False),
        ("mi", False),
        ("m", False),
        ("", False),
    ],
)
def test_mix_start(string: str, expected: bool):
    result = warmup1.mix_start(string)
    assert result is expected, fail_msg("mix_start", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("ozymandias", "oz"),
        ("bzoo", "z"),
        ("oxx", "o"),
        ("oz", "oz"),
        ("ounce", "o"),
        ("abc", ""),
        ("", ""),
        ("zoo", ""),
        ("zzzz", "z"),
    ],
)
def test_start_oz(string: str, expected: str):
    result = warmup1.start_oz(string)
    assert result == expected, fail_msg("start_oz", expected, result, string)


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 2, 3, 3),
        (1, 3, 2, 3),
        (3, 2, 1, 3),
        (9, 3, 3, 9),
        (3, 9, 3, 9),
        (3, 3, 9, 9),
        (-3, -1, -2, -1),
        (4, 4, 2, 4),
        (4, 2, 4, 4),
        (2, 4, 4, 4),
    ],
)
def test_int_max(a: int, b: int, c: int, expected: int):
    result = warmup1.int_max(a, b, c)
    assert result == expected, fail_msg("int_max", expected, result, a, b, c)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (8, 13, 8),
        (13, 8, 8),
        (13, 7, 0),
        (7, 13, 0),
        (9, 13, 9),
        (10, 12, 10),
        (11, 10, 10),
        (3, 3, 0),
        (-10, 31, -10),
        (-10, 30, 0),
    ],
)
def test_close10(a: int, b: int, expected: int):
    result = warmup1.close10(a, b)
    assert result == expected, fail_msg("close10", expected, result, a, b)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (30, 31, True),
        (30, 41, False),
        (40, 50, True),
        (40, 51, False),
        (39, 50, False),
        (50, 39, False),
        (40, 39, True),
        (41, 40, True),
        (39, 41, False),
        (50, 40, True),
        (40, 30, True),
    ],
)
def test_in3050(a: int, b: int, expected: bool):
    result = warmup1.in3050(a, b)
    assert result is expected, fail_msg("in3050", expected, result, a, b)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (11, 19, 19),
        (19, 11, 19),
        (11, 9, 11),
        (9, 11, 11),
        (9, 21, 0),
        (10, 21, 10),
        (21, 10, 10),
        (10, 20, 20),
        (20, 10, 20),
        (1, 1, 0),
    ],
)
def test_max1020(a: int, b: int, expected: int):
    result = warmup1.max1020(a, b)
    assert result == expected, fail_msg("max1020", expected, result, a, b)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("Hello", True),
        ("Heelies", True),
        ("beekeeping", False),
        ("between", True),
        ("elephant", True),
        ("hopscotch", False),
    ],
)
def test_string_e(string: str, expected: bool):
    result = warmup1.string_e(string)
    assert result is expected, fail_msg("string_e", expected, result, string)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (7, 17, True),
        (6, 17, False),
        (3, 113, True),
        (113, 114, False),
        (114, 4, True),
        (10, 0, True),
        (11, 0, False),
    ],
)
def test_last_digit(a: int, b: int, expected: bool):
    result = warmup1.last_digit(a, b)
    assert result is expected, fail_msg("last_digit", expected, result, a, b)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("Hello", "HeLLO"),
        ("hi there", "hi thERE"),
        ("hi", "HI"),
        ("woohoo", "wooHOO"),
        ("xyz12", "xyZ12"),
        ("x", "X"),
        ("", ""),
    ],
)
def test_end_up(string: str, expected: str):
    result = warmup1.end_up(string)
    assert result == expected, fail_msg("end_up", expected, result, string)


@pytest.mark.parametrize(
    "string, n, expected",
    [
        ("Miracle", 2, "Mrce"),
        ("abcdefg", 2, "aceg"),
        ("abcdefg", 3, "adg"),
        ("Chocolate", 3, "Cca"),
        ("Chocolates", 3, "Ccas"),
        ("Chocolates", 4, "Coe"),
        ("Chocolates", 100, "C"),
    ],
)
def test_every_nth(string: str, n: int, expected: str):
    result = warmup1.every_nth(string, n)
    assert result == expected, fail_msg("every_nth", expected, result, string, n)
