import pandas as pd


def preprocess(df, region_df):

    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']

    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')

    # dropping duplicates
    df.drop_duplicates(inplace=True)

    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    return df

#     global df, region_df
#
#     # Filter for Summer Olympics
#     df_filtered = df[df['Season'] == 'Summer']
#
#     # Merge with region_df on 'NOC'
#     df_merged = df_filtered.merge(region_df, on='NOC', how='left')
#
#     # Drop duplicates
#     df_cleaned = df_merged.drop_duplicates()
#
#     # One-hot encode medals
#     df_final = pd.concat([df_cleaned, pd.get_dummies(df_cleaned['Medal'])], axis=1)
#
#     return df_final