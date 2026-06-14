# 🛡️ Data Quality Summary
### Phase 2 Deliverable · Customer Segmentation & CRM Intelligence Platform

> **Purpose:** Make every cleaning decision explicit, defensible, and business-tied. Every downstream metric (Phases 3–7) inherits the trust this document establishes.

---

## 1. Headline Numbers

| Dimension | Raw | Cleaned | Retention |
|---|---|---|---|
| Rows | 541,909 | **392,692** | **72.5%** |
| Revenue (GBP) | £9,747,748 | **£8,887,209** | **91.2%** |
| Customers | 4,372 | **4,338** | **99.2%** |
| Invoices | 25,900 | 22,190 | 85.7% |
| SKUs | 4,070 | 3,665 | 90.0% |
| Countries | 38 | 37 | 97.4% |

> **The headline that matters for a CMO:**
> *"We dropped 27% of rows but kept **99.2% of customers and 91% of revenue**. The activity we set aside is anonymous guest checkout and operational line items — none of which can power CRM segmentation anyway."*

---

## 2. Quality Issues Detected

| # | Issue | Rows Affected | Severity | Business Cause (likely) |
|---|---|---|---|---|
| Q1 | Missing `CustomerID` | 135,080 (24.93%) | 🔴 Critical | Guest checkouts, POS system gaps |
| Q2 | Cancellations (`InvoiceNo` starts with `C`) | 9,288 (1.71%) | 🟡 Material | Returns, customer-initiated cancels |
| Q3 | Negative `Quantity` | 10,624 (1.96%) | 🟡 Material | Almost entirely overlaps with cancellations |
| Q4 | Zero `UnitPrice` | 2,515 (0.46%) | 🟡 Material | Free samples, promo items, data-entry placeholders |
| Q5 | Negative `UnitPrice` | 2 | 🟢 Low | Accounting adjustments (`Adjust bad debt`) |
| Q6 | Missing `Description` | 1,454 (0.27%) | 🟢 Low | Co-occurs with operational stockcodes |
| Q7 | Exact duplicate rows | 5,268 (0.97%) | 🟢 Low | Double-scans / system replay |
| Q8 | Extreme `Quantity` outliers (±80,995) | <50 | 🟡 Material | **Real B2B-scale transactions** — keep |
| Q9 | Non-product `StockCode`s (POST, DOT, M, ...) | ~3,000 | 🟢 Low | Operational line items |

---

## 3. Cleaning Pipeline (executed)

```
Step 1: Drop cancellations          541,909 →  532,621   (–9,288)
Step 2: Drop missing CustomerID     532,621 →  399,260   (–133,361)
Step 3: Quantity > 0                399,260 →  397,924   (–1,336)   [residual returns]
Step 4: UnitPrice > 0               397,924 →  397,884   (–40)      [free samples / adjustments]
Step 5: Drop duplicates             397,884 →  392,692   (–5,192)
```

> *Step-by-step numbers are produced by the notebook so a reviewer can re-run end-to-end.*

---

## 4. What We Did NOT Drop (and Why)

| Signal | Why we kept it |
|---|---|
| **Extreme quantities (up to 80,995 units)** | These are real B2B-scale orders — direct evidence for Hypothesis H4. *Blanket outlier removal would erase the most valuable customers.* |
| **`POST`, `DOT`, `BANK CHARGES` line items** | Will be filtered *contextually* in Phase 6 (segmentation), not now. They may matter for total P&L analysis in Phase 3. |
| **The single value `"Unspecified"` in Country** | Surfaces as a distinct geographic segment — useful insight, not noise. |
| **December 2010 + December 2011 overlap** | Enables a year-over-year cohort comparison for Hypothesis H6. |

---

## 5. Known Limitations of the Cleaned Dataset

| Limitation | Phase Impact | Mitigation |
|---|---|---|
| **Single year of data** | Limits multi-year CLV; cohort analysis horizon is short | Disclose; treat CLV as a 12-month proxy |
| **No demographic data** | Cannot enrich segments with age/gender | Segment on behavior, not identity |
| **No marketing-channel attribution** | Cannot tie a purchase to a campaign | Out of scope (declared in Phase 1) |
| **B2B/B2C not labeled** | Must be *inferred* in Phase 6 | Use frequency + quantity thresholds |
| **Returns dropped, not analyzed separately** | Cannot diagnose return-driven churn | Reserved for v2 (future work) |

---

## 6. Reproducibility

| Artifact | Path |
|---|---|
| Notebook (executed) | `notebooks/01_data_understanding.ipynb` |
| Cleaned dataset (parquet) | `data/processed/online_retail_cleaned.parquet` |
| Inspection CSV sample | `data/processed/online_retail_cleaned_sample.csv` |
| Data dictionary | `reports/02_data_dictionary.md` |
| This document | `reports/data_quality_summary.md` |

Any reviewer can re-run `notebooks/01_data_understanding.ipynb` against `data/raw/Online_Retail.xlsx` and reproduce identical cleaned outputs.

---

## 7. Portfolio Translation (queued for Phase 8)

> **Resume bullet candidate:**
> *"Audited a 541K-row online-retail transaction dataset across 8 fields; designed and documented a 5-step cleaning pipeline that retained 99.2% of customers and 91% of revenue while removing 135K guest-checkout records, 9.3K cancellations, and 2.5K non-product operational line items — every exclusion tied to a documented business rule."*

> **Interview talking point:**
> *"My data-quality discipline isn't about chasing 100% data retention — it's about defending every drop. If a CMO asks why we excluded 27% of rows, I can answer in one sentence per step, in business language. That's how I keep the trust of downstream stakeholders."*

---

*Document version: 1.0 — Phase 2 baseline*
