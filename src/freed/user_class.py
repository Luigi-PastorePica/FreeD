import debt_class as dbt
import loader


class User:
    def __init__(self, uid, name, debt_list):
        self.uid = uid
        self.name = name
        # self.debt_list = debt_list
        self.debt_list = [dbt.Debt(d["id"], d["principal"], d["rate"], d["minimum"], d["frequency"]) for d in debt_list]

    def add_debt(self, debt_dict):
        d = debt_dict
        d["id"] = loader.update_db("add", self.uid, debt_dict)
        self.debt_list.append(dbt.Debt(d["id"], d["principal"], d["rate"], d["minimum"], d["frequency"]))

    def remove_debt(self, debt_id):
        for debt in self.debt_list:
            if debt.id == debt_id:
                loader.update_db("rm", self.uid, debt)
                self.debt_list.remove(debt)
                break

    def list_debts(self):
        return self.debt_list
