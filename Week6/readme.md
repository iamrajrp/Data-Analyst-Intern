# 📝 Data Ingestion and Processing Summary

### Note
The full cleaned `.gz` output file (~389 MB) exceeds GitHub's file upload limit.
A smaller 100k-row sample (`sample_100k_cleaned.gz`) is included here for reference.

## 📂 Dataset Overview
- **Dataset Used**: NYC Yellow Taxi Trip Records (January–March 2019)
- **Original Format**: `.sqlite` files (monthly)
- **Combined CSV Size**: ~2.58 GB
- **Final Output Format**: `.gz` compressed, pipe-separated (`|`) text file

---

## ⚙️ File Reading Benchmarks

| Method   | Time Taken | Notes                          |
|----------|------------|--------------------------------|
| **Pandas** | 176 seconds | Full in-memory load           |
| **Dask**   | 9.5 seconds | Lazy-loaded, memory-efficient |
| **Modin**  | Skipped     | Ray issue on Windows (Jupyter) |

> ✅ Conclusion: Dask was significantly faster and more efficient for large file loading.

---

## 🧹 Data Cleaning

- Removed leading/trailing whitespace from column names
- Removed special characters using regex
- Ensured column names were YAML-safe and consistent

---

## 🧾 Schema Validation

- Created a `schema.yaml` file containing:
  - The column names
  - The separator used in the CSV file
- Loaded and validated against the cleaned data
- ✅ Column names and count matched the schema

```yaml
separator: ','
columns:
  - vendorid
  - tpep_pickup_datetime
  - tpep_dropoff_datetime
  - passenger_count
  - trip_distance
  - ratecodeid
  - store_and_fwd_flag
  - pulocationid
  - dolocationid
  - payment_type
  - fare_amount
  - extra
  - mta_tax
  - tip_amount
  - tolls_amount
  - improvement_surcharge
  - total_amount
  - congestion_surcharge
