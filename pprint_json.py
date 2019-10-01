import json
import argparse


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        return json.loads(file.read())


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


def create_parser():
    parser = argparse.ArgumentParser(description='JSON file address')
    parser.add_argument('filepath', nargs='?', default='my.json',
                        help='An optional filepath')
    args = parser.parse_args()
    return args


def main():
    try:
        filepath = create_parser().filepath
        data = load_data(filepath)
        pretty_print_json(data)
    except FileNotFoundError:
        exit('Файл не найден')
    except json.decoder.JSONDecodeError:
        exit('Файл не в формате JSON')


if __name__ == '__main__':
    main()
