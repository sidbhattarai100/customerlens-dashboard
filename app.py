import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

st.set_page_config(page_title="CustomerLens", page_icon="🔍", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #070b14;
    color: #e2e8f0;
}
.block-container { padding: 2rem 3rem; }

.hero {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
    border: 1px solid #312e81;
    border-radius: 16px;
    padding: 2.5rem 3rem;
    margin-bottom: 2rem;
}
.hero h1 {
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(90deg, #818cf8, #a78bfa, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}
.hero p { color: #94a3b8; font-size: 1.05rem; margin-top: 0.5rem; }
.tag {
    display: inline-block;
    background: #1e1b4b;
    border: 1px solid #4338ca;
    color: #a5b4fc;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-right: 8px;
    margin-top: 8px;
}
.kpi-card {
    background: linear-gradient(145deg, #0f172a, #1e293b);
    border: 1px solid #1e293b;
    border-radius: 14px;
    padding: 1.5rem;
    text-align: center;
}
.kpi-value { font-size: 2rem; font-weight: 800; margin: 0.3rem 0; }
.kpi-label { font-size: 0.8rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.08em; }
.kpi-sub { font-size: 0.78rem; color: #475569; margin-top: 0.2rem; }
.section-header {
    font-size: 1.1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.section-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #4338ca, transparent);
    margin-left: 10px;
}
.segment-card {
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 0.8rem;
    border-left: 4px solid;
}
.insight-box {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 0.8rem;
}
.insight-box h4 { color: #a78bfa; margin: 0 0 0.4rem 0; font-size: 0.9rem; }
.insight-box p { color: #94a3b8; margin: 0; font-size: 0.85rem; line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class='hero'>
    <h1>CustomerLens</h1>
    <p>AI-powered customer segmentation platform — identifying behavioral clusters to drive smarter marketing decisions</p>
    <div>
        <span class='tag'>K-Means Clustering</span>
        <span class='tag'>AWS RDS</span>
        <span class='tag'>Python</span>
        <span class='tag'>Scikit-learn</span>
        <span class='tag'>2,240 Customers</span>
        <span class='tag'>4 Segments</span>
    </div>
</div>
""", unsafe_allow_html=True)

# KPI Cards
c1, c2, c3, c4, c5 = st.columns(5)
kpis = [
    ("2,240", "Total Customers", "All records analyzed", "#818cf8"),
    ("4", "Segments Found", "K-Means clusters", "#a78bfa"),
    ("$52,247", "Avg Income", "Across all customers", "#34d399"),
    ("$1,258,379", "Total Spending", "All product categories", "#f472b6"),
    ("11", "Features Used", "For clustering model", "#fb923c"),
]
for col, (val, label, sub, color) in zip([c1,c2,c3,c4,c5], kpis):
    col.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-label'>{label}</div>
        <div class='kpi-value' style='color:{color}'>{val}</div>
        <div class='kpi-sub'>{sub}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Data
segments = ['Premium Shoppers', 'Budget Shoppers', 'Online Middle Class', 'Gourmet Enthusiasts']
customers = [346, 1035, 546, 313]
incomes = [77591, 35007, 57143, 72699]
wine = [742, 41, 417, 492]
meat = [467, 22, 120, 398]
fruit = [40, 5, 18, 97]
fish = [66, 7, 26, 128]
sweets = [43, 5, 19, 98]
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
seg_colors = ['#7c3aed', '#2563eb', '#059669', '#d97706']
descriptions = [
    "Highest earners with dominant wine & meat spend. Prime targets for premium product campaigns.",
    "Budget-conscious, low spenders across all categories. Price-sensitive and deal-driven segment.",
    "Mid-income digital shoppers with highest web purchases. Best for online channel marketing.",
    "High-income foodies who prioritize variety — top spenders on fruits, fish & sweets.",
]
icons = ["💎", "💰", "🌐", "🍽️"]

# Main layout
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.markdown("<div class='section-header'>Customer Segments</div>", unsafe_allow_html=True)
    for i, (seg, desc, color, icon) in enumerate(zip(segments, descriptions, seg_colors, icons)):
        pct = round(customers[i] / sum(customers) * 100, 1)
        st.markdown(f"""
        <div class='segment-card' style='background:linear-gradient(135deg,#0f172a,#1e293b); border-left-color:{color};'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <div>
                    <span style='font-size:1.1rem; font-weight:700; color:{color};'>{icon} {seg}</span>
                    <span style='margin-left:10px; background:{color}22; color:{color}; border-radius:10px; padding:2px 10px; font-size:0.75rem; font-weight:600;'>{customers[i]} customers · {pct}%</span>
                </div>
                <div style='color:#f8fafc; font-size:1.1rem; font-weight:800;'>${incomes[i]:,}</div>
            </div>
            <div style='color:#94a3b8; font-size:0.83rem; margin-top:0.5rem;'>{desc}</div>
            <div style='margin-top:0.6rem;'>
                <span style='color:#64748b; font-size:0.75rem;'>Wine ${wine[i]} · Meat ${meat[i]} · Fruit ${fruit[i]} · Fish ${fish[i]} · Sweets ${sweets[i]}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='section-header' style='margin-top:1rem;'>Avg Income by Segment</div>", unsafe_allow_html=True)
    fig3, ax3 = plt.subplots(figsize=(5, 3))
    fig3.patch.set_facecolor('#0f172a')
    ax3.set_facecolor('#0f172a')
    bars = ax3.barh(segments, incomes, color=seg_colors, edgecolor='none', height=0.5)
    for bar, val in zip(bars, incomes):
        ax3.text(val + 500, bar.get_y() + bar.get_height()/2,
                 f'${val:,}', va='center', color='white', fontsize=8.5, fontweight='600')
    ax3.set_xlabel('Avg Income ($)', color='#64748b', fontsize=8)
    ax3.tick_params(colors='white', labelsize=8.5)
    ax3.set_xlim(0, max(incomes) * 1.2)
    for spine in ax3.spines.values():
        spine.set_color('#1e293b')
    ax3.invert_yaxis()
    plt.tight_layout()
    st.pyplot(fig3)

with col_right:
    st.markdown("<div class='section-header'>Distribution</div>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(4.5, 4))
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')
    wedges, texts, autotexts = ax.pie(
        customers, labels=None, colors=colors,
        autopct='%1.1f%%', startangle=140,
        pctdistance=0.75,
        wedgeprops=dict(width=0.6, edgecolor='#070b14', linewidth=2)
    )
    for at in autotexts:
        at.set_color('white')
        at.set_fontsize(9)
        at.set_fontweight('bold')
    legend_patches = [mpatches.Patch(color=colors[i], label=f"{segments[i]} ({customers[i]})") for i in range(4)]
    ax.legend(handles=legend_patches, loc='lower center', bbox_to_anchor=(0.5, -0.18),
              ncol=2, facecolor='#1e293b', edgecolor='#334155', labelcolor='white', fontsize=7.5)
    ax.set_title('Segment Breakdown', color='white', fontsize=11, fontweight='bold', pad=10)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("<div class='section-header' style='margin-top:1rem;'>Spending by Category</div>", unsafe_allow_html=True)
    fig2, ax2 = plt.subplots(figsize=(4.5, 3))
    fig2.patch.set_facecolor('#0f172a')
    ax2.set_facecolor('#0f172a')
    x = np.arange(4)
    w = 0.18
    cats = [wine, meat, fruit, fish]
    cat_labels = ['Wine', 'Meat', 'Fruit', 'Fish']
    cat_colors = ['#8b5cf6', '#ef4444', '#10b981', '#3b82f6']
    for i, (cat, label, c) in enumerate(zip(cats, cat_labels, cat_colors)):
        ax2.bar(x + i*w, cat, width=w, label=label, color=c, alpha=0.9)
    ax2.set_xticks(x + w*1.5)
    ax2.set_xticklabels(['Premium', 'Budget', 'Online', 'Gourmet'], color='white', fontsize=8)
    ax2.set_ylabel('Avg Spend ($)', color='#64748b', fontsize=8)
    ax2.tick_params(colors='#64748b', labelsize=8)
    for spine in ax2.spines.values():
        spine.set_color('#1e293b')
    ax2.legend(facecolor='#1e293b', edgecolor='#334155', labelcolor='white', fontsize=7, ncol=2)
    plt.tight_layout()
    st.pyplot(fig2)

st.markdown("<br>", unsafe_allow_html=True)

# Key Insights
st.markdown("<div class='section-header'>Key Insights</div>", unsafe_allow_html=True)
i1, i2, i3, i4 = st.columns(4)
insights = [
    ("Highest Revenue Segment", "Premium Shoppers generate the most value with $77K avg income and $742 avg wine spend — ideal for loyalty programs."),
    ("Largest Segment", "Budget Shoppers make up 46% of all customers. Small spend per head but massive volume opportunity with deals."),
    ("Digital-First Segment", "Online Middle Class leads in web purchases — best channel for email campaigns and retargeting ads."),
    ("Niche High-Value", "Gourmet Enthusiasts are small (14%) but spend heavily on premium food — perfect for specialty product upsells."),
]
for col, (title, body) in zip([i1,i2,i3,i4], insights):
    col.markdown(f"""
    <div class='insight-box'>
        <h4>{title}</h4>
        <p>{body}</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<br>
<div style='text-align:center; color:#334155; font-size:0.78rem; padding:1.5rem; border-top:1px solid #1e293b;'>
    CustomerLens · Built by Siddhartha Bhattarai · Python · K-Means · AWS RDS · Streamlit
</div>
""", unsafe_allow_html=True)