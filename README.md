# 🎯 Customer Segmentation & CRM Intelligence Platform
### v1.0 RELEASE · Avelabs Application Track · Data Analyst / Data Scientist

> **An end-to-end CRM analytics + Agentic AI portfolio project** — business framing → data quality → EDA → customer analytics → RFM segmentation → ML clustering → **Agentic AI advisor** → recruiter-ready application package.

---

## 🏢 The Business Problem

A UK-based online retailer (38 countries · 4,338 customers · 541,909 transactions · £8.89M cleaned revenue) makes marketing decisions on gut feel despite owning the data to do better.

> **Strategic re-framing:** The company does not have a customer *acquisition* problem; it has a customer *intelligence* problem.

---

## ⭐ Five Headline Outcomes

| Metric | What it means |
|---|---|
| **11.9×** | Fast 2nd-buyer CLV multiplier (predicted 3×, observed 11.9× — £4,892 vs £411) |
| **£1.06M** | Recoverable revenue pool quantified across 1,170 dormant-but-loyal customers |
| **689** | VIP B2B Accounts surfaced by ML — 16% of base driving 60% of revenue (13× larger than manual top-50) |
| **0.72** | Gini coefficient — top 20% of customers drive 75% of revenue |
| **22** | Business-captioned hero charts — every visual tied to a CRM action |

---

## 🗺️ The 9-Phase Roadmap (Complete)

| Phase | Status | Headline Output |
|---|---|---|
| 1. Business Understanding | ✅ | Stakeholders · KPIs · 7 hypotheses · roadmap |
| 2. Dataset Understanding | ✅ | 392,692 cleaned rows · 4,338 customers · £8.89M |
| 3. Exploratory Data Analysis | ✅ | H1, H2, H4 confirmed; H6 directional |
| 4. Customer Analytics | ✅ | CLV · cohort retention · **H3 at 11.9×** |
| 5. RFM Analysis | ✅ | 9 segments · H5 · £1.06M recoverable |
| 6. ML Segmentation | ✅ | 5 personas · K=5 · PPTX exec deck |
| 7. AI Marketing Insights Agent | ✅ | Agentic AI · system design · prototype · architecture deck |


---

## 📊 Cumulative Key Findings

### Phase 2 — Data Foundation
- 541K rows cleaned to 392,692 / 4,338 customers / £8.89M (99.2% of customers retained).
- 5-step documented cleaning pipeline; every drop tied to a business rule.

### Phase 3 — EDA
- **H1 ✅** Top 20% = 75% of revenue (Gini 0.72)
- **H2 ✅** International AOV = 1.9× UK (£850 vs £438)
- **H4 ✅** Top 50 customers = 33% revenue · 41 orders avg
- **H6 directional** Q4 dominates (Nov peak ~1.7× Q1)

### Phase 4 — Customer Analytics
- **H3 ✅ — and stronger than predicted.** Fast 2nd-buyers (≤30d) have **11.9× CLV** of never-repeaters
- **H6 retention ✅** Dec 2010 cohort: 100% → 38% (m3) → 27% (m12)
- 95 ultra-loyal customers drive 31% of revenue at avg CLV £29,316
- Median repeat cadence = 73 days → 30-day nurture is a behavioral accelerator

### Phase 5 — RFM Segmentation
- **H5 ✅** Recoverable pool = 1,170 customers · £1.06M (11.9% of revenue)
- Champions: 1,121 customers (26%) drive 65.9% of revenue
- 9-segment playbook with named action, channel, budget priority

### Phase 6 — ML Segmentation
- K-means (K=5) on log-transformed RFM + behavioral features
- 5 business-readable personas; **VIP B2B Accounts: 689 customers (16%) → 60.1% of revenue**
- **H4 strongly confirmed** — ML expands hidden B2B segment by 13×
- 13-slide PPTX with per-persona campaign cards

### Phase 7 — AI Marketing Insights Agent ⭐⭐
- 4 deterministic data-grounded tools + LLM rendering layer
- Design principle: *"The LLM renders. It does not decide."*
- Hallucination eliminated by construction — not by hoping
- DOCX system design + 9-slide PPTX architecture deck + working prototype





---

## 📁 Repository Structure (Final)
```
Customer-Segmentation-CRM-Intelligence/
├── README.md                                  ← v1.0 RELEASE
├── data/
│   ├── raw/Online_Retail.xlsx
│   └── processed/
│       ├── online_retail_cleaned.parquet
│       ├── customer_features.csv
│       ├── customer_rfm.csv
│       ├── customer_segments_ml.csv
│       └── cohort_retention_pct.csv
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_customer_analytics.ipynb
│   ├── 04_rfm_analysis.ipynb
│   ├── 05_customer_segmentation.ipynb
│   └── 06_ai_marketing_agent.ipynb
├── reports/
│   ├── 01_business_understanding.md / .docx
│   ├── 02_data_dictionary.md
│   ├── data_quality_summary.md
│   ├── 03_eda_executive_summary.md / .pdf
│   ├── 04_customer_analytics_insights.md
│   ├── 05_rfm_segment_playbook.md
│   ├── 06_segmentation_report.md
│   ├── 07_AI_Agent_System_Design.docx
│   └── agent_sample_outputs.md
├── presentations/
│   ├── 06_segmentation_executive_deck.pptx
│   ├── 07_AI_Agent_Architecture_Deck.pptx
│   └── 09_Final_Portfolio_Deck.pptx           ← ✅ NEW (Phase 9, 18 slides)
├── images/
│   └── chart1 … chart22.png                   ← 22 hero charts

```

---

## 🔧 Tech Stack
Python · pandas · NumPy · scikit-learn (K-means, PCA) · matplotlib · Jupyter · python-pptx · python-docx · ReportLab · LLM-ready prompt design

## 📂 Dataset
**UCI Online Retail Dataset** — UK-based online retailer (Dec 2010 – Dec 2011).
541,909 raw → 392,692 cleaned · 4,338 customers · 38 countries · £8.89M cleaned revenue

---

## 🤖 The Agentic AI Layer

A working AI Marketing Insights Agent on top of the 5-persona segmentation.

**Design principle:** *"The LLM renders. It does not decide."*

- **4 deterministic tools** (persona summary · churn alert · revenue opportunity · campaign recommendation)
- **LLM rendering layer** with embedded prompt template
- **Production-ready architecture** — one-function-swap to live LLM
- **6 guardrails** documented (output validation · golden-set regression · schema validation · cost · latency · observability)

---

## 🚀 Future Work (Roadmap)
- **V2 Agent:** Live LLM swap-in (single-function change)
- **V3 Agent:** Multi-agent coordinator routing stakeholder queries
- **V4 Agent:** Predictive churn integration (BG/NBD · Gamma-Gamma)
- **Streamlit dashboard** for self-service CRM Manager querying
- **Hypothesis H7** — returns concentration analysis
- **Real-time CRM event streaming**

---

## 📬 Contact
- LinkedIn: https://www.linkedin.com/in/stabilinivlada/
- Email: vlstabilini@naver.com
- GitHub: https://github.com/vlstabilini

---

*Version: 1.0 RELEASE — All 9 phases complete. Ready to ship.*
