"""6kyu tasks."""

import re


def find_nb(m):
    """Build a pile of Cubes."""
    n = 0
    vol = 0

    while vol < m:
        n += 1
        vol += n**3

    if vol == m:
        return n
    return -1


def balance(book):
    """Easy Balance Checking."""
    lines = book.splitlines()

    clean = []
    for line in lines:
        if line.strip():
            cleared = re.sub(r"[^a-zA-Z0-9. ]", "", line)
            clean.append(cleared)

    curr_balance = float(clean[0])
    result = [f"Original Balance: {curr_balance:.2f}"]

    total = 0.0
    count = 0

    for i in clean[1:]:
        parts = i.split()
        check = parts[0]
        category = parts[1]
        amount = float(re.sub(r"[^0-9.]", "", parts[2]))

        curr_balance -= amount
        total += amount
        count += 1

        result.append(f"{check} {category} {amount:.2f} Balance {curr_balance:.2f}")

    average = total / count
    result.append(f"Total expense  {total:.2f}")
    result.append(f"Average expense  {average:.2f}")

    return "\r\n".join(result)


def f(x):
    """Floating-point Approximation (I)."""
    return x / ((1 + x) ** 0.5 + 1)


def mean(town, s):
    """Rainfall."""
    line = None
    for i in s.splitlines():
        if i.startswith(town + ":"):
            line = i
            break
    if line is None:
        return -1

    rains = []
    for i in line.split(","):
        _, value = i.split()
        rains.append(float(value))

    return sum(rains) / len(rains)


def variance(town, s):
    """Rainfall."""
    line = None
    for i in s.splitlines():
        if i.startswith(town + ":"):
            line = i
            break
    if line is None:
        return -1

    rains = []
    for i in line.split(","):
        _, value = i.split()
        rains.append(float(value))

    m = sum(rains) / len(rains)

    var_total = 0
    for r in rains:
        var_total += (r - m) ** 2
    return var_total / len(rains)


# pylint: disable=too-many-locals, too-many-branches
def nba_cup(result_sheet, to_find):
    """Ranking NBA teams."""
    if not to_find:
        return ""

    matches = result_sheet.split(",")

    wins = losses = draws = 0
    scored = conceded = points = 0
    played = False

    for m in matches:
        m = m.strip()

        parts = m.split()

        scores = []
        for p in parts:
            if p.replace(".", "", 1).isdigit():
                if "." in p:
                    return f"Error(float number):{m}"
                scores.append(p)

        if len(scores) != 2:
            continue
        s1 = scores[0]
        s2 = scores[1]

        i1 = parts.index(str(s1))
        i2 = parts.index(str(s2))

        t1 = " ".join(parts[:i1])
        t2 = " ".join(parts[i1 + 1 : i2])

        if to_find == t1:
            host = int(s1)
            opp = int(s2)
        elif to_find == t2:
            host = int(s2)
            opp = int(s1)
        else:
            continue

        scored += host
        conceded += opp

        if host > opp:
            wins += 1
            points += 3
        elif host == opp:
            draws += 1
            points += 1
        elif host < opp:
            losses += 1

        played = True

    if not played:
        return f"{to_find}:This team didn't play!"

    return f"{to_find}:W={wins};D={draws};L={losses};Scored={scored};" f"Conceded={conceded};Points={points}"


def stock_list(books, categories):
    """Help the bookseller."""
    if not books or not categories:
        return ""

    result = []

    for cat in categories:
        total = 0
        for item in books:
            code, num = item.split()
            if code[0] == cat:
                total += int(num)
        result.append(f"({cat} : {total})")

    return " - ".join(result)
