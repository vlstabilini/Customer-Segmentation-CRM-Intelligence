# 📒 Data Dictionary — UCI Online Retail Dataset
### Phase 2 Deliverable · Customer Segmentation & CRM Intelligence Platform

**Source:** UCI Machine Learning Repository — Online Retail
**Period covered:** 2010-12-01 → 2011-12-09 (~13 months)
**Raw shape:** 541,909 rows × 8 columns
**Cleaned shape:** 392,692 rows × 9 columns (Revenue derived)
**Granularity:** One row = one product line item on one invoice

---

## 📋 Column Reference

### `InvoiceNo`
| Attribute | Value |
|---|---|
| **Type** | `object` (string) |
| **Unique values** | 25,900 |
| **Missing** | 0 |
| **Example** | `536365`, `C536379` |
| **Business meaning** | Order / transaction ID. Groups multiple product lines into a single shopping basket. |
| **⚠️ Gotcha** | Invoice IDs starting with **`C`** denote **cancellations / returns** (9,288 rows, 1.71%). These rows have negative `Quantity`. **Must be filtered for customer-value analysis.** |
| **CRM use** | Basket-level metrics (avg basket size, items per order, basket value). |

---

### `StockCode`
| Attribute | Value |
|---|---|
| **Type** | `object` (string) |
| **Unique values** | 4,070 |
| **Missing** | 0 |
| **Example** | `85123A`, `POST`, `BANK CHARGES` |
| **Business meaning** | Product SKU. |
| **⚠️ Gotcha** | A subset of codes are **non-product operational entries**: `POST` (shipping), `DOT` (dotcom postage), `M` (manual), `BANK CHARGES`, `AMAZONFEE`, `CRUK` (donations), `D` (discount), `S` (samples), `C2` (carriage). These should be excluded from product-mix analysis but may be relevant for full P&L. |
| **CRM use** | Product affinity by segment (Phase 6); cross-sell candidates. |

---

### `Description`
| Attribute | Value |
|---|---|
| **Type** | `object` (string) |
| **Unique values** | 4,223 |
| **Missing** | 1,454 (0.27%) |
| **Example** | `"WHITE HANGING HEART T-LIGHT HOLDER"` |
| **Business meaning** | Human-readable product name. |
| **⚠️ Gotcha** | Some descriptions are **operational notes**, not products: `"check"`, `"damages"`, `"lost"`, `"SAMPLES"`, `"AMAZON FEE"`. Most of these co-occur with the special StockCodes above. |
| **CRM use** | Product-category clustering, NLP-driven taxonomy in Phase 7 AI Agent. |

---

### `Quantity`
| Attribute | Value |
|---|---|
| **Type** | `int64` |
| **Range (raw)** | –80,995 → +80,995 |
| **Median** | 3 |
| **Missing** | 0 |
| **Business meaning** | Number of units of this SKU sold on this invoice line. |
| **⚠️ Gotcha** | **10,624 rows have negative Quantity** (returns/cancellations). Extreme values (±80,995) are **paired transactions** — a large B2B order followed by its cancellation. These are real business activity, *not* errors. |
| **CRM use** | Volume signal; B2B-vs-B2C discrimination (Hypothesis H4). |

---

### `InvoiceDate`
| Attribute | Value |
|---|---|
| **Type** | `datetime64[ns]` |
| **Range** | 2010-12-01 08:26 → 2011-12-09 12:50 |
| **Unique timestamps** | 23,260 |
| **Missing** | 0 |
| **Business meaning** | Timestamp of the transaction (down to the minute). |
| **⚠️ Gotcha** | The dataset has a **9-day overlap** (Dec 1 2010 / Dec 9 2011) — *useful for year-over-year December cohort comparison* (Hypothesis H6). |
| **CRM use** | **Critical** for Recency (RFM), purchase cadence, seasonality, cohort retention. |

---

### `UnitPrice`
| Attribute | Value |
|---|---|
| **Type** | `float64` |
| **Currency** | GBP (£) |
| **Range (raw)** | –£11,062.06 → £38,970.00 |
| **Median** | £2.08 |
| **Missing** | 0 |
| **Business meaning** | Price per unit at time of sale. |
| **⚠️ Gotcha** | **2,515 rows have UnitPrice = 0** (free samples, promo) and **2 rows have negative UnitPrice** (`Adjust bad debt` accounting entries). Drop for customer-value analysis. |
| **CRM use** | Revenue = Quantity × UnitPrice; basis for Monetary score in RFM. |

---

### `CustomerID`
| Attribute | Value |
|---|---|
| **Type** | `float64` (in raw); cast to `int` after cleaning |
| **Unique values** | 4,372 (4,338 after cleaning) |
| **Missing** | **135,080 rows (24.93%)** ← critical |
| **Example** | `17850` |
| **Business meaning** | The customer profile this transaction belongs to. |
| **🔴 Gotcha** | Nearly **25% of transactions have no CustomerID** — likely guest checkouts or POS gaps. They contribute **~£1.45M in raw revenue** but **cannot be assigned to a CRM profile**, so they are dropped from all customer-level analyses (Phases 4–7). |
| **CRM use** | **The most important field in the dataset.** Foundation of every customer-level metric. |

---

### `Country`
| Attribute | Value |
|---|---|
| **Type** | `object` (string) |
| **Unique values** | 38 |
| **Missing** | 0 |
| **Top value** | `United Kingdom` (91.4% of rows) |
| **Business meaning** | Customer's country of registration. |
| **⚠️ Gotcha** | Includes the value `"Unspecified"` — these will surface as a low-revenue "unknown geography" segment. |
| **CRM use** | Geographic segmentation; AOV comparison UK vs. International (Hypothesis H2). |

---

### `Revenue` *(derived in cleaned dataset)*
| Attribute | Value |
|---|---|
| **Type** | `float64` |
| **Formula** | `Quantity × UnitPrice` |
| **Business meaning** | Line-item revenue in GBP. |
| **CRM use** | Monetary (M) in RFM; CLV computation; revenue concentration analysis. |

---

## 🧭 Field Importance Map — for Phases 3 → 7

| Field | EDA (P3) | Customer Analytics (P4) | RFM (P5) | Segmentation (P6) | AI Agent (P7) |
|---|---|---|---|---|---|
| `InvoiceNo` | ★★★ | ★★★ | ★★★ | ★★ | ★ |
| `StockCode` | ★★ | ★ | – | ★★ | ★★ |
| `Description` | ★ | – | – | ★ | ★★★ (NLP context) |
| `Quantity` | ★★★ | ★★ | ★★ | ★★★ | ★★ |
| `InvoiceDate` | ★★★ | ★★★ | ★★★ (Recency) | ★★★ | ★★★ |
| `UnitPrice` | ★★ | ★★ | ★★ (Monetary) | ★★ | ★★ |
| `CustomerID` | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |
| `Country` | ★★★ | ★★ | ★ | ★★ | ★★ |
| `Revenue` (derived) | ★★★ | ★★★ | ★★★ | ★★★ | ★★★ |

---

## 🧹 Cleaning Decisions Summary

| # | Decision | Rows Removed | Justification |
|---|---|---|---|
| 1 | Drop cancellations (`InvoiceNo` starts with `C`) | 9,288 | These are not new business; they negate prior revenue. |
| 2 | Drop rows with missing `CustomerID` | 133,361 (after step 1) | Cannot be assigned to a CRM profile — out of scope for customer-level analysis. |
| 3 | Keep only `Quantity > 0` | 0 (already covered by step 1) | Positive sales only. |
| 4 | Keep only `UnitPrice > 0` | 40 (after prior steps) | Excludes free samples and bad-debt adjustments. |
| 5 | Drop exact duplicates | 5,225 (after prior steps) | Likely double-scans / system replays. |
| — | **Total dropped** | **148,917 (27.5%)** | **Result: 392,692 rows, 4,338 customers, £8.89M revenue retained.** |

---

## 📦 Output Files

| File | Path | Description |
|---|---|---|
| `online_retail_cleaned.parquet` | `data/processed/` | Cleaned dataset (392,692 rows × 9 cols) — input for Phases 3–7. |
| `online_retail_cleaned_sample.csv` | `data/processed/` | First 2,000 rows for quick inspection (GitHub-friendly). |

---

*Document version: 1.0 — Phase 2 baseline*
*Maintainer: Data Analyst track · CRM Intelligence Platform*
