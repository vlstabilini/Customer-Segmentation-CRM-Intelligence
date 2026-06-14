"""
Phase 7 — AI Marketing Insights Agent (Prototype).

Design philosophy:
  • Deterministic, rule-based scaffolding (works without live LLM calls).
  • LLM-prompt templates embedded so the system is *production-ready* — swap the
    `_render` function with an LLM call to make it live.
  • Outputs in CMO-readable language + structured JSON for downstream systems.

This script runs the agent over the Phase 6 segmented customer table and
produces:
  - phase7_agent_outputs.json   (machine-readable)
  - reports/agent_sample_outputs.md  (human-readable, 5 persona briefs + churn alerts)
"""
import pandas as pd, numpy as np, json, os
from datetime import datetime

OUT_JSON = 'phase7_agent_outputs.json'
OUT_MD   = 'reports/agent_sample_outputs.md'

df = pd.read_csv('data/processed/customer_segments_ml.csv')

# -------------------------------------------------------------------
# Agent capabilities (4 tools)
# -------------------------------------------------------------------

def tool_persona_summary(df, persona):
    """Produces a structured per-persona executive brief."""
    sub = df[df['persona']==persona]
    total_rev = df['Monetary'].sum()
    return {
        'persona': persona,
        'customers': int(len(sub)),
        'customer_share_pct': round(len(sub)/len(df)*100, 1),
        'revenue': round(float(sub['Monetary'].sum()), 0),
        'revenue_share_pct': round(float(sub['Monetary'].sum()/total_rev*100), 1),
        'avg_monetary': round(float(sub['Monetary'].mean()), 0),
        'median_monetary': round(float(sub['Monetary'].median()), 0),
        'avg_frequency': round(float(sub['Frequency'].mean()), 1),
        'avg_recency_days': round(float(sub['Recency'].mean()), 0),
    }

def tool_churn_alert(df, persona, recency_threshold):
    """Surfaces high-value customers within a persona who have crossed a dormancy threshold."""
    sub = df[(df['persona']==persona) & (df['Recency'] > recency_threshold)]
    top = sub.nlargest(5, 'Monetary')[['CustomerID','Recency','Frequency','Monetary','country']]
    return {
        'persona': persona,
        'recency_threshold_days': recency_threshold,
        'at_risk_count': int(len(sub)),
        'at_risk_revenue': round(float(sub['Monetary'].sum()), 0),
        'top_5_to_recover': top.to_dict(orient='records'),
    }

def tool_revenue_opportunity(df, persona, target_persona):
    """Quantifies the upside of migrating customers from one persona to another."""
    src = df[df['persona']==persona]
    tgt = df[df['persona']==target_persona]
    src_avg = float(src['Monetary'].mean())
    tgt_avg = float(tgt['Monetary'].mean())
    lift = tgt_avg - src_avg
    return {
        'source_persona': persona,
        'target_persona': target_persona,
        'source_customers': int(len(src)),
        'source_avg_monetary': round(src_avg, 0),
        'target_avg_monetary': round(tgt_avg, 0),
        'per_customer_lift': round(lift, 0),
        'total_opportunity_if_all_migrated': round(lift * len(src), 0),
        'realistic_10pct_migration': round(lift * len(src) * 0.10, 0),
    }

def tool_campaign_recommendation(persona):
    """Returns the canonical campaign brief for a persona (from Phase 6 playbook)."""
    playbook = {
        'VIP B2B Accounts': {
            'campaign': 'Named Account Program',
            'priority': 'HIGHEST',
            'channel': 'Direct human (Account Manager) + personalized email',
            'budget_tier': 'Highest per-customer spend',
            'kpis': ['Account retention rate', 'Revenue per account YoY', 'NPS'],
            'actions': [
                'Assign Account Managers to top 50 within this cluster',
                'Custom pricing tier and quarterly business reviews',
                'Reorder workflows to remove friction on repeat orders',
                'Suppress from generic bulk-email campaigns',
            ],
        },
        'Loyal Repeat Buyers': {
            'campaign': 'Tier-Up to VIP',
            'priority': 'HIGH',
            'channel': 'Triggered email + retargeting + loyalty platform',
            'budget_tier': 'High',
            'kpis': ['Migration rate to VIP', 'Avg basket value', 'Frequency uplift'],
            'actions': [
                'Volume-discount thresholds that hint at VIP-tier rewards',
                'Loyalty tier program with VIP benefits at qualifying threshold',
                'Personalized cross-sell based on category affinity',
            ],
        },
        'Engaged New Buyers': {
            'campaign': '30-Day Nurture (H3 lever — 11.9x CLV multiplier)',
            'priority': 'HIGH (highest aggregate ROI)',
            'channel': 'Automated lifecycle email + onboarding',
            'budget_tier': 'Medium per-customer',
            'kpis': ['2nd-purchase rate within 30 days', 'Cohort retention at month 3'],
            'actions': [
                'Welcome series within 24 hours of first purchase',
                'Day-25 second-purchase trigger email (lands BEFORE the 73-day median repeat cadence)',
                'Product education content for category breadth',
                'Light incentive on 2nd order to reduce friction',
            ],
        },
        'Casual Low-Value Buyers': {
            'campaign': 'Quarterly Reactivation Promo',
            'priority': 'MEDIUM',
            'channel': 'Bulk email + light retargeting',
            'budget_tier': 'Low-medium',
            'kpis': ['Reactivation rate', 'Cost per reactivated customer'],
            'actions': [
                'Quarterly seasonal promo email (avoid over-frequency)',
                'Light retargeting around peak shopping windows',
                '90-day dormancy reactivation offer',
            ],
        },
        'Dormant Former Buyers': {
            'campaign': 'Annual Touch / Suppress',
            'priority': 'LOW',
            'channel': 'Bulk email (1x per year max)',
            'budget_tier': 'Lowest',
            'kpis': ['Cost per reactivation', 'Suppression list hygiene'],
            'actions': [
                'Single annual reactivation email',
                'Suppress from frequency-based campaigns',
                'Use as lookalike-exclusion seed for paid media',
            ],
        },
    }
    return {'persona': persona, **playbook.get(persona, {})}

# -------------------------------------------------------------------
# Agent reasoning loop (deterministic; LLM-prompt-shaped)
# -------------------------------------------------------------------
def render_executive_brief(persona, summary, alert, opp, recommendation):
    """Renders a CMO-readable brief. Replace this function body with an
    LLM call (using the `prompt_template` below) to make the system live."""

    prompt_template = (
        "You are a senior CRM strategist. Write a 6-bullet executive brief for "
        f"the '{persona}' segment using ONLY the data provided. Tone: CMO-ready, "
        "no jargon, every claim tied to a number. Structure: who they are, "
        "why they matter, top risk, top opportunity, recommended campaign, "
        "named KPI to measure success."
    )

    sections = []
    sections.append(f"### Executive Brief — {persona}")
    sections.append(f"_Generated by AI Marketing Insights Agent on {datetime.now().strftime('%Y-%m-%d')}._")
    sections.append("")
    sections.append(f"**Who they are.** {summary['customers']:,} customers ({summary['customer_share_pct']}% of base) "
                    f"with average historical value £{summary['avg_monetary']:,.0f}, average frequency "
                    f"{summary['avg_frequency']} orders, average recency {summary['avg_recency_days']:.0f} days.")
    sections.append(f"**Why they matter.** This persona contributes **£{summary['revenue']:,.0f} "
                    f"({summary['revenue_share_pct']}% of total revenue)** — context the CRM budget must respect.")
    if alert:
        sections.append(f"**Top risk.** {alert['at_risk_count']:,} customers in this persona crossed the "
                        f"{alert['recency_threshold_days']}-day dormancy line, representing "
                        f"£{alert['at_risk_revenue']:,.0f} of historical revenue. "
                        f"Top recoverable customer: CID {alert['top_5_to_recover'][0]['CustomerID']} "
                        f"with £{alert['top_5_to_recover'][0]['Monetary']:,.0f} historical value.")
    if opp:
        sections.append(f"**Top opportunity.** Migrating 10% of these customers into the "
                        f"'{opp['target_persona']}' tier = **£{opp['realistic_10pct_migration']:,.0f}** "
                        f"incremental annual revenue (per-customer lift £{opp['per_customer_lift']:,.0f}).")
    sections.append(f"**Recommended campaign.** {recommendation['campaign']} — priority "
                    f"{recommendation['priority']}, channel: {recommendation['channel']}, "
                    f"budget tier: {recommendation['budget_tier']}.")
    sections.append(f"**KPIs to measure success.** {', '.join(recommendation['kpis'])}.")
    sections.append("")
    return "\n".join(sections), prompt_template

# -------------------------------------------------------------------
# Run the agent across all 5 personas
# -------------------------------------------------------------------
PERSONAS = ['VIP B2B Accounts','Loyal Repeat Buyers','Engaged New Buyers',
            'Casual Low-Value Buyers','Dormant Former Buyers']
RECENCY_THRESHOLDS = {
    'VIP B2B Accounts':        30,
    'Loyal Repeat Buyers':     90,
    'Engaged New Buyers':      45,
    'Casual Low-Value Buyers': 180,
    'Dormant Former Buyers':   None,  # no alert needed
}
MIGRATION_PATHS = {
    'Loyal Repeat Buyers':     'VIP B2B Accounts',
    'Engaged New Buyers':      'Loyal Repeat Buyers',
    'Casual Low-Value Buyers': 'Engaged New Buyers',
    'Dormant Former Buyers':   None,
    'VIP B2B Accounts':        None,  # already at the top
}

all_outputs = {'briefs': [], 'churn_alerts': [], 'revenue_opportunities': [],
               'campaign_recommendations': []}

md_lines = []
md_lines.append("# 🤖 AI Marketing Insights Agent — Sample Outputs")
md_lines.append("### Phase 7 deliverable · Customer Segmentation & CRM Intelligence Platform")
md_lines.append("")
md_lines.append(f"_Generated on {datetime.now().strftime('%Y-%m-%d')} by the prototype agent against "
                f"the Phase 6 segmented customer table (4,338 customers, 5 personas)._")
md_lines.append("")
md_lines.append("These are **deterministic, rule-based sample outputs** from the prototype. The agent's "
                "design is LLM-ready — the rendering function carries an embedded prompt template that can "
                "be swapped for a live LLM call without changing any other component.")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 📋 Output 1 — Executive Briefs (one per persona)")
md_lines.append("")

for persona in PERSONAS:
    summary = tool_persona_summary(df, persona)
    thr = RECENCY_THRESHOLDS.get(persona)
    alert = tool_churn_alert(df, persona, thr) if thr else None
    tgt = MIGRATION_PATHS.get(persona)
    opp = tool_revenue_opportunity(df, persona, tgt) if tgt else None
    recommendation = tool_campaign_recommendation(persona)

    brief_md, prompt = render_executive_brief(persona, summary, alert, opp, recommendation)
    md_lines.append(brief_md)
    md_lines.append("---")
    md_lines.append("")
    all_outputs['briefs'].append({
        'persona': persona, 'summary': summary, 'alert': alert,
        'opportunity': opp, 'recommendation': recommendation,
        'llm_prompt_template': prompt,
    })

# -------------------------------------------------------------------
# Output 2 — Consolidated churn alerts
# -------------------------------------------------------------------
md_lines.append("## ⚠️ Output 2 — Consolidated Churn Alerts (cross-persona)")
md_lines.append("")
md_lines.append("| Persona | Threshold | At-risk count | At-risk revenue | Top customer ID | Top customer value |")
md_lines.append("|---|---|---|---|---|---|")
for persona in PERSONAS:
    thr = RECENCY_THRESHOLDS.get(persona)
    if thr is None: continue
    a = tool_churn_alert(df, persona, thr)
    if a['at_risk_count'] == 0: continue
    top = a['top_5_to_recover'][0]
    md_lines.append(f"| {persona} | {thr}d | **{a['at_risk_count']:,}** | "
                    f"£{a['at_risk_revenue']:,.0f} | CID {int(top['CustomerID'])} | "
                    f"£{top['Monetary']:,.0f} |")
    all_outputs['churn_alerts'].append(a)
md_lines.append("")
md_lines.append("---")
md_lines.append("")

# -------------------------------------------------------------------
# Output 3 — Revenue opportunity map
# -------------------------------------------------------------------
md_lines.append("## 💰 Output 3 — Revenue Opportunity Map (migration economics)")
md_lines.append("")
md_lines.append("| From | To | Customers | Per-customer lift | 10% migration upside |")
md_lines.append("|---|---|---|---|---|")
for persona, tgt in MIGRATION_PATHS.items():
    if tgt is None: continue
    o = tool_revenue_opportunity(df, persona, tgt)
    md_lines.append(f"| {persona} | {tgt} | {o['source_customers']:,} | "
                    f"£{o['per_customer_lift']:,.0f} | **£{o['realistic_10pct_migration']:,.0f}** |")
    all_outputs['revenue_opportunities'].append(o)
md_lines.append("")
md_lines.append("---")
md_lines.append("")

# -------------------------------------------------------------------
# Output 4 — Campaign briefs (structured)
# -------------------------------------------------------------------
md_lines.append("## 🎬 Output 4 — Campaign Briefs (machine-readable)")
md_lines.append("")
md_lines.append("Each persona's campaign brief is exportable as JSON for downstream CRM systems. Sample:")
md_lines.append("")
sample = tool_campaign_recommendation('Engaged New Buyers')
md_lines.append("```json")
md_lines.append(json.dumps(sample, indent=2))
md_lines.append("```")
md_lines.append("")
for p in PERSONAS:
    all_outputs['campaign_recommendations'].append(tool_campaign_recommendation(p))

md_lines.append("---")
md_lines.append("")
md_lines.append("## 🔧 Embedded LLM Prompt Template (for live deployment)")
md_lines.append("")
md_lines.append("The prototype renders briefs deterministically. To go live, replace the `render_executive_brief` "
                "function body with a single LLM call using this template:")
md_lines.append("")
md_lines.append("```")
md_lines.append(all_outputs['briefs'][0]['llm_prompt_template'])
md_lines.append("```")
md_lines.append("")
md_lines.append("Inputs available to the prompt: `summary`, `alert`, `opportunity`, `recommendation` "
                "(all structured dicts).")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append(f"*Agent prototype version: 1.0 · {datetime.now().strftime('%Y-%m-%d')}*")

with open(OUT_JSON,'w') as f:
    json.dump(all_outputs, f, indent=2, default=str)
with open(OUT_MD,'w') as f:
    f.write("\n".join(md_lines))

print(f"✓ Wrote {OUT_JSON}")
print(f"✓ Wrote {OUT_MD}")
print(f"✓ Briefs generated: {len(all_outputs['briefs'])}")
print(f"✓ Churn alerts:     {len(all_outputs['churn_alerts'])}")
print(f"✓ Opportunities:    {len(all_outputs['revenue_opportunities'])}")
