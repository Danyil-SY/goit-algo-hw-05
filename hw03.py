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


def parse_log_line(line: str) -> dict:
    """
    Parse a log line and return a dictionary with date, time, level, and message.
    """
    parts = line.split(maxsplit=3)

    return {
        'date': parts[0], 
        'time': parts[1], 
        'level': parts[2], 
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    """
    Load logs from a file and return a list of log dictionaries.
    """
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except Exception as e:
        print(f"Exception: {e}")   
    return logs

def count_logs_by_level(logs: list) -> dict:
    """
    Count logs by level and return a dictionary with counts for each level.
    """
    counts = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict) -> None:
    """
    Print log level counts.
    """
    print("Log Level   |   Count")
    print("---------------------")
    for level, count in counts.items():
        print(f"{level.ljust(11)} |   {count}")

def show_logs_by_level(logs: list, level: str) -> list:
    """
    Print details of logs for the specified level.
    """
    filtered_logs = [log for log in logs if log['level'] == level.upper()]
    print(f"\nDetails of logs for level '{level.upper()}':")
    for log in filtered_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main(file_path: str, level: str = None) -> None:
    """
    Main function to analyze log files.
    """
    logs = load_logs(file_path)

    if not logs:
        return
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    
    if level:
        show_logs_by_level(logs, level)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <file_path> [<level>]")
    else:
        file_path = sys.argv[1]
        level = sys.argv[2] if len(sys.argv) > 2 else None
        main(file_path, level)