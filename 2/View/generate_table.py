from random import choice, randint


def generate_table(number_of_rows):
    names = ["Liam", "Olivia", "Noah", "Emma",
             "Oliver", "Ava", "Elijah", "Charlotte",
             "William", "Sophia", "James", "Amelia",
             "Eric", "Kyle", "Kenny", "Stenley"]

    last_names = ["Smith", "Jonhson", "Jones", "Brown",
                  "Garcia", "Miller", "Davis", "Taylor",
                  "Cartman", "Broflovski", "McCormick", "Marsh",
                  "Lee", "King", "Scott", "Stewart"
                  ]
    res = []

    for _ in range(number_of_rows):
        name = choice(names)
        last_name = choice(last_names)
        full_name = " ".join([name, last_name])
        group = randint(10, 20)
        sick = randint(0, 100)
        absent = randint(0, 100)
        other = randint(0, 100)
        res.append([full_name, group, sick, absent, other])

    return res