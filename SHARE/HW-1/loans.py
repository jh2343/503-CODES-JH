# IMPORT
import pandas as pd

# READ
df = pd.read_csv("data/loans.csv")
print("START\n", df)

# RENAME id
df = df.rename(columns={"id": "loan_id"})

# MELT
df = pd.melt(df, id_vars=df.columns[0:5])
# print(df)

# REMOVE ROWS WITH '-' AND THEN GROUP X COLUMN
df = df[df["value"] == "X"]
df = df.drop(["value"], axis=1)

# SPLIT 24_A --> 24 A
df["loan_term"] = df.variable.str[0:2]
df["letter"] = df.variable.str[3]
df = df.drop("variable", axis=1)

# CONVERT LETTER INTO default and expired
df["loan_status"] = df["letter"].apply(
    lambda x: "expired" if ((x == "A") | (x == "B")) else "current"
)
df["loan_default"] = df["letter"].apply(
    lambda x: True if ((x == "B") | (x == "D")) else False
)
df = df.drop("letter", axis=1)

# RENAME
df = df.rename(columns={"payments": "loan_payments"})
df = df.rename(columns={"amount": "loan_amount"})

# SAVE
df.to_csv("loans_py.csv", index=False)  # , sep='\t')
print("END\n", df)


# loan_amount: The amount of the loan if there is one, NA if none
# loan_payments: The amount of the loan payment if there is one, NA if none
# loan_term: The duration of loan in months, NA if none
# loan_status: The status of the loan (current or expired), NA if none
# loan_default: T/F if the loan is in default, or NA if none
