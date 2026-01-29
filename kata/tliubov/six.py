"""6kyu level tasks."""

import re
from math import sqrt


def find_nb(m):
    """Build a pile of Cubes."""

    possible_volume = 0
    cube_count = 0
    while possible_volume < m:
        cube_count += 1
        possible_volume += cube_count**3
    return cube_count if possible_volume == m else -1


def balance(book):
    """Easy Balance Checking."""

    clean_lines, lines_arr, rows, result_str = "", [], [], ""
    total_expense = 0

    for ch in book:
        if ch.isalnum() or ch in (" ", ".", "\n"):
            clean_lines += ch

    lines_arr = [line for line in clean_lines.split("\n") if line]
    rows = [row.split() for row in lines_arr]
    current_balance = float(rows[0][0])
    result_str += f"Original Balance: {current_balance:.2f}\r\n"

    for i in range(1, len(rows)):
        check_number = rows[i][0]
        category = rows[i][1]
        check_amount = float(rows[i][2])
        remainder = round(current_balance - check_amount, 2)
        total_expense += check_amount
        current_balance -= check_amount
        result_str += f"{check_number} {category} {check_amount:.2f} Balance {remainder:.2f}\r\n"

    if total_expense:
        avg_expense = total_expense / (len(rows) - 1)
    else:
        avg_expense = 0

    result_str += f"Total expense  {total_expense:.2f}\r\n"
    result_str += f"Average expense  {avg_expense:.2f}"
    return result_str


def f(x):
    """Floating-point Approximation (I)."""

    approximation = x / (sqrt(x + 1) + 1)
    return approximation


def find_monthly_data(town, s):
    """Rainfall - find monthly data for town."""

    for line in s.split("\n"):
        if line.startswith(town):
            town_data = line.replace(f"{town}:", "").split(",")
            monthly_data = [month.split() for month in town_data]
            return monthly_data
    return []


def mean(town, s):
    """Rainfall - find mean of rainfall for the town."""

    monthly_data = find_monthly_data(town, s)
    if not monthly_data:
        return -1

    total_rainfall = 0
    for i in range(12):
        total_rainfall += float(monthly_data[i][1])
    return total_rainfall / 12


def variance(town, s):
    """Rainfall - find variance of rainfall for the town."""

    monthly_data = find_monthly_data(town, s)
    if not monthly_data:
        return -1

    town_mean = mean(town, s)
    deviation_sum = 0
    for i in range(12):
        deviation = (town_mean - float(monthly_data[i][1])) ** 2
        deviation_sum += deviation
    return deviation_sum / 12


def rainfall(town,s):
    """Rainfall - find variance and mean of rainfall."""

    return [mean(town, s), variance(town, s)]


def nba_cup(result_sheet, to_find):
    """Rank NBA teams."""

    if not to_find:
        return ""

    team_name = rf"\b{to_find}\b"
    is_found = False
    results = {"wins": 0, "draws": 0, "losses": 0, "scored": 0, "conceded": 0, "points": 0}

    for match in result_sheet.split(","):
        if not re.search(team_name, match):
            continue

        is_found = True

        if re.search(r"\d+\.\d+", match):
            return f"Error(float number):{match}"

        scores = [int(n) for n in re.findall(r"\b\d+\b", match)]
        parts = re.split(team_name, match)

        if re.match(r"\s+\d", parts[1]):
            team_score, opponent_score = scores[0], scores[1]
        else:
            team_score, opponent_score = scores[1], scores[0]

        results["scored"] += team_score
        results["conceded"] += opponent_score

        if team_score < opponent_score:
            results["losses"] += 1
        elif team_score > opponent_score:
            results["wins"] += 1
            results["points"] += 3
        else:
            results["draws"] += 1
            results["points"] += 1

    if not is_found:
        return f"{to_find}:This team didn't play!"

    return (
        f"{to_find}:W={results['wins']};D={results['draws']};L={results['losses']};Scored={results['scored']};"
        f"Conceded={results['conceded']};Points={results['points']}"
    )


def stock_list(stocklist, categories):
    """Help the bookseller."""

    if not (stocklist and categories):
        return ""

    books_total = {category: 0 for category in categories}
    for record in stocklist:
        code, quantity = record.split()
        category = code[0]
        quantity = int(quantity)
        if category in categories:
            books_total[category] += quantity

    result = []
    for category in books_total:
        result.append(f"({category} : {books_total[category]})")
    return " - ".join(result)
