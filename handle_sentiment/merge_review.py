import pandas as pd


df_erigo = pd.read_csv("./dataset/reviews_erigo.csv")
df_robot = pd.read_csv("./dataset/reviews_robot.csv")
df_sandisk = pd.read_csv("./dataset/reviews_sandisk.csv")
df_teamgroup = pd.read_csv("./dataset/reviews_teamgroup.csv")
df_gm = pd.read_csv("./dataset/reviews_gm.csv")
df_rinnai = pd.read_csv("./dataset/reviews_rinnai.csv")
df_xiaomi = pd.read_csv("./dataset/reviews_xiaomi.csv")
df_bardi = pd.read_csv("./dataset/reviews_bardi.csv")


merged_df = pd.concat(
    [
        df_erigo,
        df_robot,
        df_sandisk,
        df_teamgroup,
        df_gm,
        df_rinnai,
        df_xiaomi,
        df_bardi,
    ]
)

merged_df.to_csv("./dataset/reviews_.csv", index=False)

print(merged_df["sentiment"].value_counts())

print("Data ulasan sudah digabung")
