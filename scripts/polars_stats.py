import polars as pl

def summarize_with_polars(file_path, group_by=None):
    df = pl.read_csv(file_path)
    print("Basic describe():")
    print(df.describe())

    print("\nTop values per categorical column:")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            print(f"\nColumn: {col}")
            vc = df.group_by(col).agg(pl.count().alias("count")).sort("count", descending=True).head(5)
            print(vc)

    if group_by:
        grouped = df.group_by(group_by).agg([
            pl.len(),
            *[pl.col(c).mean().alias(f"{c}_mean") for c in df.columns if df[c].dtype in [pl.Int64, pl.Float64]]
        ])
        print("\nGrouped stats:")
        print(grouped)

if __name__ == "__main__":
    summarize_with_polars("../data/2024_tw_posts_president_scored_anon.csv", group_by="source")