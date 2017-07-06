import re


def FindFeature(feature, table):
    # feature = 'Covalent radius'
    found = False
    for line in table.splitlines():
        if found:
            #print(line)
            nr = ExtractNumber(line)
            return nr
        match = re.search(feature, line)
        if match:
            # print(match.group(0))
            found = True


def ExtractNumber(line):
    x = re.findall(r'\d+', line)
    return x
