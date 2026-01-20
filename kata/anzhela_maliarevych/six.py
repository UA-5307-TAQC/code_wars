"""6kyu tasks."""

import re
from math import sqrt


def find_nb(m):
    """Build a pile of Cubes."""
    n = 0
    total = 0

    while total < m:
        n += 1
        total += n ** 3

    if total == m:
        return n
    else:
        return -1


def balance(book):
    """Easy Balance Checking."""

    clean = re.sub(r"[^a-zA-Z0-9.\n ]", "", book)
    lines = [line for line in clean.split("\n") if line.strip()]

    original_balance = float(lines[0])
    balance = original_balance

    result = []
    result.append(f"Original Balance: {original_balance:.2f}")

    total_expense = 0
    count = 0

    for line in lines[1:]:
        parts = line.split()
        check = parts[0]
        category = parts[1]
        amount = float(parts[2])

        balance -= amount
        total_expense += amount
        count += 1

        result.append(
            f"{check} {category} {amount:.2f} Balance {balance:.2f}"
        )

    average = total_expense / count if count else 0

    result.append(f"Total expense  {total_expense:.2f}")
    result.append(f"Average expense  {average:.2f}")

    return "\r\n".join(result)


def f(x):
    """Floating-point Approximation (I)."""
    return x / (sqrt(1 + x) + 1)


def mean(town, s):
    """Rainfall"""
    lines = s.splitlines()
    for line in lines:
        if line.startswith(town + ":"):
            data = line.split(":")[1].split(",")
            values = []
            for item in data:
                values.append(float(item.split()[1]))
            return sum(values) / len(values)
    return -1


def variance(town, s):
    lines = s.splitlines()
    for line in lines:
        if line.startswith(town + ":"):
            data = line.split(":")[1].split(",")
            values = []
            for item in data:
                values.append(float(item.split()[1]))

            m = sum(values) / len(values)
            var = 0
            for x in values:
                var += (x - m) ** 2
            return var / len(values)
    return -1


def nba_cup(result_sheet, to_find):
    """Rank NBA teams."""
    if to_find == "":
        return ""

    split_line = result_sheet.split(",")

    wins = draws = losses = 0
    scored = conceded = points = 0
    played = False

    pattern = r'^(.+?) (\d+(?:\.\d+)?) (.+?) (\d+(?:\.\d+)?)$'

    for game in split_line:
        game = game.strip()

        match = re.match(pattern, game)
        if not match:
            continue

        team_1, score_1, team_2, score_2 = match.groups()

        if "." in score_1 or "." in score_2:
            return f"Error(float number):{game}"

        score_1 = int(score_1)
        score_2 = int(score_2)

        if to_find == team_1 or to_find == team_2:
            played = True
            if to_find == team_1:
                my_score, opp_score = score_1, score_2
            else:
                my_score, opp_score = score_2, score_1

            scored += my_score
            conceded += opp_score

            if my_score > opp_score:
                wins += 1
                points += 3
            elif my_score == opp_score:
                draws += 1
                points += 1
            else:
                losses += 1

    if not played:
        return f"{to_find}:This team didn't play!"

    return (
        f"{to_find}:W={wins};D={draws};L={losses};"
        f"Scored={scored};Conceded={conceded};Points={points}"
    )


def stock_list(stocklist, categories):
    """Help the bookseller."""
    if not stocklist or not categories:
        return ""
    
    result = []
    
    for cat in categories:
        total = 0
        
        for book in stocklist:
            code, count  = book.split()
            if code[0] == cat:
                total += int(count )
        
        result.append(f"({cat} : {total})")
    
    return " - ".join(result)