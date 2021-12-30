import random

from src.validate_rg import validate_rg

VALID_RG_LIST_WITH_MASK = [
    '12.738.958-1',
    '45.110.371-3',
    '45.038.255-2',
    '50.567.509-2',
    '25.401.751-4',
    '23.446.712-5',
    '41.554.447-6',
    '31.180.011-7',
    '17.780.093-8',
    '11.514.066-9',
]
VALID_RG_LIST_WITHOUT_MASK = [
    '127389581',
    '451103713',
    '450382552',
    '505675092',
    '254017514',
    '234467125',
    '415544476',
    '311800117',
    '177800938',
    '115140669',
]
INVALID_RG_LIST_WITH_MASK = [
    '12.738.158-1',
    '45.110.171-3',
    '45.038.155-2',
    '50.567.109-2',
    '25.401.151-4',
    '23.446.112-5',
    '41.554.147-6',
    '31.180.111-7',
    '17.780.193-8',
    '11.514.166-9',
]
INVALID_RG_LIST_WITHOUT_MASK = [
    '127381581',
    '451101713',
    '450381552',
    '505671092',
    '254011514',
    '234461125',
    '415541476',
    '311801117',
    '177801938',
    '115141669',
]

VALID_RG_WITH_MASK = random.choice(VALID_RG_LIST_WITH_MASK)
VALID_RG_WITHOUT_MASK = random.choice(VALID_RG_LIST_WITHOUT_MASK)

INVALID_RG_WITH_MASK = random.choice(INVALID_RG_LIST_WITH_MASK)
INVALID_RG_WITHOUT_MASK = random.choice(INVALID_RG_LIST_WITHOUT_MASK)


def test_validate_rg_module():
    assert validate_rg is not None


def test_clean_rg():
    clened_rg = validate_rg._clean(INVALID_RG_WITH_MASK)
    assert all(i.isdigit() == True for i in clened_rg)
    clened_rg = validate_rg._clean(VALID_RG_WITH_MASK)
    assert all(i.isdigit() == True for i in clened_rg)


def test_is_not_allowed_rg():
    ALLOWED_RG = '111111111'
    assert validate_rg._is_allowed(ALLOWED_RG) == False


def test_is_allowed_rg():
    assert validate_rg._is_allowed(VALID_RG_WITHOUT_MASK) == True


def test_verification_digit():
    DV = VALID_RG_WITHOUT_MASK[-1]
    assert validate_rg._caculate_digit(VALID_RG_WITHOUT_MASK) == DV


def test_invalid_rg_without_mask():
    RG = INVALID_RG_WITHOUT_MASK
    assert validate_rg.is_valid(RG) == False


def test_invalid_rg_with_mask():
    RG = INVALID_RG_WITH_MASK
    assert validate_rg.is_valid(RG) == False


def test_valid_rg_without_mask():
    RG = VALID_RG_WITHOUT_MASK
    assert validate_rg.is_valid(RG) == True


def test_valid_rg_with_mask():
    RG = VALID_RG_WITH_MASK
    assert validate_rg.is_valid(RG) == True


def test_all_invalid_rg_with_mask():
    for RG in INVALID_RG_LIST_WITH_MASK:
        assert validate_rg.is_valid(RG) == False


def test_all_invalid_rg_without_mask():
    for RG in INVALID_RG_LIST_WITHOUT_MASK:
        assert validate_rg.is_valid(RG) == False


def test_all_valid_rg_with_mask():
    for RG in VALID_RG_LIST_WITH_MASK:
        assert validate_rg.is_valid(RG) == True


def test_all_valid_rg_without_mask():
    for RG in VALID_RG_LIST_WITHOUT_MASK:
        assert validate_rg.is_valid(RG) == True
