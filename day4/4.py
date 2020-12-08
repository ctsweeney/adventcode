#!/usr/bin/env python3

import re


def read_passport_file(data) -> list:
    with open(data) as pp:
        passport_data = pp.read().split("\n\n")
        return passport_data


class Passport:
    check_data = ["eyr", "hgt", "iyr", "byr", "pid", "cid", "ecl", "hcl"]

    def __init__(self, data) -> None:
        self.passports = data

    def check_total_valid_passport1(self):
        total_valid_passports = 0
        for passport in self.passports:
            valid_field_set = set(self.check_data)
            passport_list = re.split(" |\n", passport)
            for item in passport_list:
                code = item[:item.index(":")]
                valid_field_set.remove(code)

            if len(valid_field_set) == 1:
                if valid_field_set.pop() == "cid":
                    total_valid_passports += 1
            elif len(valid_field_set) == 0:
                total_valid_passports += 1

        return total_valid_passports

    def check_total_valid_passport2(self):
        total_valid_passports = 0
        for passport in self.passports:
            valid_passport = set(self.check_data)
            fields = re.split(" |\n", passport)
            for f in fields:
                key = f[:f.index(":")]
                value = f[f.index(":") + 1:]

                # Lets do some data checks on the each valid value
                if key == "byr":
                    if not 1920 <= int(value) <= 2002:
                        continue

                elif key == "iyr":
                    if not 2010 <= int(value) <= 2020:
                        continue

                elif key == "eyr":
                    if not 2020 <= int(value) <= 2030:
                        continue

                elif key == "hgt":
                    if not value[-2:] in ["in", "cm"]:
                        continue

                    if value[-2:] == "in":
                        if not 59 <= int(value[:-2]) <= 76:
                            continue

                    else:
                        if not 150 <= int(value[:-2]) <= 193:
                            continue

                elif key == "hcl":
                    if not re.fullmatch("#([0-9]|[a-f]){6}", value):
                        continue

                elif key == "ecl":
                    if not re.fullmatch("amb|blu|brn|gry|grn|hzl|oth", value):
                        continue

                elif key == "pid":
                    if not re.fullmatch("[0-9]{9}", value):
                        continue

                valid_passport.remove(key)

            if len(valid_passport) == 1:
                if valid_passport.pop() == "cid":
                    total_valid_passports += 1
            elif len(valid_passport) == 0:
                total_valid_passports += 1

        return total_valid_passports


data = read_passport_file('passport.txt')
passport = Passport(data)
print(
    f"The number of valid passports is: {passport.check_total_valid_passport1()}")
print(
    f"The number of valid passports with data validation is: {passport.check_total_valid_passport2()}")
