- sütun df["sütun_ismi"]
- satır df.loc["satır_indexi"]
- mixed - df.loc["satır_indexi]["sütun_ismi"]
- filter - df[df["carat"].isnull()]
- satır döndürme (row - iteration)
for index, row in df.iterrows():
    # Satır döndürme
    pass
- sütun döndürme