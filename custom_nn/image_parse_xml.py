import argparse
import json
import re

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to iBug 300-W data XML file")
ap.add_argument("-t", "--output", required=True, help="path to output data JSON file")
args = vars(ap.parse_args())

IMAGE = re.compile(r"image file='")

print("[INFO] Parsing data XML file...")
rows = open(args['input']).read().strip().split("\n")
output = open(args['output'], 'w')

images = []

for idx, row in enumerate(rows):
    image = re.findall(IMAGE, row)

    if len(image) != 0:
        attr_file = "file='"
        i = row.find(attr_file)
        j = row.find("'", i + len(attr_file) + 1)
        file_name = row[i + len(attr_file):j]

        attrs_pos = ["top='", "left='", "width='", "height='"]
        rect = []
        for a_idx, attr in enumerate(attrs_pos):
            i = rows[idx+1].find(attr)
            j = rows[idx+1].find("'", i + len(attr) + 1)
            rect.append(int(rows[idx+1][i + len(attr):j]))

        if rect[0] >= 0 and rect[1] >= 0 and rect[2] >= rect[0] and rect[3] >= rect[1]:
            images.append({
                "file" : file_name,
                "t" : rect[0],
                "l" : rect[1],
                "w" : rect[2],
                "h" : rect[3]
            })

json.dump(images, output, indent=4)
output.close()