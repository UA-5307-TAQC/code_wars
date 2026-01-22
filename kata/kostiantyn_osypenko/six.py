"""Solutions for 6 kyu tasks."""

import re


def find_nb(m):
    """Build a pile of Cubes solution."""
    i = 1
    n = 0
    while m > 0:
        m -= i**3
        i += 1
        n += 1
    return n if m == 0 else -1


def balance(book: str):
    """Easy balance checking solution."""
    lines = book.splitlines()
    clean_lines = []

    for line in lines:
        if not line:
            continue
        clean_line = "".join(char for char in line if char.isalnum() or char in ". ")
        clean_lines.append(clean_line)

    original_balance = float(clean_lines[0])
    total_expense = 0
    report = [f"Original Balance: {original_balance:.2f}"]

    for i in range(1, len(clean_lines)):
        num, category, amount = clean_lines[i].split(" ")
        total_expense += float(amount)
        new_line = f"{num} {category} {float(amount):.2f} Balance {original_balance - total_expense:.2f}"
        report.append(new_line)
    report.append(f"Total expense  {total_expense:.2f}")
    report.append(f"Average expense  {total_expense / len(report[1:-1]):.2f}")

    return "\r\n".join(report)


def f(x):
    """Floating-point Approximation solution."""
    return x / ((1 + x) ** 0.5 + 1)


def mean(town: str, s: str):
    """Rainfall mean function solution."""
    records = s.splitlines()
    rainfall_data = []

    for record in records:
        parsed_town, record_info = record.split(":")
        if parsed_town == town:
            for month_record in record_info.split(","):
                rainfall_value = float(month_record.split(" ")[1])
                rainfall_data.append(rainfall_value)

    if not rainfall_data:
        return -1

    return sum(rainfall_data) / len(rainfall_data)


def variance(town, s):
    """Rainfall variance function solution."""
    records = s.splitlines()
    rainfall_data = []

    for record in records:
        parsed_town, record_info = record.split(":")
        if parsed_town == town:
            for month_record in record_info.split(","):
                rainfall_value = float(month_record.split(" ")[1])
                rainfall_data.append(rainfall_value)

    if not rainfall_data:
        return -1

    avg = sum(rainfall_data) / len(rainfall_data)
    return sum((month_rainfall - avg) ** 2 for month_rainfall in rainfall_data) / len(rainfall_data)


def nba_cup(result_sheet: str, to_find: str):
    """Rank NBA teams solution."""
    if not to_find:
        return ""

    nb_wins = 0
    nb_draws = 0
    nb_losses = 0
    scored = 0
    conceded = 0
    points = 0
    found = False

    records = result_sheet.split(",")
    pattern = re.compile(r"^(.*?) (\d+\.?\d*) (.*?) (\d+\.?\d*)$")

    for record in records:
        match = pattern.match(record)
        if match:
            team_1, score_1, team_2, score_2 = match.groups()
            if float(score_1) % 1 == 0 and float(score_2) % 1 == 0:
                if to_find == team_1:
                    our_score, opp_score = int(score_1), int(score_2)
                elif to_find == team_2:
                    our_score, opp_score = int(score_2), int(score_1)
                else:
                    continue

                found = True

                if our_score > opp_score:
                    nb_wins += 1
                    points += 3
                elif our_score == opp_score:
                    nb_draws += 1
                    points += 1
                else:
                    nb_losses += 1

                scored += our_score
                conceded += opp_score

            else:
                return f"Error(float number):{record}"

    if not found:
        return f"{to_find}:This team didn't play!"

    return f"{to_find}:W={nb_wins};D={nb_draws};L={nb_losses};Scored={scored};Conceded={conceded};Points={points}"


def stock_list(stocklist: list[str], categories: list[str]):
    """Help the bookseller! solution."""
    if not stocklist:
        return ""

    res = {}
    for code in stocklist:
        res[code[0]] = res.get(code[0], 0) + int(code.split(" ")[1])

    return " - ".join([f"({cat} : {res[cat]})" if cat in res else f"({cat} : 0)" for cat in categories])
