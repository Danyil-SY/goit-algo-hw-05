'''
    Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.

    Файли логів – це файли, що містять записи про події, які відбулися в операційній системі, програмному забезпеченні або інших системах. Вони допомагають відстежувати та аналізувати поведінку системи, виявляти та діагностувати проблеми.

    Для виконання завдання візьміть наступний приклад лог-файлу:

    2024-01-22 08:30:01 INFO User logged in successfully.
    2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
    2024-01-22 09:00:45 ERROR Database connection failed.
    2024-01-22 09:15:10 INFO Data export completed.
    2024-01-22 10:30:55 WARNING Disk usage above 80%.
    2024-01-22 11:05:00 DEBUG Starting data backup process.
    2024-01-22 11:30:15 ERROR Backup process failed.
    2024-01-22 12:00:00 INFO User logged out.
    2024-01-22 12:45:05 DEBUG Checking system health.
    2024-01-22 13:30:30 INFO Scheduled maintenance.
'''

import sys


# Parse logs
def parse_log_line(line: str) -> dict:
    parts = line.split(maxsplit=3)

    return {'date': parts[0], 
            'time': parts[1], 
            'level': parts[2], 
            'message': parts[3].strip()}

# Load logs from a file
def load_logs(file_path: str) -> list:
    logs = []

    with open(file_path, 'r') as file:
        for line in file:
            logs.append(parse_log_line(line))

    return logs

# Filter logs by level
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    counts = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}

    for log in logs:
        counts[log['level']] += 1

    return counts

# Show results
def display_log_counts(counts: dict) -> None:
    print("Log Level   |   Count")
    print("---------------------")

    for level, count in counts.items():
        print(f"{level.ljust(11)} |   {count}")

# Main function
def main(file_path: str, level: str = None) -> None:
    logs = load_logs(file_path)

    if level:
        logs = filter_logs_by_level(logs, level)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <file_path> [<level>]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None
    main(file_path, level)