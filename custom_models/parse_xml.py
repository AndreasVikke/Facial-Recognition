import argparse
import re

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to iBug 300-W data XML file")
ap.add_argument("-t", "--output", required=True, help="path to output data XML file")
args = vars(ap.parse_args())

LANDMARKS = set(list(range(36, 48)))

PART = re.compile(r"part name='[0-9]+'")

print("[INFO] PArsing data XML file...")
rows = open(args['input']).read().strip().split("\n")
output = open(args['output'], 'w')

for row in rows:
    parts = re.findall(PART, row)

    if len(parts) == 0:
        output.write("{}\n".format(row))
    else:
        attr = "name='"
        i = row.find(attr)
        j = row.find("'", i + len(attr) + 1)
        name = int(row[i + len(attr):j])

        if name in LANDMARKS:
            output.write("{}\n".format(row))

output.close()