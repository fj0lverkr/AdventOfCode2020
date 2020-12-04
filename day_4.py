"""
Puzzle 1:
Count the number of valid passports - those that have all required fields.
Treat cid as optional. In your batch file, how many passports are valid?
"""


class Passport:
    _birth_year = 0
    _issue_year = 0
    _expiration_year = 0
    _height = 0
    _hair_color = ""
    _eye_color = ""
    _passport_id = ""
    _country_id = ""

    def __init__(self, byr: int = None, iyr: int = None, eyr: int = None, hgt: int = None, hcl: str = None,
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
            # TODO implement logic for complex checking from second puzzle
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
            processable_lines.append(block.replace("\n", ""))
        for key_and_value in processable_lines:
            key_and_value_data = key_and_value.split(":")
            doc_data[key_and_value_data[0]] = key_and_value_data[1]
    return doc_data


def puzzle_1():
    valid_docs = 1
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
        print(passport)
        if passport.validate(True, False):
            valid_docs += 1
    print(f"Valid passports: {valid_docs}.")


if __name__ == "__main__":
    puzzle_1()
