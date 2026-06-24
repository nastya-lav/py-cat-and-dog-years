import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_array",
    [
        pytest.param(
            0, 0, [0, 0],
            id="test should return zero when age is zero"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="test should add human year for first 15 animal's years"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="test should add second human year for next 9 animal's years past 15th"  # noqa: E501
        ),
        pytest.param(
            100, 100, [21, 17],
            id="test should convert age for each animal accordingly"
        )
    ]
)
def test_should_convert_age_correctly(
    cat_age: int,
    dog_age: int,
    expected_array: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_array


def test_should_raise_exception_if_age_is_negative() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -1)
