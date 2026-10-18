
def format_data(df):
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "").astype(float)

    df["number_of_open_complaints"] = df["number_of_open_complaints"].str.split("/").str[1].astype("Int64")

    return df

def clean_nulls(df):
    df["customer"] = df["customer"].fillna("Unknown")
    df["state"] = df["state"].fillna(df["state"].mode()[0])
    df["gender"] = df["gender"].fillna(df["gender"].mode()[0])
    df["education"] = df["education"].fillna(df["education"].mode()[0])
    df["customer_lifetime_value"] = df["customer_lifetime_value"].fillna(df["customer_lifetime_value"].median())
    df["income"] = df["income"].fillna(df["income"].median())
    df["monthly_premium_auto"] = df["monthly_premium_auto"].fillna(df["monthly_premium_auto"].median())
    df["number_of_open_complaints"] = df["number_of_open_complaints"].fillna(df["number_of_open_complaints"].mode()[0])
    df["policy_type"] = df["policy_type"].fillna(df["policy_type"].mode()[0])
    df["vehicle_class"] = df["vehicle_class"].fillna(df["vehicle_class"].mode()[0])
    df["total_claim_amount"] = df["total_claim_amount"].fillna(df["total_claim_amount"].median())

    return df

def clean_duplicates(df):
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    return df

def format_integers(df):
    df["customer_lifetime_value"] = df["customer_lifetime_value"].astype(int)
    df["income"] = df["income"].astype(int)
    df["monthly_premium_auto"] = df["monthly_premium_auto"].astype(int)
    df["total_claim_amount"] = df["total_claim_amount"].astype(int)

    return df

def main():
    import pandas as pd

    df = pd.read_csv("https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv")

    df = df.rename(columns={
        "Customer": "customer",
        "ST": "state",
        "GENDER": "gender",
        "Education": "education",
        "Customer Lifetime Value": "customer_lifetime_value",
        "Income": "income",
        "Monthly Premium Auto": "monthly_premium_auto",
        "Number of Open Complaints": "number_of_open_complaints",
        "Policy Type": "policy_type",
        "Vehicle Class": "vehicle_class",
        "Total Claim Amount": "total_claim_amount"
    })

    df = format_data(df)
    df = clean_nulls(df)
    df = format_integers(df)
    df = clean_duplicates(df)

    return df
