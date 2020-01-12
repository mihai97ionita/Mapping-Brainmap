import os
import json
import sys
import time
import getopt


def parse_content(field, text):
    files = []
    for file in os.listdir("jsons"):
        files.append(os.path.join("jsons", file))

    outfile = os.path.join("results", get_next_file_name())
    of = open(outfile, "w", encoding="utf-8")

    of.write(f"Project matches for text <{text.upper()}> in field <{field.upper()}>")

    for file in files:
        author = os.path.splitext(os.path.basename(file))[0]
        printed_name = False
        f = open(file, "r")

        try:
            data = json.load(f)
        except:
            continue

        for i in range(len(data)):
            filed_data = data[i][field]
            title = data[i]["title"]

            # treat list field separately
            if type(filed_data) is list:
                for item in filed_data:
                    if text.lower() in item.lower():
                        if not printed_name:
                            printed_name = True
                            of.write(f"\n\n{author.upper()}\n")
                        print(f"{author} matches your search with the project -- {title}")
                        project = json.dumps(data[i], indent=2)
                        of.write(f"{project}\n")
            else:
                if text.lower() in filed_data.lower():
                    if not printed_name:
                        printed_name = True
                        of.write(f"\n\n{author.upper()}\n")
                    print(f"{author} matches your search with the project -- {title}")
                    project = json.dumps(data[i], indent=2)
                    of.write(f"{project}\n")

        f.close()

    of.close()
    print(f"\nMore details about the matches in {outfile}\n")


def get_next_file_name():
    idx = len(os.listdir("results")) + 1
    return f"result_{idx}.txt"


def main(argv):
    field = ""
    text = ""
    try:
        opts, argv = getopt.getopt(argv, "hf:t:", ["help", "field", "text"])

    except getopt.GetoptError:
        print("content_parser.py -f <field> -t <key_word>\n"
              "try --help for more details")
        sys.exit(2)

    if len(opts) == 0:
        print("Not enough arguments given!\nTry content_parser.py --help for more details")
        sys.exit(2)
    elif len(opts) == 1 and opts[0][0] not in ["-h", "--help"]:
        print(f"Not enough arguments given!\nTry content_parser.py --help for more details")
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

    if not os.path.isdir("results"):
        os.makedirs("results")


    print(f"################ BEGIN PARSER ################")
    start = time.time()
    parse_content(field, text)
    end = time.time()
    print(f"parser finished in {round(end-start)} seconds")
    print(f"#################### DONE ####################")


if __name__ == "__main__":
    main(sys.argv[1:])
