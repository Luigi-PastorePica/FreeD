class Debt:
    def __init__(self, id, principal, rate, minimum, frequency=12):
        self.id = id
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

    def list_minimum_payments(self, current_principal, periods, minimum = 0):
        balance_list = [float(current_principal)]
        for period in range(periods):
            next_period_principal = self.calculate_next_principal(current_principal, minimum)
            balance_list.append(next_period_principal)
            current_principal = next_period_principal

        return balance_list


# # TODO Convert this into a test
debt1 = Debt(1, 100, 0.1, 0, 12)
# print("Compounds:")
# for value in debt1.list_compounds(24):
#     print(value)
print("Balances:")
for value in debt1.list_minimum_payments(100, 24, 10):
    print(value)
