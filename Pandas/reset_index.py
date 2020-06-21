df_sub = df[~((df['col1']>=value1)|(df['col2']<=value2))].copy()
df_sub.reset_index(drop=True)
