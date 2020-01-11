import os
import json
import sys
import time
import getopt

def parse_content(field, text):
    files = []
    for file in os.listdir("jsons"):
        files.append(os.path.join("jsons", file))

    for file in files:
        f = open(file, "r")
        try:
            data = json.load(f)
        except:
            continue
        titlu = data[0]["title"]
        print(f"{file}: {titlu}")
        


def main(argv):
    field = ""
    text = ""
    try:
        opts, argv = getopt.getopt(argv, "hf:t:", ["help", "field", "text"])

    except getopt.GetoptError:
        print("content_parser.py -f <field> -t <key_word>\n"
              "try --help for more details")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ["-h", "--help"]:
            print("content_parser.py -f <field> -t <key_word>")
            print("\nSearch for the key_word given with option -t in the field "
                  "given with option -f")
            sys.exit(2)
        elif opt in ["-f", "--field"]:
            field = arg
        elif opt in ["-t", "--text"]:
            text = arg
        else:
            print(f"Unknown option -- {opt}")
            sys.exit(2)

    print(f"field -- {field}")
    print(f"text -- {text}")
    print(f"################ BEGIN PARSER ################")
    start = time.time()
    parse_content(field, text)
    end = time.time()
    print(f"parser finished in {round(end-start)} seconds")
    print(f"#################### DONE ####################")


if __name__ == "__main__":
    main(sys.argv[1:])
