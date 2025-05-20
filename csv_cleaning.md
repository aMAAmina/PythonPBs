## The problem covers csv handeling with python
You’re given a CSV file from a small clinic that tracks basic patient data. The file has issues due to inconsistent entries and missing information. Your goal is to clean the data and output a clean version of the CSV.

**Sample of clinic_patients.csv**
| patient_id | name        | age | visit_date  | diagnosis   |
|------------|-------------|-----|-------------|-------------|
| 1          | John Doe    | 28  | 2024-12-01  | Flu         |
| 2          |             | 35  | 2025-01-15  | Cold        |
| 3          | Alice Smith |     | 2025-01-17  |             |
| 4          | David Lee   | 41  |             | Allergy     |
| 5          |             |     |             |             |
| 6          | Mary Stone  | 29  | 2025-01-20  | Headache    |

## Tasks to complete
1. Generate the CSV file with Python from scratch.
2. Fill missing `name` fields with "Unknown".
3. Fill missing `age` fields with the average age (rounded down).
4. Fill missing `visit_date` fields with "Unknown".
5. Fill missing `diagnosis` fields with "Not Diagnosed".
6. Remove any fully empty rows (like row 5).
7. Sort the data by `visit_date` ascending. Put "Unknown" visit_dates at the end.
8. Export the clean version to cleaned_clinic_patients.csv.
9. Convert `visit_date` to datetime objects for proper sorting.
10. Validate that `age` is always an integer after cleaning.
11. Add a column `needs_followup` with `True` if diagnosis is "Not Diagnosed", else `False`
