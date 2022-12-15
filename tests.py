from lab3 import record, cashcalculator, caloriescalculator
import pytest


@pytest.fixture()
def test_calories_calculator():
    cal_calculate = caloriescalculator(2000)
    cal_calculate.add_record((record(amount=106, comment='Авокадо')))
    cal_calculate.add_record((record(amount=120, comment='Красная рыба')))
    cal_calculate.add_record((record(amount=212, comment='Яичница')))
    cal_calculate.add_record((record(amount=141, comment='Хлебцы')))
    return cal_calculate.get_calories_remained()


def test_cal_calc1(test_calories_calculator):
    assert (
            test_calories_calculator != f'Сегодня Вы достаточно кушали!')
    print("\n", test_calories_calculator)


@pytest.fixture()
def test_cash_calculator():
    cash_calculate = cashcalculator(1000)
    cash_calculate.add_record((record(amount=220, comment='Такси')))
    cash_calculate.add_record((record(amount=120, comment='Мокко')))
    cash_calculate.add_record((record(amount=79, comment='Шоколадка')))
    return cash_calculate.get_cash_remained('rub')


def test_cash_calc1(test_cash_calculator):
    assert (
            test_cash_calculator != f'На сегодня деньги кончились!')
    print("\n", test_cash_calculator)


@pytest.mark.parametrize("cal, message", [
    (600, 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 21 Ккал'),
    (579, 'Сегодня Вы достаточно кушали!')
])
def test_calories_variations(cal, message):
    cal_calculate = caloriescalculator(cal)
    cal_calculate.add_record((record(amount=106, comment='Авокадо')))
    cal_calculate.add_record((record(amount=120, comment='Красная рыба')))
    cal_calculate.add_record((record(amount=212, comment='Яичница')))
    cal_calculate.add_record((record(amount=141, comment='Хлебцы')))
    assert cal_calculate.get_calories_remained() == message
    print("\n", cal_calculate.get_calories_remained())


@pytest.mark.parametrize("cash, message", [
    (1000, 'На сегодня денег осталось: 581.0 руб'),
    (419, 'На сегодня деньги кончились!'),
    (200, 'Сегодня Вы ушли в долг: -219.0 руб')
])
def test_cash_variations(cash, message):
    cash_calculate = cashcalculator(cash)
    cash_calculate.add_record((record(amount=220, comment='Такси')))
    cash_calculate.add_record((record(amount=120, comment='Мокко')))
    cash_calculate.add_record((record(amount=79, comment='Шоколадка')))
    assert cash_calculate.get_cash_remained('rub') == message
    print("\n", cash_calculate.get_cash_remained('rub'))
