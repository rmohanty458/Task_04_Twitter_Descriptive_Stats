import pandas as pd

def summarize_with_pandas(file_path, group_by=None):
    df = pd.read_csv(file_path)

    print("Basic describe():")
    print(df.describe(include='all'))

    print("\nTop values per categorical column:")
    for col in df.select_dtypes(include=["object", "category"]).columns:
        print(f"\nColumn: {col}")
        print(df[col].value_counts().head(5))

    if group_by:
        grouped = df.groupby(group_by)
        print("\nGrouped stats:")
        print(grouped.describe())

if __name__ == "__main__":
    summarize_with_pandas("../data/2024_tw_posts_president_scored_anon.csv", group_by="source")