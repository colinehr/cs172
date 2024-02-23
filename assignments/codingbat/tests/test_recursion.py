import codingbat.recursion as recursion
import pytest


def fail_msg(func_name: str, expected, actual, *args) -> str:
    if len(args) == 1:
        return f"expected {func_name}({args[0]!r}) → {expected!r}, was {actual!r}"
    args_tuple = tuple(args)
    return f"expected {func_name}{args_tuple!r} → {expected!r}, was {actual!r}"


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (8, 40320),
        (12, 479001600),
    ],
)
def test_factorial(n: int, expected: int):
    result = recursion.factorial(n)
    assert result == expected, fail_msg("factorial", expected, result, n)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 2),
        (2, 4),
        (3, 6),
        (4, 8),
        (5, 10),
        (12, 24),
        (50, 100),
        (234, 468),
    ],
)
def test_bunny_ears(n: int, expected: int):
    result = recursion.bunny_ears(n)
    assert result == expected, fail_msg("bunny_ears", expected, result, n)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (20, 6765),
    ],
)
def test_fibonacci(n: int, expected: int):
    result = recursion.fibonacci(n)
    assert result == expected, fail_msg("fibonacci", expected, result, n)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (5, 15),
        (6, 21),
        (7, 28),
        (20, 210),
    ],
)
def test_triangle(n: int, expected: int):
    result = recursion.triangle(n)
    assert result == expected, fail_msg("triangle", expected, result, n)


@pytest.mark.parametrize(
    "n, expected",
    [
        (126, 9),
        (49, 13),
        (12, 3),
        (10, 1),
        (1, 1),
        (0, 0),
        (730, 10),
        (1111, 4),
        (11111, 5),
        (10110, 3),
        (235, 10),
    ],
)
def test_sum_digits(n: int, expected: int):
    result = recursion.sum_digits(n)
    assert result == expected, fail_msg("sum_digits", expected, result, n)


@pytest.mark.parametrize(
    "n, expected",
    [
        (717, 2),
        (7, 1),
        (123, 0),
        (77, 2),
        (7123, 1),
        (771237, 3),
        (771737, 4),
        (47571, 2),
        (777777, 6),
        (773777, 5),
    ],
)
def test_count7(n: int, expected: int):
    result = recursion.count7(n)
    assert result == expected, fail_msg("count7", expected, result, n)


@pytest.mark.parametrize(
    "base, n, expected",
    [
        (3, 1, 3),
        (3, 2, 9),
        (3, 3, 27),
        (3, 4, 81),
        (2, 1, 2),
        (2, 2, 4),
        (2, 3, 8),
        (2, 4, 16),
        (2, 5, 32),
        (10, 1, 10),
        (10, 2, 100),
        (10, 3, 1000),
    ],
)
def test_power_n(base: int, n: int, expected: int):
    result = recursion.power_n(base, n)
    assert result == expected, fail_msg("power_n", expected, result, base, n)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("xxhixx", 4),
        ("xhixhix", 3),
        ("hixhi", 1),
        ("hi", 0),
        ("h", 0),
        ("x", 1),
        ("", 0),
    ],
)
def test_count_x(string: str, expected: int):
    result = recursion.count_x(string)
    assert result == expected, fail_msg("count_x", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("xxhixx", 1),
        ("xhixhix", 2),
        ("hixhi", 2),
        ("hi", 1),
        ("h", 0),
        ("x", 0),
        ("", 0),
        ("ihihihihih", 4),
        ("ihihihihihi", 5),
        ("xhixhxihihhhih", 3),
    ],
)
def test_count_hi(string: str, expected: int):
    result = recursion.count_hi(string)
    assert result == expected, fail_msg("count_hi", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("codex", "codey"),
        ("xxhixx", "yyhiyy"),
        ("xhixhix", "yhiyhiy"),
        ("xhiy", "yhiy"),
        ("xxx", "yyy"),
        ("xyx", "yyy"),
        ("h", "h"),
        ("x", "y"),
        ("y", "y"),
        ("", ""),
    ],
)
def test_change_xy(string: str, expected: str):
    result = recursion.change_xy(string)
    assert result == expected, fail_msg("change_xy", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("codex", "code"),
        ("xxhixx", "hi"),
        ("xhixhix", "hihi"),
        ("xhiy", "hiy"),
        ("xxx", ""),
        ("xyx", "y"),
        ("h", "h"),
        ("x", ""),
        ("y", "y"),
        ("", ""),
    ],
)
def test_no_x(string: str, expected: str):
    result = recursion.no_x(string)
    assert result == expected, fail_msg("no_x", expected, result, string)


@pytest.mark.parametrize(
    "l, expected",
    [
        ([1, 2, 11], 1),
        ([11, 11], 2),
        ([1, 2, 3, 4], 0),
        ([1, 11, 3, 11, 11], 3),
        ([11], 1),
        ([1], 0),
        ([], 0),
    ],
)
def test_count_11(l: list[int], expected: str):
    try:
        result = recursion.count_11(l)
        assert result == expected, fail_msg("count_11", expected, result, l)
    except TypeError:
        result = recursion.count_11(l, 0)
        assert result == expected, fail_msg("count_11", expected, result, l, 0)
    


@pytest.mark.parametrize(
    "string, expected",
    [
        ("hello", "h*e*l*l*o"),
        ("mash", "m*a*s*h"),
        ("abc", "a*b*c"),
        ("ab", "a*b"),
        ("a", "a"),
        ("", ""),
    ],
)
def test_all_star(string: str, expected: str):
    result = recursion.all_star(string)
    assert result == expected, fail_msg("all_star", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("hello", "hel*lo"),
        ("xxyy", "x*xy*y"),
        ("aaaa", "a*a*a*a"),
        ("aaab", "a*a*ab"),
        ("aa", "a*a"),
        ("a", "a"),
        ("", ""),
    ],
)
def test_pair_star(string: str, expected: str):
    result = recursion.pair_star(string)
    assert result == expected, fail_msg("pair_star", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("yyzzza", "yza"),
        ("abbbcdd", "abcd"),
        ("Hello", "Helo"),
        ("xyz", "xyz"),
        ("112ab445", "12ab45"),
        ("zzzzzz", "z"),
        ("a", "a"),
    ],
)
def test_string_clean(string: str, expected: str):
    result = recursion.string_clean(string)
    assert result == expected, fail_msg("string_clean", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("xyz(abc)123", "(abc)"),
        ("x(hello)", "(hello)"),
        ("(xy)1", "(xy)"),
        ("not really (possible)", "(possible)"),
        ("(abc)", "(abc)"),
        ("(abc)xy", "(abc)"),
        ("(abc)x", "(abc)"),
        ("()", "()"),
    ],
)
def test_paren_bit(string: str, expected: str):
    result = recursion.paren_bit(string)
    assert result == expected, fail_msg("paren_bit", expected, result, string)


@pytest.mark.parametrize(
    "string, expected",
    [
        ("(())", True),
        ("((()))", True),
        ("((x))", False),
        ("((())", False),
        ("((()()", False),
        ("()", True),
        ("", True),
        ("(yy)", False),
    ],
)
def test_nest_paren(string: str, expected: bool):
    result = recursion.nest_parens(string)
    assert result is expected, fail_msg("nest_parens", expected, result, string)


@pytest.mark.parametrize(
    "string, sub, expected",
    [
        ("catcowcat", "cat", 2),
        ("catcowcat", "cow", 1),
        ("catcowcat", "dog", 0),
        ("cacatcowcat", "cat", 2),
        ("xyx", "x", 2),
        ("iiiijj", "i", 4),
        ("iiiijj", "ii", 2),
        ("iiiijj", "iii", 1),
        ("iiiijj", "jj", 1),
        ("iiiijj", "j", 2),
        ("a", "abc", 0),
        ("", "foo", 0),
    ],
)
def test_str_count(string: str, sub: str, expected: int):
    result = recursion.str_count(string, sub)
    assert result == expected, fail_msg("str_count", expected, result, string)


@pytest.mark.parametrize(
    "string, sub, expected",
    [
        ("catcowcat", "cat", 9),
        ("catcowcat", "cow", 3),
        ("cccatcowcatxx", "cat", 9),
        ("abccatcowcatcatxyz", "cat", 12),
        ("xyx", "x", 3),
        ("xyx", "y", 1),
        ("xyx", "z", 0),
        ("z", "z", 1),
        ("z", "x", 0),
        ("", "x", 0),
    ],
)
def test_str_dist(string: str, sub: str, expected: int):
    result = recursion.str_dist(string, sub)
    assert result == expected, fail_msg("str_dist", expected, result, string)
