import sys
import re

def parse_log_line(line: str) -> dict:
    try:
        parts = line.strip().split(' ', 3)
        if len(parts) < 4:
            raise ValueError("Неправильний формат рядка логу")
        date, time, level, message = parts
        return {
            'date': date,
            'time': time,
            'level': level.upper(),
            'message': message
        }
    except Exception as e:
        print(f"Помилка парсингу рядка: {line}\n{e}")
        return {}
    

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            logs = list(filter(None, [parse_log_line(line) for line in file]))
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при зчитуванні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"].lower() == level.lower(), logs))


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level.upper():<17}| {count}")


def display_logs(logs: list, level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py path/to/logfile.log [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if filter_level:
        filtered = filter_logs_by_level(logs, filter_level)
        if filtered:
            display_logs(filtered, filter_level)
        else:
            print(f"\nНе знайдено записів для рівня '{filter_level.upper()}'.")


if __name__ == "__main__":
    main()