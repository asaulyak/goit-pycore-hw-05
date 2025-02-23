import sys
from datetime import datetime
from functools import reduce
from itertools import islice


def parse_log_line(line: str) -> dict:
    try:
        date, time, level, *message = line.split(' ')
        ful_date = ' '.join([date, time])

        return {
            'datetime': datetime.strptime(ful_date,'%Y-%m-%d %H:%M:%S'),
            'level': level.lower(),
            'message': ' '.join(message).strip()
        }
    except Exception as e:
        print('Error parsing log line:', e)


def load_logs(file_path: str) -> list:
    try:
        with open(file_path) as file:
            for line in file:
                yield parse_log_line(line)
    except FileNotFoundError:
        print(f"File {file_path} not found")
    except Exception as e:
        print(f"An error occurred: {e}")


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]


def count_logs_by_level(logs: list) -> dict:
    return reduce(lambda acc, log: {**acc, log['level']: acc.get(log['level'], 0) + 1}, logs, {})

def format_log_line(line):
    return f"{line['datetime']} - {line['message']}"

def display_logs(logs: list, head):
    body = '\n'.join(map(format_log_line, logs))

    print(head)
    print(body)

def display_log_counts(counts: dict):
    column_1 = 'Рівень логування'
    column_2 = 'Кількість'
    head = ' | '.join([column_1, column_2])
    divider = '-' * len(column_1) + ' | ' + '-' * len(column_2)

    lines = [(level.upper() + ' ' * (len(column_1) - len(level))+ ' | ' + str(count)) for level, count in counts.items()]
    body = '\n'.join(lines)

    print(head)
    print(divider)
    print(body)


def main():
    if len(sys.argv) < 2:
        print('Provide path to log file as an argument')
        sys.exit(1)

    path = sys.argv[1]
    log_level = sys.argv[2].lower() if len(sys.argv) > 2 else None

    # get the first 100 lines from the log file
    logs = list(islice(load_logs(path), 100))

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if log_level:
        filtered = filter_logs_by_level(logs, log_level)
        print('\n')
        display_logs(filtered, f'Деталі логів для рівня \'{log_level.upper()}\':')


if __name__ == "__main__":
    main()