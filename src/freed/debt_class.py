class Debt(object):
    def __init__(self, id_nbr, principal, rate, minimum, frequency=12):
        self.id = id_nbr
        self.principal = principal
        self.rate = rate
        self.minimum = minimum
        if frequency > 0:
            self.frequency = frequency
        else:
            raise ValueError("Frequency should be higher than 0. Value given is {}.\n".format(frequency))

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

    def __repr__(self):
        return "{{id: {}, principal: {}, rate: {}, minimum: {}, frequency: {}}}".\
            format(self.id, self.principal, self.rate, self.minimum, self.frequency)
