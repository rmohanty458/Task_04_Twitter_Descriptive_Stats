import csv
import math
from collections import defaultdict, Counter
from statistics import mean, stdev

def is_numeric(value):
    try:
        float(value)
        return True
    except:
        return False

def summarize_column(values):
    numeric_values = [float(v) for v in values if is_numeric(v)]
    if numeric_values:
        count = len(numeric_values)
        avg = mean(numeric_values)
        minimum = min(numeric_values)
        maximum = max(numeric_values)
        std = stdev(numeric_values) if len(numeric_values) > 1 else 0
        return {"count": count, "mean": avg, "min": minimum, "max": maximum, "std": std}
    else:
        count = len(values)
        unique_counts = Counter(values)
        most_common = unique_counts.most_common(1)[0] if unique_counts else None
        return {"count": count, "unique": len(unique_counts), "most_common": most_common}

def summarize_dataset(file_path, group_by=None):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    print(f"Loaded {len(rows)} rows from {file_path}")

    # Group rows
    grouped = defaultdict(list)
    if group_by:
        for row in rows:
            key = tuple(row[g] for g in group_by)
            grouped[key].append(row)
    else:
        grouped[("all",)] = rows

    for group, group_rows in grouped.items():
        print(f"\nGroup: {group}")
        col_data = defaultdict(list)
        for row in group_rows:
            for col, val in row.items():
                if val.strip() != "":
                    col_data[col].append(val)

        for col, values in col_data.items():
            stats = summarize_column(values)
            print(f"Column: {col}")
            print(f"  Stats: {stats}")

if __name__ == "__main__":
    summarize_dataset("../data/2024_tw_posts_president_scored_anon.csv", group_by=["source"])
