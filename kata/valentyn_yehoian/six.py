"""Task from codewars 6kyu tasks with parsers"""

import math
import re

from core import kata  # pylint: disable=import-error

MATCH_PATTERN = re.compile(r"^(.+?)\s+([\d\.]+)\s+(.+?)\s+([\d\.]+)$")


@kata("Build a pile of Cubes")
def find_nb(m):
    """Finds the integer"""
    i = 0
    current_sum = 0
    while current_sum < m:
        i += 1
        current_sum += i**3
        if current_sum == m:
            return i
    return -1


@kata("Easy Balance Checking")
def balance(book):
    """Cleans the checkbook string,returns a formatted report with expenses."""
    chars_to_remove = ",;:!=?{}"
    for char in chars_to_remove:
        book = book.replace(char, "")

    lines = [line.strip() for line in book.split("\n") if line.strip()]

    if not lines:
        return ""

    original_balance = float(lines[0])
    current_balance = original_balance
    total_expense = 0
    item_count = 0

    result_lines = []
    result_lines.append(f"Original Balance: {original_balance:.2f}")

    for line in lines[1:]:
        parts = line.split()
        price = float(parts[-1])
        item_info = " ".join(parts[:-1])

        current_balance -= price
        total_expense += price
        item_count += 1

        result_lines.append(f"{item_info} {price:.2f} Balance {current_balance:.2f}")

    result_lines.append(f"Total expense  {total_expense:.2f}")
    result_lines.append(f"Average expense  {total_expense / item_count:.2f}")

    return "\r\n".join(result_lines)


@kata("Floating-point Approximation (I)")
def f(x):
    """Calculates the function value."""
    return x / (math.sqrt(1 + x) + 1)


def get_town_data(town, s):
    """
    Helper function: Extracts rainfall data for a specific town
    from the raw string data.
    """
    search_key = town + ":"
    start_index = s.find(search_key)

    if start_index == -1:
        return None

    end_index = s.find("\n", start_index)
    if end_index == -1:
        end_index = len(s)

    raw_line = s[start_index:end_index]
    numbers_str = raw_line.split(":")[1]

    values = []
    for item in numbers_str.split(","):
        number = float(item.split()[1])
        values.append(number)

    return values


@kata("Rainfall")
def mean(town, s):
    """Calculates the average rainfall for a given town."""
    values = get_town_data(town, s)

    if values is None:
        return -1

    return sum(values) / len(values)


@kata("Rainfall")
def variance(town, s):
    """Calculates the variance of rainfall for a given town."""
    values = get_town_data(town, s)

    if values is None:
        return -1.0

    mean_val = sum(values) / len(values)
    return sum((x - mean_val) ** 2 for x in values) / len(values)


def update_stats(stats, own, opp):
    """Updates the statistics dictionary based on the match score."""
    stats["Scored"] += own
    stats["Conceded"] += opp

    if own > opp:
        stats["W"] += 1
        stats["Points"] += 3
    elif own == opp:
        stats["D"] += 1
        stats["Points"] += 1
    else:
        stats["L"] += 1


@kata("Ranking NBA teams")
def nba_cup(result_sheet, to_find):
    """Parses NBA match results using Regex."""
    if to_find == "":
        return ""

    matches = result_sheet.split(",")
    stats = {"W": 0, "D": 0, "L": 0, "Scored": 0, "Conceded": 0, "Points": 0}
    team_played = False

    for match in matches:
        match = match.strip()
        if not match or to_find not in match:
            continue

        match_data = MATCH_PATTERN.match(match)
        if not match_data:
            continue

        t1_name, s1_str, t2_name, s2_str = match_data.groups()

        if "." in s1_str or "." in s2_str:
            return f"Error(float number):{match}"

        try:
            if t1_name == to_find:
                own, opp = int(s1_str), int(s2_str)
            elif t2_name == to_find:
                own, opp = int(s2_str), int(s1_str)
            else:
                continue
        except ValueError:
            return f"Error(float number):{match}"

        team_played = True
        update_stats(stats, own, opp)

    if not team_played:
        return f"{to_find}:This team didn't play!"

    return (
        f"{to_find}:W={stats['W']};D={stats['D']};L={stats['L']};"
        f"Scored={stats['Scored']};Conceded={stats['Conceded']};Points={stats['Points']}"
    )


@kata("Help the bookseller !")
def stock_list(stocklist, categories):
    """Summarizes the total quantity of books for each category code provided."""
    if not stocklist or not categories:
        return ""

    counts = {category: 0 for category in categories}

    for item in stocklist:
        code, quantity = item.split()
        category_char = code[0]
        qty_value = int(quantity)

        if category_char in counts:
            counts[category_char] += qty_value

    result_parts = []
    for cat in categories:
        total = counts[cat]
        result_parts.append(f"({cat} : {total})")

    return " - ".join(result_parts)
