from http.cookiejar import MONTHS


class Debt:
    def __init__(self, id_nbr, principal, rate, minimum, frequency=12):
        self.id = id_nbr
        self.principal = principal
        self.rate = rate
        self.minimum = minimum
        self.frequency = frequency

    def calculate_compound(self, periods):
        new_principal = self.principal * (1 + self.rate / self.frequency) ** periods
        return new_principal

    def list_compounds(self, periods):
        balance_list = []
        for period in range(periods + 1):
            balance_list.append(self.calculate_compound(period))

        return balance_list

    def calculate_next_principal(self, current_principal, current_payment = 0):
        next_principal = current_principal * (1 + self.rate / self.frequency) - current_payment
        return next_principal

    def list_minimum_payments(self, current_principal, periods, minimum):
        balance_list = [float(current_principal)]
        next_period_principal = current_principal
        for period in range(periods):
            next_period_principal = self.calculate_next_principal(current_principal, minimum)
            if next_period_principal < 0.0:
                balance_list.append(0.0)
                break

            balance_list.append(next_period_principal)
            current_principal = next_period_principal

        return balance_list

if __name__ == "__main__":
    MONTHS = 24
    debt1 = Debt(1, 1_000, 0.3, 100, 12)

    print(f"Compound over next {MONTHS} months.")
    for compound_val in debt1.list_compounds(MONTHS):
        print(compound_val)

    print(f"\nNext Principal")
    print(debt1.calculate_next_principal(100, 0))

    print(f"\nList minimum payments over {MONTHS} months")
    for minimum in debt1.list_minimum_payments(1000, MONTHS, 100):
        print(minimum)
