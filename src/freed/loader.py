import csv

debt_attr = ["id", "principal", "rate", "minimum", "frequency"]  # More attributes might be added in the future.
numerical_attr = ["id", "principal", "rate", "minimum", "frequency"] # This list includes only the numerical attributes.


def load_user(uid):
    """
    Loads the data used to instantiate a single user object.
    Not implemented yet. load_debt_list() does the heavy lifting for now.

    Parameters
    ----------
    uid : The unique id number of the user

    Returns
    -------
    user : An instance of the user class
    """
    raise NotImplementedError


def load_debt_list(uid):
    user_file = "{}.csv".format(str(uid))
    debt_list = []
    try:
        with open(user_file, 'r', newline='') as ufile:
            user_reader = csv.DictReader(ufile)
            for row in user_reader:
                debt_list.append({attr: int_or_float(row[attr]) if attr in numerical_attr else row[attr] for attr in debt_attr})

    except FileNotFoundError as e:
        print(e.strerror + "\nCreating file now\n")
        with open(user_file, 'w', newline='') as ufile:
            user_writer = csv.DictWriter(ufile, debt_attr)
            user_writer.writeheader()

    return debt_list


def update_db(mode, uid, debt_vals):
    user_file = "{}.csv".format(str(uid))
    debt_id = -1
    if mode == "add":
        debt_list = load_debt_list(uid)
        if debt_list:
            debt_id = int(debt_list[-1]["id"]) + 1
        else:
            debt_id = 0
        debt_vals["id"] = debt_id
        with open(user_file, 'a', newline='') as user_file:
            writer = csv.DictWriter(user_file, debt_attr)
            writer.writerow(debt_vals)
    elif mode == "rm":
        debt_list = load_debt_list(uid)
        for debt in debt_list:
            if debt["id"] == debt_vals.id:
                debt_list.remove(debt)
                break
        with open(user_file, 'w', newline='') as user_file:
            writer = csv.DictWriter(user_file, debt_attr)
            writer.writeheader()
            writer.writerows(debt_list)
        debt_id = debt_vals.id
    elif mode == "mod":
        debt_list = load_debt_list(uid)
        for debt in debt_list:
            if debt["id"] == debt_vals["id"]:
                for key, value in debt_vals.items():
                    debt["key"] = value
                break
        with open(user_file, 'w', newline='') as user_file:
            writer = csv.DictWriter(user_file, debt_attr)
            writer.writeheader()
            writer.writerows(debt_list)
        debt_id = debt_vals["id"]
    else:
        raise ValueError("Mode must be one of add, rm, mod")

    return debt_id


def int_or_float(num_string):
    number = 0
    try:
        number = int(num_string)
    except ValueError:
        number = float(num_string)

    return number
