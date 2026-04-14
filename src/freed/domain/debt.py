class Debt:
    def __init__(self, id_nbr: int, principal: float, rate: float, minimum: float, frequency: int=12) -> None:
        self.id: int = id_nbr
        self.principal: float = principal
        self.rate: float = rate
        self.minimum: float = minimum
        self.frequency: float = frequency

    def calculate_compound(self, periods: int) -> float:
        new_principal: float = self.principal * (1 + self.rate / self.frequency) ** periods
        return new_principal

    def list_compounds(self, periods: int) -> list[float]:
        balance_list: list[float] = []
        period: int
        for period in range(periods + 1):
            balance_list.append(self.calculate_compound(period))

        return balance_list

    def calculate_next_principal(self, current_principal: float, current_payment: float = 0.0) -> float:
        next_principal: float = current_principal * (1 + self.rate / self.frequency) - current_payment
        return next_principal

    def list_minimum_payments(self, current_principal: float, periods: int, minimum: float):
        balance_list: list[float] = [float(current_principal)]
        next_period_principal: float = current_principal
        period: int
        for period in range(periods):
            next_period_principal: float = self.calculate_next_principal(current_principal, minimum)
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
