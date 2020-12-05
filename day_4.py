"""
Puzzle 1:
Count the number of valid passports - those that have all required fields.
Treat cid as optional. In your batch file, how many passports are valid?

Puzzle 2:
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
"""
import re


class Passport:
    _birth_year = 0
    _issue_year = 0
    _expiration_year = 0
    _height = 0
    _hair_color = ""
    _eye_color = ""
    _passport_id = ""
    _country_id = ""

    def __init__(self, byr: int = None, iyr: int = None, eyr: int = None, hgt: str = None, hcl: str = None,
                 ecl: str = None, pid: str = None, cid: str = None):
        self._birth_year = byr
        self._issue_year = iyr
        self._expiration_year = eyr
        self._height = hgt
        self._hair_color = hcl
        self._eye_color = ecl
        self._passport_id = pid
        self._country_id = cid

    def __repr__(self):
        return f"Passport BYR:{self._birth_year} IYR:{self._issue_year} EYR:{self._expiration_year} HGT:{self._height} \
HCL:{self._hair_color} ECL:{self._eye_color} PID:{self._passport_id} CID:{self._country_id}"

    def validate(self, cid_optional: bool, complex_check: bool) -> bool:
        if not complex_check:
            if self._birth_year is not None and self._issue_year is not None and self._expiration_year is not None and \
                    self._height is not None and self._hair_color is not None and self._eye_color is not None and \
                    self._passport_id is not None:
                if cid_optional:
                    return True
                else:
                    return self._country_id is not None
            else:
                return False
        else:
            if self.validate(True, False):
                hcl_regex = re.compile(r"#[0-9a-zA-Z]{6}")
                ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                pid_regex = re.compile(r"[0-9]{9}")
                byr_valid = 1920 <= int(self._birth_year) <= 2002
                iyr_valid = 2010 <= int(self._issue_year) <= 2020
                eyr_valid = 2020 <= int(self._expiration_year) <= 2030
                if self._height.endswith("cm"):
                    height_cm = int(self._height.strip("cm"))
                    hgt_valid = 150 <= height_cm <= 193
                elif self._height.endswith("in"):
                    height_in = int(self._height.strip("in"))
                    hgt_valid = 59 <= height_in <= 76
                else:
                    return False
                hcl_valid = hcl_regex.match(self._hair_color)
                ecl_valid = False
                for color in ecl_list:
                    if color == self._eye_color:
                        ecl_valid = True
                        break
                pid_valid = pid_regex.match(self._passport_id)
                if byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid:
                    return True
                else:
                    return False
            else:
                return False


DATA_SET = "datasets/day_4_puzzle_1.txt"
DELIMITER = "\n"


def process_raw_document(doc):
    doc_data = {'byr': None,
                'iyr': None,
                'eyr': None,
                'hgt': None,
                'hcl': None,
                'ecl': None,
                'pid': None,
                'cid': None}
    processable_lines = []
    for line in doc:
        blocks = line.split(" ")
        for block in blocks:
            # processable_lines.append(block.replace("\n", ""))
            processable_lines.append(block)
        for key_and_value in processable_lines:
            key_and_value_data = key_and_value.split(":")
            doc_data[key_and_value_data[0]] = key_and_value_data[1]
    return doc_data


def puzzle(complex_check: bool):
    valid_docs = 0
    documents_raw = []
    lines = []
    with open(DATA_SET, "r") as file:
        for line in file.readlines():
            if line == "\n":
                if len(lines) > 0:
                    documents_raw.append(lines)
                    lines = []
            else:
                lines.append(line)

    for document_raw in documents_raw:
        p_data = process_raw_document(document_raw)
        passport = Passport(p_data['byr'], p_data['iyr'], p_data['eyr'], p_data['hgt'], p_data['hcl'], p_data['ecl'],
                            p_data['pid'], p_data['cid'])
        if passport.validate(True, complex_check):
            print(passport)
            valid_docs += 1
    print(f"Valid passports: {valid_docs}.")


if __name__ == "__main__":
    # Puzzle 1:
    puzzle(True)

    # Puzzle 2:
    # puzzle(True)
