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
            return data
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return None
    except FileNotFoundError:
        print("File not found.")
        return None

def save_json(data, file_path):
    if data is None:
        print("No data to save.")
        return
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Failed to save data: {e}")

if __name__ == "__main__":
    args = parse_arguments()
    data = load_json(args.source)
    save_json(data, args.destination)
