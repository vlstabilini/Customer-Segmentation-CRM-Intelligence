# Phase 1 — Business Understanding
### Customer Segmentation & CRM Intelligence Platform
**Target Role:** Data Analyst / Data Scientist @ Avelabs (에이브랩스)
**Author:** [Your Name]
**Phase Owner:** Business Analyst → Data Scientist
**Status:** ✅ Phase 1 Complete

---

## 1. Executive Summary

Modern retail and consumer-platform companies generate massive volumes of transactional data, yet most marketing decisions are still made on **gut feel, simple aggregate metrics, or one-size-fits-all campaigns**. The result is predictable: marketing budgets are over-spent on customers who would have bought anyway, high-value customers churn quietly, and CRM systems sit on top of data they cannot operationalize.

This project simulates a **consulting engagement with a mid-size online retailer** — the type of client Avelabs serves across Retail, Fashion, Beauty, and Platform businesses — and builds a **Customer Segmentation & CRM Intelligence Platform** that transforms raw transaction data into:

- A quantified understanding of *who the most valuable customers are*,
- *Which customers are at risk of churn*,
- *What marketing actions to take for each segment*, and
- An **AI Marketing Insights Agent** that converts these analytics into executive-ready recommendations on demand.

The deliverable is not a model — it is a **decision system**.

---

## 2. Business Problem Definition

### 2.1 The Client (Simulated)
A UK-based online retail company operating across 38 countries, primarily selling gift and homeware products to a mix of B2C consumers and small B2B resellers. Annual transaction volume exceeds 500,000 line items across roughly 4,300 unique customers.

### 2.2 The Pain Point
The marketing and CRM teams cannot answer the following questions with confidence:

| # | Business Question | Current State | Cost of Inaction |
|---|---|---|---|
| Q1 | Who are our most valuable customers? | Anecdotal — based on sales rep memory | Top customers receive same treatment as one-time buyers |
| Q2 | Which customers are about to churn? | No early warning system | Reactive win-back is 5–7× more expensive than retention |
| Q3 | Which customers deserve VIP treatment? | Loyalty program is flat — no tiers | VIPs feel under-appreciated; budget is sprayed evenly |
| Q4 | What marketing message should each customer receive? | Single bulk newsletter | Email engagement decays; unsubscribes rise |
| Q5 | What is the ROI of our CRM investments? | Cannot be measured at the segment level | Finance challenges marketing budget annually |
| Q6 | How do we grow revenue without acquiring more customers? | Acquisition-only growth strategy | CAC rises while existing-customer LTV is untapped |

### 2.3 The Strategic Framing
> **"The company does not have a customer acquisition problem. It has a customer intelligence problem."**

This re-framing is critical — it shifts the conversation from *spend more on ads* to *extract more value from existing customers*, which is where Avelabs' analytics services create the highest ROI for their clients.

### 2.4 Scope
**In scope:**
- Transactional data analysis (UCI Online Retail dataset, Dec 2010 – Dec 2011)
- Customer segmentation and CRM-tier design
- Marketing action recommendations per segment
- AI-assisted executive reporting layer

**Out of scope (explicit boundaries):**
- Product recommendation engines (deferred to v2)
- Real-time streaming pipelines (this is a batch-analytics MVP)
- Inventory and supply-chain optimization
- Paid-media attribution modeling

---

## 3. Stakeholder Analysis

| Stakeholder | Primary Concern | What They Need From This Project | Success Looks Like (for them) |
|---|---|---|---|
| **Chief Marketing Officer (CMO)** | Marketing ROI, brand equity | Clear segments, defensible budget allocation, executive narrative | Can present segment-based marketing strategy to the CEO with confidence |
| **CRM Manager** | Retention rate, lifecycle journeys | Actionable customer tiers (VIP, At-Risk, etc.) + churn alerts | Lifecycle email flows mapped to RFM segments; measurable retention lift |
| **Marketing Operations** | Campaign execution, targeting lists | Exportable segment lists + segment definitions | Can launch a 5-segment campaign in <1 day without engineering tickets |
| **Finance / FP&A** | Cost discipline, revenue forecasting | Revenue concentration analysis, CLV by segment | Can model marketing spend → revenue impact with segment-level granularity |
| **E-commerce / Product** | Conversion, repeat purchase rate | Behavioral patterns of high-LTV customers | Product page / checkout improvements informed by VIP behavior |
| **Customer Service** | Handling time, escalation routing | Awareness of which customers are high-value (VIP routing) | VIPs get prioritized support; service costs are tier-appropriate |
| **Data / Engineering Team** | Data reliability, system maintainability | Documented, reproducible pipeline | Notebooks → production handoff is trivial |
| **CEO / Board** | Growth, margin, defensibility | One-page strategic narrative + numbers that back it | Investor-grade story about customer-led growth |

**Primary stakeholder for this engagement:** CMO + CRM Manager (the budget owners).
**Secondary stakeholders:** Finance, Marketing Ops (the operationalizers).

---

## 4. Success Metrics (KPIs)

Success is measured on **three layers**: business outcomes, analytical outputs, and project execution.

### 4.1 Business Outcome KPIs (the only ones a CMO cares about)

| KPI | Baseline | Target | Why It Matters |
|---|---|---|---|
| **Repeat Purchase Rate** | TBD from EDA | +5–10 pp lift in 6 months | Direct measure of CRM effectiveness |
| **90-Day Churn Rate (high-value cohort)** | TBD from RFM | –20% relative reduction | Retention is 5–7× cheaper than acquisition |
| **Revenue from Top-20% Customers** | TBD (likely 60–80%) | Defend and grow concentration | Pareto reality: protect the revenue base |
| **Email Campaign Conversion Rate** | Industry avg ~2% | +30% relative lift via segmentation | Proves segmentation > batch-and-blast |
| **Customer Lifetime Value (avg)** | TBD | +15% in 12 months | Long-term enterprise value driver |

### 4.2 Analytical Output KPIs

| KPI | Target |
|---|---|
| Customer segments identified | 4–6 actionable, business-interpretable clusters |
| Segment stability (over time windows) | >70% customers stay in same / adjacent tier month-over-month |
| RFM coverage | 100% of customers with ≥1 purchase scored |
| Data quality | <5% rows discarded after cleaning; all discards documented |

### 4.3 Project Execution KPIs

| KPI | Target |
|---|---|
| Phases delivered on time | 9/9 |
| Files in GitHub repo | ≥25 |
| Reproducibility | Any reviewer can re-run all notebooks end-to-end |
| Recruiter-ready artifacts | Resume bullets, LinkedIn post, PPTX, README — all complete |

---

## 5. Hypothesis Register

> Avelabs' JD explicitly lists **Hypothesis Validation** as a required skill. This register makes that competency *visible and testable* throughout the project. Each hypothesis will be confirmed, rejected, or refined during EDA / RFM / segmentation phases.

| # | Hypothesis | Type | Phase to Validate | Business Implication if True |
|---|---|---|---|---|
| H1 | Revenue follows a Pareto distribution — top 20% of customers generate ≥70% of revenue | Concentration | Phase 3 (EDA) | Justifies VIP program; concentrates marketing spend on the vital few |
| H2 | The UK accounts for >80% of revenue, but non-UK markets have higher AOV (average order value) | Geographic | Phase 3 | Different growth strategies per geography |
| H3 | Customers who make a 2nd purchase within 30 days have >3× lifetime value of one-time buyers | Behavioral | Phase 4 | Justifies aggressive 30-day post-purchase nurture campaigns |
| H4 | A meaningful share of revenue comes from "wholesale-like" buyers (very high frequency, very high quantity) — i.e., B2B inside a B2C dataset | Segmentation | Phase 6 | Requires a separate B2B CRM track; standard consumer playbook will not fit |
| H5 | "At-Risk" customers (defined as: previously high-frequency, now dormant 60+ days) are recoverable with targeted win-back | Retention | Phase 5 (RFM) | Justifies a dedicated win-back budget line |
| H6 | December (gift season) drives a disproportionate share of new-customer acquisition, but these customers have poor 12-month retention | Seasonality | Phase 3 | Gift-season acquisition needs a dedicated retention playbook |
| H7 | Returns (negative quantity rows) are concentrated in a small subset of customers and product categories | Data quality / Behavior | Phase 2–3 | Operational fix + potential fraud / dissatisfaction signal |

---

## 6. Project Roadmap

| Phase | Deliverable | Primary Business Question Answered | Avelabs-JD Skill Demonstrated |
|---|---|---|---|
| **1. Business Understanding** ✅ | This document + README v0.1 | "What problem are we actually solving?" | Business Thinking, Communication |
| **2. Dataset Understanding** | Data dictionary + quality notebook | "Can we trust the data?" | SQL/Python, Data Analysis |
| **3. Exploratory Data Analysis** | EDA notebook + executive insights | "What is the data telling us?" | Analytical Thinking, Hypothesis Validation |
| **4. Customer Analytics** | Frequency, CLV, repeat-rate analysis | "Who drives the revenue?" | Customer Analytics |
| **5. RFM Analysis** | RFM scoring + CRM segments | "Who is at risk? Who is loyal?" | CRM Intelligence |
| **6. Customer Segmentation (ML)** | Clustering notebook + PPTX | "How should we treat each group?" | Machine Learning, Business Communication |
| **7. AI Marketing Insights Agent** | Agentic AI design + prototype | "How do we scale insight to decisions?" | LLMs, Agentic AI, Decision Systems |
| **8. Resume Integration** | Resume bullets, LinkedIn, STAR stories | "How does this become a job offer?" | Portfolio translation |
| **9. Application Package** | Resume PDF, GitHub, PPTX, Interview Pack | Final deliverable to Avelabs | Full-stack data professional |

### 6.1 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Dataset quality issues (returns, missing CustomerID) | High | Medium | Document all cleaning decisions in Phase 2 |
| Over-engineering the ML in Phase 6 | Medium | High | Keep clusters business-interpretable, not technically optimal |
| AI agent (Phase 7) feels like a demo, not a product | Medium | High | Frame as a decision-support system tied to real RFM outputs |
| Phase 8–9 polish gets rushed | Medium | Very High | Treat resume integration as a *first-class deliverable*, not an afterthought |

---

## 7. So What? — The Business Bridge

Every analytical deliverable in subsequent phases will be tied back to one of the following business levers:

1. **Revenue Protection** — keeping the top 20% of customers from churning
2. **Revenue Expansion** — moving mid-tier customers up the value ladder
3. **Cost Reduction** — stopping over-investment in unprofitable customer cohorts
4. **Decision Velocity** — letting the AI Agent shrink "insight-to-action" time from weeks to minutes

If an analysis cannot be tied to one of these four levers, it does not ship.

---

## 8. Why This Project, Why Avelabs

Avelabs' positioning is *enterprise decision intelligence through Data + AI + Agentic systems*, with explicit focus on Retail, Fashion, Beauty, and Platforms. This project is intentionally built as a **miniature of an Avelabs client engagement**:

- The dataset is real-world retail, matching Avelabs' core industries.
- The framing is consulting-grade — stakeholders, KPIs, hypotheses, scope.
- The deliverables span the full Avelabs stack: Analytics → ML → Agentic AI → BI Communication.
- The final artifact is a *decision system*, not a notebook.

This is not a coding exercise. It is a demonstration of how I would think and deliver on Day 30 of the job.

---

*Document version: 1.0 — Phase 1 baseline*
*Next phase: Dataset Understanding (Data Dictionary, Quality Assessment)*
