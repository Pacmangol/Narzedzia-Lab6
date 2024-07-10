import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description='Konwersja plików.')
    parser.add_argument('source', help='Ścieżka do pliku źródłowego')
    parser.add_argument('destination', help='Ścieżka do pliku docelowego')
    return parser.parse_args()

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print("JSON data:", data)
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    args = parse_arguments()
    load_json(args.source)
