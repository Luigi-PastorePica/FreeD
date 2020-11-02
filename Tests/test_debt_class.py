from src.debt_class import Debt

debt1 = Debt(id_nbr=1, principal=100, rate=0.1, minimum=0, frequency=12)
LIST_COMPOUNDS1 = [100.00, 100.83, 101.67, 102.52, 103.38, 104.24, 105.11, 105.98, 106.86, 107.76, 108.65, 109.56, 110.47,
                   111.39, 112.32, 113.26, 114.20, 115.15, 116.11, 117.08, 118.06, 119.04, 120.03, 121.03, 122.04]
PERIODS1 = len(LIST_COMPOUNDS1) - 1  # Should not count period 0

debt2 = Debt(id_nbr=2, principal=100, rate=0.1, minimum=10, frequency=12)
LIST_COMPOUNDS2 = [100.0, 90.83, 81.59, 72.27, 62.87, 53.40, 43.84, 34.21, 24.49, 14.70, 4.82, -5.14, -15.18,
                   -25.31, -35.52, -45.82, -56.20, -66.67, -77.22, -87.87, -98.60, -109.42, -120.33, -131.34, -142.43]
PERIODS2 = len(LIST_COMPOUNDS2) - 1

LIST_COMPOUNDS2_2 = [100.0, 90.83, 81.59, 72.27, 62.87, 53.40, 43.84, 34.21, 24.49, 14.70, 4.82, 0.0]
PERIODS2_2 = len(LIST_COMPOUNDS2_2)


def test_calculate_compound():
    abs_tolerance = 0.01
    passed = True
    for period in range(PERIODS1):
        calculated_compound = debt1.calculate_compound(period)
        sample_compound = LIST_COMPOUNDS1[period]
        # print(calculated_compound)
        # print(sample_compound)
        # print(abs(round(calculated_compound - sample_compound, 2)))
        if abs(round(calculated_compound - sample_compound, 2)) > abs_tolerance:
            passed = False
            break
    assert passed is True


def test_list_compounds():
    abs_tolerance = 0.01
    passed = True
    compounds_list = debt1.list_compounds(PERIODS1)
    if len(compounds_list) == len(LIST_COMPOUNDS1):
        for i, j in enumerate(compounds_list):
            if abs(round(j - LIST_COMPOUNDS1[i], 2)) > abs_tolerance:
                passed = False
                break
    else:
        passed = False

    assert passed is True


def test_calculate_next_principal():
    abs_tolerance = 0.01
    passed = True

    current_principal = debt1.principal
    minimum = debt1.minimum
    for index in range(PERIODS1):
        next_principal = debt1.calculate_next_principal(current_principal, minimum)
        # print("current " + str(current_principal))
        # print("next " + str(next_principal))
        # print("LIST_COMPOUNDS1[" + str(index) + " + 1] " + str(LIST_COMPOUNDS1[index+1]))
        if abs(round(next_principal - LIST_COMPOUNDS1[index+1], 2)) > abs_tolerance:
            passed = False
            break
        current_principal = next_principal

    if passed is True:
        current_principal = debt2.principal
        minimum = debt2.minimum
        for index in range(PERIODS2):
            next_principal = debt2.calculate_next_principal(current_principal, minimum)
            if abs(round(next_principal - LIST_COMPOUNDS2[index+1], 2)) > abs_tolerance:
                passed = False
                break
            current_principal = next_principal

    assert passed is True


def test_list_minimum_payments():

    abs_tolerance = 0.01
    passed = True
    compounds_wo_min = debt2.list_minimum_payments(debt2.principal, PERIODS2_2, debt2.minimum)
    if len(compounds_wo_min) == len(LIST_COMPOUNDS2_2) and compounds_wo_min[-1] == 0.0:
        for i, j in enumerate(compounds_wo_min):
            # print("compounds_wo_min[ " + str(i) + "] = " + str(compounds_wo_min[i]))
            # print("LIST_COMPOUNDS2_2[ " + str(i) + "] = " + str(LIST_COMPOUNDS2_2[i]))
            if abs(round(j - LIST_COMPOUNDS2_2[i], 2)) > abs_tolerance:
                passed = False
                break
    else:
        passed = False

    assert passed is True


# test_calculate_compound()

# test_list_compounds()

# test_calculate_next_principal()

# test_list_minimum_payments()
