from random import choice, randint
import bisect


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
        group = "".join((str(randint(0, 4)), str(randint(1, 9))))
        sick = str(randint(0, 100))
        absent = str(randint(0, 100))
        other = str(randint(0, 100))
        bisect.insort(res, [full_name, group, sick, absent, other])
    return res
