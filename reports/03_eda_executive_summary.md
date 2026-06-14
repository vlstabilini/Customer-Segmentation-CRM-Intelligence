# 📊 Phase 3 — EDA Executive Summary
### Customer Segmentation & CRM Intelligence Platform
**One-page read for a CMO / CRM Manager**

---

## 🎯 Bottom Line — Four Things to Know

1. **Revenue is dangerously concentrated.** Top 20% of customers (~870 people) drive **75% of revenue**. Gini coefficient = **0.72** (income-inequality-grade). A churn event in the top 1% is a multi-£10,000 revenue hit. **→ A VIP-tier program is non-optional.**

2. **International isn't a smaller UK — it's a different business.** UK = 82% revenue, mean AOV **£438**. International = 18% revenue but mean AOV **£850 (1.9× UK)** across only 1,886 invoices. **→ Two playbooks: UK = volume/retention; International = high-touch/account-style.**

3. **A B2B segment is hiding in a B2C dataset.** The top 50 customers average **41 orders each** (vs. median of 2 for the rest), drive **33% of total revenue**, and buy at 10am–3pm Tue–Thu (a work-hours pattern). **→ These need named account managers, not email blasts.**

4. **Q4 (Sep–Nov) is the revenue engine, but the gift-season cohort retention is untested.** Peak month = November 2011 (~1.7× a typical Q1 month). **→ A dedicated 30/60/90-day post-Christmas nurture playbook is needed before the natural January slump.**

---

## 📐 The Numbers

| Metric | Value |
|---|---|
| Customers | 4,338 |
| Invoices | 18,532 |
| Revenue | £8,887,209 |
| Period | Dec 2010 – Dec 2011 (~13 months) |
| Top 1% of customers' revenue share | **31.8%** |
| Top 20% of customers' revenue share | **74.7%** |
| Gini coefficient | **0.72** |
| UK revenue share | **82.0%** |
| Intl mean AOV vs UK mean AOV | **£850 vs £438 (1.9×)** |
| One-time buyers | **1,493 (34.4%)** |
| Median orders per customer | **2** |
| Top 50 customers' revenue share | **33.3%** |
| #1 customer revenue | **£280,206** |

---

## ✅ Hypothesis Verdicts (registered in Phase 1)

| # | Hypothesis | Verdict |
|---|---|---|
| H1 | Top 20% of customers drive ≥70% of revenue | ✅ **CONFIRMED** (75%) |
| H2 | International AOV > UK AOV | ✅ **CONFIRMED** (1.9×) |
| H4 | Hidden B2B segment inside B2C data | ✅ **CONFIRMED** (top 50 = 33% revenue, 41 orders/customer) |
| H6 | Q4 gift-season cohort behaves differently | 🟡 **Directional** — Q4 spike confirmed; retention test deferred to Phase 5 |
| H3 | 2nd-purchase-within-30-days → 3× LTV | ⏳ Phase 4 |
| H5 | Dormant-but-loyal recoverable via win-back | ⏳ Phase 5 |
| H7 | Returns concentrated in few customers | ⏳ Phase 5 / future work |

---

## 🎬 Three Marketing Recommendations (already actionable)

| # | Recommendation | Driven by | Expected impact |
|---|---|---|---|
| 1 | **Launch a 4-tier VIP program** (top 1% / top 5% / top 20% / rest) | H1 | Defends 75% of revenue base |
| 2 | **Split UK and International into separate CRM tracks** with different cadence and offer mix | H2 | Unlocks the higher AOV ceiling of international without diluting UK ROI |
| 3 | **Build a B2B account-management lane** for the top 50 accounts (named AM, reorder workflows, custom pricing tier) | H4 | Protects the 33% revenue concentration and uncaps account growth |

---

## 📁 Supporting Artifacts

- Full notebook: `notebooks/02_eda.ipynb`
- 7 hero charts: `images/chart1` … `chart7`
- Detailed PDF read-out: `reports/03_eda_executive_summary.pdf`

---

*Document version: 1.0 — Phase 3 baseline*
