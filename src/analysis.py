import pandas as pd
from pathlib import Path

# Project folder location
BASE_DIR = Path(__file__).resolve().parent.parent

# Load dataset
file_path = BASE_DIR / "data" / "raw" / "Unemployment in India.csv"

df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Remove completely empty rows
df.dropna(how="all", inplace=True)

# Convert date
df["Date"] = pd.to_datetime(
    df["Date"], dayfirst=True, errors="coerce"
)

# Convert unemployment rate to numeric
df["Estimated Unemployment Rate (%)"] = pd.to_numeric(
    df["Estimated Unemployment Rate (%)"],
    errors="coerce"
)

# Calculate average unemployment
average = df["Estimated Unemployment Rate (%)"].mean()

print("UNEMPLOYMENT ANALYSIS")
print("---------------------")
print("Total Records:", len(df))
print("Average Unemployment Rate:", round(average, 2), "%")

# Save cleaned dataset
output_path = BASE_DIR / "data" / "processed"
output_path.mkdir(parents=True, exist_ok=True)

df.to_csv(
    output_path / "cleaned_unemployment_data.csv",
    index=False
)

print("Analysis completed successfully!")
