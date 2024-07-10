import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Konwersja plików.')
    parser.add_argument('source', help='Ścieżka do pliku źródłowego')
    parser.add_argument('destination', help='Ścieżka do pliku docelowego')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(f"Source: {args.source}, Destination: {args.destination}")
