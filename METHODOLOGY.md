# Methodology

How the numbers in this repo were computed. Everything is reproducible
with `scripts/crunch_areas.py` + the DVSA open microdata.

## Source

DVSA anonymised MOT test results, full-year 2024, monthly CSVs from the
official S3 bucket:
`edh-dvsa-data-gov-uk-files-prod.s3.eu-west-1.amazonaws.com`
(files `test_result_2024-01.csv` … `test_result_2024-12.csv`).

## Filters (per test record)

- `test_type == "NT"` — normal tests only (no retests, no partial retests)
- `test_class_id == "4"` — cars and small vans (the standard consumer MOT)
- `test_result` in `{"P", "F", "PRS"}` — pass, fail, pass-after-rectification-at-station

Records: **45,573,249** after filtering.

## Definitions

- **Outright fail rate** = `F ÷ (P + F + PRS) × 100`. The headline metric.
  National: **20.69%**.
- **Initial fail rate** = `(F + PRS) ÷ (P + F + PRS) × 100` — cars that
  arrived with a failure-level defect, even if fixed at the station.
  National: **25.93%**.
- **PRS quirk:** some areas (notably London) show unusually high
  pass-after-rectification shares — e.g. East London 10.7% PRS vs
  Dundee 2.7%. We report both rates so readers can see it.

## Geography

Grouped by `postcode_area` (the outward-code area, e.g. KY, E, TR).
116 areas. Town names mapped manually from the area codes.

## CSV quirks handled

The monthly files contain embedded header rows and quoted multi-line
rows — the script reads with `dtype=str` and drops rows where
`test_id == "test_id"`.

## What this is NOT

- Not first-attempt rates (PRS is reported separately, not folded in silently).
- Not comparable to studies using different cuts (e.g. 2025 partial-year or
  all-classes data) — see the article for how this differs from the
  CarCostCheck/Zego cuts.
