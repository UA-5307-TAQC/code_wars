"""Solutions for 6 kyu tasks."""

import math
import re


def find_nb(m):
    """Build a pile of Cubes."""
    current_volume = 0
    n = 0

    while current_volume < m:
        n += 1
        current_volume += n**3

    if current_volume == m:
        return n
    return -1


def balance(book):
    """Easy Balance Checking."""
    clean_string = re.sub(r"[^a-zA-Z0-9.\n]", " ", book)
    lines = [line.strip() for line in clean_string.split("\n") if line.strip()]
    original_balance = float(lines[0])
    current_balance = original_balance
    total_expense = 0
    result = [f"Original Balance: {original_balance:.2f}"]

    for line in lines[1:]:
        parts = line.split()
        price = float(parts[-1])
        item_name = " ".join(parts[1:-1])
        item_id = parts[0]
        current_balance -= price
        total_expense += price
        result.append(f"{item_id} {item_name} {price:.2f} Balance {current_balance:.2f}")

    result.append(f"Total expense  {total_expense:.2f}")
    transaction_count = len(lines) - 1
    average = total_expense / transaction_count
    result.append(f"Average expense  {average:.2f}")
    return "\r\n".join(result)


def f(x):
    """Floating-point Approximation."""
    res = x / (math.sqrt(1 + x) + 1)
    return res


def get_rainfall_data(town, strng):
    """Parses the input string."""
    for line in strng.splitlines():
        if line.startswith(town + ":"):
            numbers = re.findall(r"\d*\.\d+|\d+", line)
            return [float(x) for x in numbers]
    return None


def mean(town, strng):
    """Calculates the average (mean)."""
    records = get_rainfall_data(town, strng)

    if not records:
        return -1.0

    return sum(records) / len(records)


def variance(town, strng):
    """Calculates the variance."""
    records = get_rainfall_data(town, strng)

    if not records:
        return -1.0

    avg = sum(records) / len(records)
    variance_sum = sum((x - avg) ** 2 for x in records)
    return variance_sum / len(records)


def nba_cup(result_sheet, to_find):
    """Ranking NBA teams."""
    if not to_find:
        return ""

    stats = {"W": 0, "D": 0, "L": 0, "Scored": 0, "Conceded": 0, "Points": 0, "Played": False}

    for match in result_sheet.split(","):
        if not match:
            continue

        pattern = re.match(r"^(.*?) (\d+(?:\.\d+)?) (.*?) (\d+(?:\.\d+)?)$", match)

        if not pattern:
            continue

        team_a, score_a_str, team_b, score_b_str = pattern.groups()

        if "." in score_a_str or "." in score_b_str:
            return f"Error(float number):{match}"

        if to_find == team_a:
            my_score, opp_score = int(score_a_str), int(score_b_str)
        elif to_find == team_b:
            my_score, opp_score = int(score_b_str), int(score_a_str)
        else:
            continue

        stats["Played"] = True
        stats["Scored"] += my_score
        stats["Conceded"] += opp_score

        if my_score > opp_score:
            stats["W"] += 1
            stats["Points"] += 3
        elif my_score == opp_score:
            stats["D"] += 1
            stats["Points"] += 1
        else:
            stats["L"] += 1

    if not stats["Played"]:
        return f"{to_find}:This team didn't play!"

    return (
        f"{to_find}:W={stats['W']};D={stats['D']};L={stats['L']};"
        f"Scored={stats['Scored']};Conceded={stats['Conceded']};Points={stats['Points']}"
    )


def stock_list(stocklist, categories):
    """Help the bookseller."""
    if not stocklist or not categories:
        return ""

    counts = {}

    for item in stocklist:
        code, quantity = item.split()
        category = code[0]
        amount = int(quantity)
        counts[category] = counts.get(category, 0) + amount
    result_parts = []

    for cat in categories:
        total = counts.get(cat, 0)
        result_parts.append(f"({cat} : {total})")
    return " - ".join(result_parts)
