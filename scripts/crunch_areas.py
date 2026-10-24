# NOTE: this is the exact script used for the CheckMyMOT 2024 analysis.
# BASE below pointed at a local copy of the DVSA open microdata; download the
# 2024 monthly CSVs (see README) and point BASE at them to reproduce.
# Source: https://edh-dvsa-data-gov-uk-files-prod.s3.eu-west-1.amazonaws.com/
import pandas as pd, glob, json, os

BASE = os.path.expanduser("~/workspace/checkmymot/mot-data/MOT testing data results (2024)")
files = sorted(glob.glob(os.path.join(BASE, "test_result_2024*.csv")))
agg = {}
for f in files:
    for chunk in pd.read_csv(f, usecols=["test_id","test_class_id","test_type","test_result","postcode_area"],
                             chunksize=400_000, dtype=str):
        chunk = chunk[chunk.test_id != "test_id"]
        c = chunk[(chunk.test_type == "NT") & (chunk.test_class_id == "4") &
                  (chunk.test_result.isin(["P","F","PRS"]))]
        if c.empty: continue
        g = c.groupby("postcode_area").test_result.value_counts().unstack(fill_value=0)
        for area, row in g.iterrows():
            e = agg.setdefault(area, [0,0,0])
            e[0] += int(row.get("P",0)) + int(row.get("F",0)) + int(row.get("PRS",0))
            e[1] += int(row.get("F",0)); e[2] += int(row.get("PRS",0))
    print("done", os.path.basename(f))

rows = []
for area,(n,f_,prs) in agg.items():
    rows.append({"area": area, "tests": n, "fail_F": f_, "prs": prs,
                 "fail_pct": round(100*f_/n,2), "initial_fail_pct": round(100*(f_+prs)/n,2)})
rows.sort(key=lambda r: -r["initial_fail_pct"])
json.dump(rows, open(os.path.expanduser("~/workspace/checkmymot/mot-data/areas.json"),"w"), indent=1)
big = [r for r in rows if r["tests"] >= 50000]
print("WORST (initial fail, >=50k tests):"); [print(r) for r in big[:12]]
print("BEST:"); [print(r) for r in big[-12:]]
