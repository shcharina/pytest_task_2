_PRICE_VOCABULARY = {
    1_000_000_000: 'млрд',
    1_000_000: 'млн',
    1_000: 'тыс'
}
_DEFAULT_TITLE = 'Цена'
_UNIT = '₽'
_MAX_PRICE = 999_999_999_999

def get_price_filter_title(price_from: int | None, price_to: int | None) -> str:
    if price_from is None and price_to is None:
        return _DEFAULT_TITLE
    if price_from == 0 and price_to == 0:
        return '¯\_(ツ)_/¯'

    # Editing&Formatting prices
    if price_to is not None and price_from is not None and price_to < price_from:
        price_to = price_from
    if price_from is not None:
        if price_from > _MAX_PRICE:
            price_from = _MAX_PRICE
        price_from = format_number(price_from)
    if price_to is not None:
        if price_to > _MAX_PRICE:
            price_to = _MAX_PRICE
        price_to = format_number(price_to)

    if price_to is not None and price_from is not None and price_from[1] == price_to[1]:
        del price_from[1]

    for price_list in price_from, price_to:
        if price_list is not None and '' in price_list:
            price_list.remove('')
    price_from = ' '.join(price_from) if price_from is not None else price_from
    price_to = ' '.join(price_to) if price_to is not None else price_to

    # Returning a suitable title
    if price_to is None:
        return f'от {price_from} {_UNIT}'
    if price_from is None:
        return f'до {price_to} {_UNIT}'

    return f'{price_from} - {price_to} {_UNIT}'

def format_number(num: int) -> list[str]:
    for price in _PRICE_VOCABULARY:
        if num >= price:
            num = num / price
            string_num = f'{num:.1f}'.rstrip('0').rstrip('.')
            return [string_num, _PRICE_VOCABULARY[price]]
    return [str(num), '']