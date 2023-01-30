from src.c09_smallest_multiple import smallest_multiple
import timeit


def test_smallest_multiple() -> None:
    setup_import = "from src.c09_smallest_multiple import smallest_multiple"

    correct_response = smallest_multiple(20) == 232792560

    time = timeit.timeit(
        "smallest_multiple(20)",
        setup=f"{setup_import}",
        number=1,
    )

    correct_time = time <= 0.005

    assert (
        correct_response and correct_time
    ), f"Falhou, o tempo foi: {time}, algoritmo correto? {correct_response}"
