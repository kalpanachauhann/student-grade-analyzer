import numpy as np
import pandas as pd
import os


#  LOAD DATA

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "students.csv"))

# Clean column names — removes any hidden spaces
df.columns = [col.strip() for col in df.columns]

# Clean string values
df["Name"] = df["Name"].str.strip()

subjects = ["Math", "Science", "English", "History", "Computer"]


#  CALCULATE TOTAL AND AVERAGE

df["Total"]   = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1).round(2)


#  ASSIGN GRADE

def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

df["Grade"]  = df["Average"].apply(assign_grade)
df["Status"] = df["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")


#  DISPLAY FULL REPORT

print("=" * 65)
print("          STUDENT GRADE ANALYSIS REPORT")
print("=" * 65)
print(df[["Name", "Total", "Average", "Grade", "Status"]].to_string(index=False))


#  CLASS STATISTICS (NumPy)

averages = df["Average"].values

print("\n" + "=" * 65)
print("                  CLASS STATISTICS")
print("=" * 65)
print(f"  Class Average     : {np.mean(averages):.2f}")
print(f"  Highest Average   : {np.max(averages)}")
print(f"  Lowest Average    : {np.min(averages)}")
print(f"  Standard Deviation: {np.std(averages):.2f}")


#  TOP 3 STUDENTS

top3 = df.nlargest(3, "Average")[["Name", "Average", "Grade"]]
print("\n" + "=" * 65)
print("                  TOP 3 STUDENTS")
print("=" * 65)
print(top3.to_string(index=False))


#  FAILED STUDENTS

failed = df[df["Status"] == "Fail"][["Name", "Average", "Grade"]]
print("\n" + "=" * 65)
print("                  FAILED STUDENTS")
print("=" * 65)
if failed.empty:
    print("  No students failed.")
else:
    print(failed.to_string(index=False))


#  SUBJECT-WISE AVERAGE (NumPy)

print("\n" + "=" * 65)
print("               SUBJECT-WISE AVERAGE")
print("=" * 65)
for subject in subjects:
    subject_avg = np.mean(df[subject].values)
    print(f"  {subject:<12}: {subject_avg:.2f}")


#  EXPORT REPORT

output_path = os.path.join(os.path.dirname(__file__), "data", "report.csv")
df.to_csv(output_path, index=False)
print("\n" + "=" * 65)
print("  Report saved to data/report.csv")
print("=" * 65)