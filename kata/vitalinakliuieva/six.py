"""Solutions for Codewars kata (6 kyu)."""

import math
import re

from core import kata  # pylint: disable=import-error


@kata("Build a pile of Cubes")
def find_nb(m):
    """Build a pile of Cubes exercise"""
    n = 0
    total = 0

    while total < m:
        n += 1
        total += n**3

    return n if total == m else -1


@kata("Easy Balance Checking")
def balance(book):
    """Easy Balance Checking exercise"""
    lines = book.splitlines()
    lines = [re.sub(r"[^a-zA-Z0-9. ]+", "", line) for line in lines if line.strip()]

    balance_num = float(lines[0])
    report_lines = [f"Original Balance: {balance_num:.2f}"]

    total_expense = 0.0
    count_expense = 0

    for line in lines[1:]:
        parts = line.split()
        check_num = parts[0]
        category = " ".join(parts[1:-1])
        amount = float(parts[-1])

        balance_num -= amount
        total_expense += amount
        count_expense += 1

        report_lines.append(f"{check_num} {category} {amount:.2f} Balance {balance_num:.2f}")

    average_expense = total_expense / count_expense if count_expense else 0
    report_lines.append(f"Total expense  {total_expense:.2f}")
    report_lines.append(f"Average expense  {average_expense:.2f}")

    return "\r\n".join(report_lines)


@kata("Floating-point Approximation (I)")
def f(x):
    """Floating-point Approximation  exercise"""
    return x / (math.sqrt(1 + x) + 1)


@kata("Rainfall")
def mean(town, s):
    """Rainfall exercise"""
    values = get_values(town, s)
    if values is None:
        return -1
    return sum(values) / len(values)


@kata("Rainfall")
def variance(town, s):
    """Rainfall exercise"""
    values = get_values(town, s)
    if values is None:
        return -1

    avg = sum(values) / len(values)
    return sum((x - avg) ** 2 for x in values) / len(values)


def get_values(town, s):
    """Get values for Rainfall exercise"""
    for line in s.split("\n"):
        if line.startswith(town + ":"):
            data = line.split(":")[1]
            return [float(x.split()[1]) for x in data.split(",")]
    return None


@kata("Ranking NBA teams")
def nba_cup(result_sheet, to_find):  # pylint: disable=R0914, R0912
    """Ranking NBA teams exercise"""
    if not to_find:
        return ""

    wins = draws = losses = scored = conceded = points = 0
    found = False

    for game in result_sheet.split(","):
        game = game.strip()
        if not game:
            continue

        parts = game.split()

        for p in parts:
            if "." in p:
                try:
                    if not p.isdigit():
                        return f"Error(float number):{game}"
                except ValueError:
                    pass

        score_indexes = [i for i, p in enumerate(parts) if p.isdigit()]
        if len(score_indexes) != 2:
            continue

        i1, i2 = score_indexes
        score1, score2 = int(parts[i1]), int(parts[i2])

        team1 = " ".join(parts[:i1])
        team2 = " ".join(parts[i1 + 1 : i2])

        if to_find not in (team1, team2):
            continue

        found = True

        if to_find == team1:
            scored += score1
            conceded += score2
            if score1 > score2:
                wins += 1
                points += 3
            elif score1 == score2:
                draws += 1
                points += 1
            else:
                losses += 1
        else:
            scored += score2
            conceded += score1
            if score2 > score1:
                wins += 1
                points += 3
            elif score1 == score2:
                draws += 1
                points += 1
            else:
                losses += 1

    if not found:
        return f"{to_find}:This team didn't play!"

    return f"{to_find}:W={wins};D={draws};L={losses};" f"Scored={scored};Conceded={conceded};Points={points}"


@kata("Help the bookseller !")
def stock_list(stocklist, categories):
    """Help the bookseller ! exercise"""
    total = 0
    result = []
    if not stocklist:
        return ""
    for category in categories:
        for book in stocklist:
            if re.search(category, book[0]):
                num = book.split(" ")[1]
                total += int(num)
        result.append(f"({category} : {total})")
        total = 0
    result = " - ".join(result)

    return result
