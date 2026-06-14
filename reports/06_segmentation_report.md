# 🧬 Phase 6 — ML-Driven Customer Segmentation Report
### Customer Segmentation & CRM Intelligence Platform

**Audience:** CMO · CRM Manager · Data team
**Purpose:** Document the 5-persona ML segmentation, validate it against the Phase 5 RFM taxonomy, and translate each persona into a named marketing campaign.

---

## 1. Method

| Step | Choice | Reasoning |
|---|---|---|
| Algorithm | K-Means | Interpretable centroids; recognized by every CRM and marketing-ops team |
| Features | log(R), log(F), log(M), log(avg_basket), log(tenure_days) | Log transforms compress the right-skew documented in Phases 3–4 |
| Scaling | StandardScaler | Equalizes feature weight across dimensions |
| K selection | **K = 5** | Business-readable; near elbow; silhouette = 0.279 |
| Validation | PCA visualization + RFM cross-tab | 2 PCs explain 83.9% variance; strong convergence with RFM Champions |

> **Why not the K with the highest silhouette?** K=2 had a marginally higher silhouette but collapsed all valuable customers into one undifferentiated blob — useless for CRM. **The right K is the one that produces personas you can build campaigns around**, not the one that optimizes a single statistical metric.

---

## 2. The 5 Personas

| Persona | Customers | % of base | Revenue | % revenue | Avg Monetary | Avg Frequency | Avg Recency |
|---|---|---|---|---|---|---|---|
| **VIP B2B Accounts** | 689 | 15.9% | £5,343,349 | **60.1%** | £7,755 | 14.0 | 11 days |
| Loyal Repeat Buyers | 899 | 20.7% | £2,260,131 | 25.4% | £2,514 | 4.0 | 67 days |
| Engaged New Buyers | 1,140 | 26.3% | £683,417 | 7.7% | £599 | 3.2 | 71 days |
| Casual Low-Value Buyers | 807 | 18.6% | £476,183 | 5.4% | £590 | 1.1 | 146 days |
| Dormant Former Buyers | 803 | 18.5% | £124,130 | 1.4% | £155 | 1.1 | 168 days |
| **Total** | **4,338** | 100% | **£8,887,209** | 100% | | | |

---

## 3. Persona Profiles

### 🥇 VIP B2B Accounts (689 customers · 60.1% of revenue)
- **Signature:** High monetary, high frequency, very recent, high basket value
- **Story:** This is the "hidden B2B" segment first surfaced in Phase 3 (H4) — the ML clustering surfaces a *much larger* cohort (689) than the manual top-50 cutoff. They buy 14 times on average in 13 months, with basket sizes 4–10× the median customer.
- **Named campaign:** **Named Account Program** — assign account managers, custom pricing, quarterly business reviews, reorder workflows.
- **Channel:** Direct human (AM) + personalized email.
- **Budget:** Highest per-customer spend justified by economics.

### 🥈 Loyal Repeat Buyers (899 customers · 25.4% of revenue)
- **Signature:** Moderate monetary, moderate frequency, recent, mid basket
- **Story:** The natural pipeline into VIP. Already proving repeat behavior at 4 orders avg.
- **Named campaign:** **Tier-Up to VIP** — frequency-uplift campaigns, loyalty tier program, cross-sell to grow basket.
- **Channel:** Triggered email + retargeting + loyalty platform.
- **Budget:** High; tier-up ROI is strong.

### 🌱 Engaged New Buyers (1,140 customers · 7.7% of revenue)
- **Signature:** Low frequency (3 orders), recent, low monetary
- **Story:** The biggest persona by headcount. **Phase 4's H3 finding (11.9× CLV multiplier) makes this the highest-aggregate-ROI lever in the project.** Convert these to "Loyal" tier and you've built a sustainable pipeline.
- **Named campaign:** **30-Day Nurture** — welcome series, day-25 second-purchase trigger (just before the natural 73-day median repeat cadence).
- **Channel:** Automated lifecycle email + onboarding.
- **Budget:** Medium per-customer; highest aggregate ROI across the portfolio.

### 🌤️ Casual Low-Value Buyers (807 customers · 5.4% of revenue)
- **Signature:** Very low frequency (~1 order), moderate recency, low monetary
- **Story:** Bought once, came back rarely. Not zero-value, but not a priority.
- **Named campaign:** **Quarterly Reactivation Promo** — seasonal touchpoints only.
- **Channel:** Bulk email + light retargeting.
- **Budget:** Low-medium per-customer.

### 😴 Dormant Former Buyers (803 customers · 1.4% of revenue)
- **Signature:** Very low frequency, very high recency (~168 days), lowest monetary
- **Story:** Functionally churned. Reactivation economics are unfavorable.
- **Named campaign:** **Annual Touch / Suppress** — 1× annual email maximum; otherwise suppress.
- **Channel:** Bulk email · low frequency.
- **Budget:** Lowest — explicitly *do not over-invest*.

---

## 4. Cross-Validation vs. Phase 5 RFM Segments

| ML Persona ↓ / RFM Segment → | Champions | Loyal Customers | Potential Loyalists | New Customers | Promising | Cannot Lose Them | At Risk | About to Sleep | Hibernating |
|---|---|---|---|---|---|---|---|---|---|
| VIP B2B Accounts | **656** | 25 | 3 | 0 | 0 | 5 | 0 | 0 | 0 |
| Loyal Repeat Buyers | 217 | **182** | 87 | 10 | 13 | 144 | 150 | 26 | 70 |
| Engaged New Buyers | 247 | 120 | **200** | 22 | 30 | 132 | 259 | 27 | 103 |
| Casual Low-Value Buyers | 0 | 2 | 5 | 37 | 81 | 1 | 215 | 167 | 299 |
| Dormant Former Buyers | 1 | 0 | 9 | 30 | 87 | 3 | 261 | 131 | **281** |

**Key findings:**
- **Top-tier convergence is strong:** 656 of 1,121 Champions (59%) land in VIP B2B Accounts. The two methods *agree* on who the most valuable customers are.
- **Mid-tier divergence is informative:** ML clustering groups by *behavioral fingerprint* (basket size, tenure) rather than score thresholds — pulling some RFM Champions into Loyal Repeat Buyers if their basket is smaller, and some Cannot Lose Them into Engaged New Buyers if their behavioral profile is "new again."
- **Bottom-tier convergence is strong:** Dormant Former Buyers absorbs 281 RFM Hibernating customers (37% of all Hibernating).
- **Recommendation:** Use **ML personas for strategy** (campaign design, budget allocation) and **RFM segments for tactical targeting** (lifecycle triggers, send-list inclusion rules).

---

## 5. Hypothesis Update

| # | Hypothesis | Phase | Verdict |
|---|---|---|---|
| H4 | Hidden B2B segment in B2C data | P3 confirmed at 50; **P6 expands to 689** | ✅ **STRONGLY CONFIRMED** |

The ML clustering doesn't just confirm H4 — it shows the manual estimate **understated the B2B cohort by 13×**.

---

## 6. Q1 Budget Allocation

| Priority | Persona | Budget Tier | Q1 Action |
|---|---|---|---|
| 🔴 1 | VIP B2B Accounts | Highest per-customer | Account-managed retention |
| 🔴 2 | Engaged New Buyers | Medium · highest aggregate ROI | 30-day nurture (H3) |
| 🟡 3 | Loyal Repeat Buyers | High | Tier-up campaigns |
| 🟡 4 | Casual Low-Value Buyers | Low-medium | Quarterly seasonal promo |
| ⚪ 5 | Dormant Former Buyers | Lowest | Annual touch · suppress otherwise |

**Principle:** Budget follows revenue concentration AND lifecycle leverage — not customer-count parity.

---

## 7. Hand-off to Phase 7

The `customer_segments_ml.csv` is the **direct input to Phase 7 AI Marketing Insights Agent**. The agent will:
- Read live persona labels
- Generate per-segment executive summaries on demand
- Surface churn alerts (recency degradation within VIP / Loyal tiers)
- Recommend campaign moves based on the playbook above

---

## 📁 Supporting Artifacts

- Notebook: `notebooks/05_customer_segmentation.ipynb`
- Executive deck: `presentations/06_segmentation_executive_deck.pptx`
- Segment-labeled customers: `data/processed/customer_segments_ml.csv`
- Hero charts: `images/chart17` … `chart21`

---

*Document version: 1.0 — Phase 6 baseline*
