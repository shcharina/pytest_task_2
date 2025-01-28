import pytest

from src.price_formatting import get_price_filter_title

@pytest.mark.parametrize(
    'price_from, price_to, expected_title',
    [
        (0,0, '¯\_(ツ)_/¯'),
        (400, 200, '400 - 400 ₽'),
        (20, 30, '20 - 30 ₽'),
        (20, 300_000, '20 - 300 тыс ₽'),
        (2001, 300_000, '2 - 300 тыс ₽'),
        (2001, 300_000_000, '2 тыс - 300 млн ₽'),
        (1_000_000_000_000, 1_000_000_000_999, '1000 - 1000 млрд ₽'),
        (123_456_789_123, 999_999_999_999, '123.5 - 1000 млрд ₽'),
        (2001, None, 'от 2 тыс ₽'),
        (None, 100_500, 'до 100.5 тыс ₽'),
        (None, 10_050_000, 'до 10.1 млн ₽'),
        (None, None, 'Цена')
    ]
)
def test_get_price_filter_title(price_from, price_to, expected_title):
    # Arrange & Act
    title = get_price_filter_title(price_from=price_from, price_to=price_to)

    # Assert
    assert title == expected_title