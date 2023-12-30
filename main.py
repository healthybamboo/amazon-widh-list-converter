import sys
from csv_convert import CsvConverter


def main(path):
    csv_converter = CsvConverter(path)
    csv_converter.dump()

if __name__ == "__main__":
    args = sys.argv[1:]

    if not len(args) == 1:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    main(path=args[0])
    print('Done')
