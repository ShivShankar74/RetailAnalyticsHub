import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

APP_NAME = "Retail Analytics Hub"

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# DESIGN TOKENS  —  "Aurora Glass" theme
# ============================================================

BG = "#080B1A"
PANEL = "#111633"
PANEL_ALT = "#171D42"
PANEL_BORDER = "rgba(139,92,246,0.28)"
GRID = "rgba(148,163,255,0.12)"
TEXT = "#F1F3FF"
TEXT_DIM = "#9AA3C7"

VIOLET = "#8B5CF6"
CYAN = "#22D3EE"
PINK = "#F472B6"
AMBER = "#FBBF24"
GREEN = "#34D399"

COLORWAY = [VIOLET, CYAN, PINK, AMBER, GREEN, "#60A5FA", "#FB7185", "#A78BFA"]

# ============================================================
# PLOTLY TEMPLATE
# ============================================================

pio.templates["aurora"] = pio.templates["plotly_dark"]
pio.templates["aurora"].layout.update(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Poppins, sans-serif", color=TEXT, size=13),
    title=dict(font=dict(family="Poppins, sans-serif", size=16, color=TEXT)),
    colorway=COLORWAY,
    xaxis=dict(gridcolor=GRID, zerolinecolor=GRID, linecolor=GRID),
    yaxis=dict(gridcolor=GRID, zerolinecolor=GRID, linecolor=GRID),
    legend=dict(bgcolor="rgba(0,0,0,0)"),
    margin=dict(t=60, l=10, r=10, b=10),
)
pio.templates.default = "aurora"

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
    }}

    /* ---- Aurora background ---- */
    .stApp {{
        background:
            radial-gradient(900px 500px at 8% -5%, rgba(139,92,246,0.28), transparent 60%),
            radial-gradient(800px 500px at 95% 5%, rgba(34,211,238,0.18), transparent 60%),
            radial-gradient(700px 500px at 50% 110%, rgba(244,114,182,0.16), transparent 60%),
            {BG};
        background-attachment: fixed;
        color: {TEXT};
    }}

    header[data-testid="stHeader"] {{
        background: transparent;
    }}

    .main .block-container {{
        padding-top: 1.5rem;
        max-width: 1320px;
    }}

    /* ---- Sidebar ---- */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #12173A 0%, #0B0F26 100%);
        border-right: 1px solid {PANEL_BORDER};
    }}
    section[data-testid="stSidebar"] * {{
        color: {TEXT} !important;
    }}

    .sb-brand {{
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 6px 0 14px 0;
        margin-bottom: 10px;
        border-bottom: 1px solid {PANEL_BORDER};
    }}
    .sb-brand .logo {{
        width: 36px; height: 36px;
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 18px;
        background: linear-gradient(135deg, {VIOLET}, {CYAN});
        box-shadow: 0 6px 18px rgba(139,92,246,0.45);
    }}
    .sb-brand .name {{
        font-weight: 700;
        font-size: 15px;
        line-height: 1.1;
    }}
    .sb-brand .tag {{
        font-size: 11px;
        color: {TEXT_DIM} !important;
    }}

    /* ---- Hero header ---- */
    .hero {{
        position: relative;
        overflow: hidden;
        border-radius: 20px;
        padding: 30px 34px;
        margin-bottom: 14px;
        background:
            linear-gradient(135deg, rgba(139,92,246,0.35), rgba(34,211,238,0.18) 60%, rgba(244,114,182,0.22));
        border: 1px solid {PANEL_BORDER};
        box-shadow: 0 20px 50px rgba(0,0,0,0.35);
        animation: fadeInUp 0.6s ease-out;
    }}
    .hero::after {{
        content: "";
        position: absolute;
        right: -60px; top: -60px;
        width: 240px; height: 240px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(255,255,255,0.18), transparent 70%);
        animation: floaty 7s ease-in-out infinite;
    }}
    .hero .eyebrow {{
        display: inline-block;
        font-size: 11.5px;
        font-weight: 600;
        letter-spacing: 1.6px;
        text-transform: uppercase;
        color: {CYAN};
        background: rgba(34,211,238,0.12);
        border: 1px solid rgba(34,211,238,0.35);
        padding: 4px 12px;
        border-radius: 999px;
        margin-bottom: 12px;
    }}
    .hero h1 {{
        font-weight: 700;
        font-size: 38px;
        margin: 0;
        line-height: 1.15;
        background: linear-gradient(90deg, #FFFFFF 10%, #C4B5FD 50%, #67E8F9 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .hero p {{
        color: {TEXT_DIM};
        font-size: 15px;
        margin: 8px 0 0 0;
    }}

    .meta-row {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin: 0 0 8px 2px;
    }}
    .chip {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        color: {TEXT_DIM};
        background: rgba(255,255,255,0.04);
        border: 1px solid {PANEL_BORDER};
        padding: 5px 12px;
        border-radius: 999px;
    }}
    .chip b {{ color: {TEXT}; font-weight: 700; }}

    /* ---- Section headers ---- */
    .db-section {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 38px 0 16px 0;
    }}
    .db-section .pill {{
        width: 5px;
        height: 26px;
        border-radius: 6px;
        background: linear-gradient(180deg, {VIOLET}, {CYAN});
        box-shadow: 0 0 14px rgba(139,92,246,0.7);
    }}
    .db-section h3 {{
        font-weight: 600;
        font-size: 20px;
        color: {TEXT};
        margin: 0;
    }}
    .db-section .sub {{
        color: {TEXT_DIM};
        font-size: 13px;
    }}

    /* ---- KPI cards ---- */
    .kpi-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(185px, 1fr));
        gap: 14px;
        margin-bottom: 6px;
    }}
    .kpi-card {{
        position: relative;
        overflow: hidden;
        background: linear-gradient(160deg, rgba(255,255,255,0.07), rgba(255,255,255,0.02));
        backdrop-filter: blur(10px);
        border: 1px solid {PANEL_BORDER};
        border-radius: 16px;
        padding: 18px 20px;
        animation: fadeInUp 0.55s ease-out backwards;
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    }}
    .kpi-card::before {{
        content: "";
        position: absolute;
        left: 0; top: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--kpi-a), var(--kpi-b));
    }}
    .kpi-card:hover {{
        transform: translateY(-5px);
        border-color: var(--kpi-a);
        box-shadow: 0 14px 34px rgba(0,0,0,0.4), 0 0 24px -6px var(--kpi-a);
    }}
    .kpi-card .kpi-icon {{
        width: 34px; height: 34px;
        display: flex; align-items: center; justify-content: center;
        border-radius: 10px;
        font-size: 16px;
        margin-bottom: 12px;
        background: linear-gradient(135deg, var(--kpi-a), var(--kpi-b));
    }}
    .kpi-card .kpi-label {{
        color: {TEXT_DIM};
        font-size: 12.5px;
        font-weight: 500;
        margin-bottom: 4px;
    }}
    .kpi-card .kpi-value {{
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        font-size: 24px;
        color: {TEXT};
        letter-spacing: -0.4px;
    }}
    .kpi-card:nth-child(1) {{ animation-delay: 0.02s; }}
    .kpi-card:nth-child(2) {{ animation-delay: 0.08s; }}
    .kpi-card:nth-child(3) {{ animation-delay: 0.14s; }}
    .kpi-card:nth-child(4) {{ animation-delay: 0.20s; }}
    .kpi-card:nth-child(5) {{ animation-delay: 0.26s; }}
    .kpi-card:nth-child(6) {{ animation-delay: 0.32s; }}

    /* ---- Chart & table glass panels ---- */
    div[data-testid="stPlotlyChart"] {{
        background: linear-gradient(160deg, rgba(255,255,255,0.05), rgba(255,255,255,0.015));
        border: 1px solid {PANEL_BORDER};
        border-radius: 16px;
        padding: 10px 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        animation: fadeInUp 0.7s ease-out backwards;
    }}

    div[data-testid="stDataFrame"] {{
        border: 1px solid {PANEL_BORDER};
        border-radius: 14px;
        overflow: hidden;
        animation: fadeInUp 0.7s ease-out backwards;
    }}

    div[data-testid="stMetric"] {{
        background: linear-gradient(160deg, rgba(255,255,255,0.07), rgba(255,255,255,0.02));
        border: 1px solid {PANEL_BORDER};
        border-radius: 14px;
        padding: 14px 18px;
    }}
    div[data-testid="stMetricValue"] {{
        font-family: 'JetBrains Mono', monospace;
    }}

    div[data-testid="stExpander"] {{
        background: rgba(255,255,255,0.03);
        border: 1px solid {PANEL_BORDER};
        border-radius: 14px;
    }}

    .stAlert {{
        background: rgba(139,92,246,0.10);
        border: 1px solid {PANEL_BORDER};
        border-radius: 14px;
    }}

    /* multiselect tags */
    span[data-baseweb="tag"] {{
        background: linear-gradient(135deg, {VIOLET}, #6D28D9) !important;
        border-radius: 8px !important;
    }}

    hr {{
        border-color: {PANEL_BORDER};
    }}

    .footer {{
        text-align: center;
        color: {TEXT_DIM};
        font-size: 12.5px;
        padding: 10px 0 24px 0;
    }}
    .footer b {{
        background: linear-gradient(90deg, {VIOLET}, {CYAN});
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    /* ---- Animations ---- */
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(16px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes floaty {{
        0%, 100% {{ transform: translate(0, 0); }}
        50%      {{ transform: translate(-18px, 14px); }}
    }}
</style>
""", unsafe_allow_html=True)


def section_header(title, subtitle=None):
    """Renders a styled section header."""
    sub_html = f'<span class="sub">— {subtitle}</span>' if subtitle else ""
    st.markdown(
        f'<div class="db-section"><div class="pill"></div>'
        f'<h3>{title}</h3>{sub_html}</div>',
        unsafe_allow_html=True
    )


def kpi_grid(cards):
    """cards: list of (icon, label, value, color_a, color_b) tuples."""
    html = '<div class="kpi-grid">'
    for icon, label, value, a, b in cards:
        html += (
            f'<div class="kpi-card" style="--kpi-a:{a}; --kpi-b:{b}">'
            f'<div class="kpi-icon">{icon}</div>'
            f'<div class="kpi-label">{label}</div>'
            f'<div class="kpi-value">{value}</div>'
            f'</div>'
        )
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def style_fig(fig):
    """Shared finishing touches for every chart."""
    fig.update_layout(hoverlabel=dict(bgcolor=PANEL_ALT, font_color=TEXT))
    return fig


# ============================================================
# DATASET CONFIGURATION
# ============================================================

EXPECTED_COLUMNS = [
    "transaction_id",
    "customer_id",
    "category",
    "item",
    "price_per_unit",
    "quantity",
    "total_spent",
    "payment_method",
    "transaction_date",
    "discount_applied",
    "year",
    "month",
    "month_name",
    "average_transaction_value",
    "discount_status"
]


# ============================================================
# FIND DATASET
# ============================================================

def find_dataset():

    data_dir = Path(__file__).resolve().parent

    possible_files = [
        data_dir / "retail-orders-clean.csv",
        data_dir / "clean_dataset.csv",
        data_dir / "retail_orders_clean.csv",
        data_dir / "retail_orders.csv"
    ]

    for file in possible_files:
        if file.exists():
            return file

    csv_files = list(data_dir.glob("*.csv"))

    if len(csv_files) == 1:
        return csv_files[0]

    if len(csv_files) > 1:
        st.error(
            "Multiple CSV files found in the data folder. "
            "Please keep only the Task 03 cleaned dataset."
        )

        st.write("CSV files found:")

        for file in csv_files:
            st.write(f"- `{file.name}`")

        st.stop()

    return None


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_dataset(file_path):

    df = pd.read_csv(file_path)

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    df.columns = df.columns.str.replace("*", "", regex=False)
    df.columns = df.columns.str.replace("\ufeff", "", regex=False)

    missing_columns = [
        col for col in EXPECTED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        st.error("Dataset columns do not match the expected Task 03 dataset.")

        st.write("### Missing columns")
        st.write(missing_columns)

        st.write("### Columns detected in your CSV")
        st.write(list(df.columns))

        st.stop()

    df = df[EXPECTED_COLUMNS].copy()

    numeric_columns = [
        "price_per_unit",
        "quantity",
        "total_spent",
        "discount_applied",
        "year",
        "month",
        "average_transaction_value"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

    df = df.dropna(
        subset=[
            "transaction_id",
            "customer_id",
            "category",
            "total_spent",
            "transaction_date"
        ]
    )

    return df


# ============================================================
# GET DATASET
# ============================================================

dataset_path = find_dataset()

if dataset_path is None:

    st.error("No CSV dataset found.")

    st.info(
        "Place your cleaned CSV next to `app.py` "
        "and name it `retail-orders-clean.csv`."
    )

    st.stop()


df = load_dataset(dataset_path)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown(
    f'<div class="sb-brand"><div class="logo">🛍️</div>'
    f'<div><div class="name">{APP_NAME}</div>'
    f'<div class="tag">Sales · Customers · Insights</div></div></div>',
    unsafe_allow_html=True
)

st.sidebar.markdown("### 🎛️ Filters")

min_date = df["transaction_date"].min().date()
max_date = df["transaction_date"].max().date()

date_range = st.sidebar.date_input(
    "Transaction Date",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date = pd.Timestamp(date_range[0])
    end_date = pd.Timestamp(date_range[1])
else:
    start_date = pd.Timestamp(min_date)
    end_date = pd.Timestamp(max_date)

categories = sorted(df["category"].dropna().unique().tolist())
selected_categories = st.sidebar.multiselect(
    "Category", categories, default=categories
)

payment_methods = sorted(df["payment_method"].dropna().unique().tolist())
selected_payment = st.sidebar.multiselect(
    "Payment Method", payment_methods, default=payment_methods
)

discount_options = sorted(df["discount_status"].dropna().unique().tolist())
selected_discount = st.sidebar.multiselect(
    "Discount Status", discount_options, default=discount_options
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df[
    (df["transaction_date"] >= start_date)
    & (df["transaction_date"] < end_date + pd.Timedelta(days=1))
    & (df["category"].isin(selected_categories))
    & (df["payment_method"].isin(selected_payment))
    & (df["discount_status"].isin(selected_discount))
].copy()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    f'<div class="hero">'
    f'<span class="eyebrow">Live Business Intelligence</span>'
    f'<h1>{APP_NAME}</h1>'
    f'<p>Interactive sales, customer &amp; business performance analysis</p>'
    f'</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="meta-row">'
    f'<span class="chip">DATASET <b>{dataset_path.name}</b></span>'
    f'<span class="chip">RECORDS <b>{len(filtered_df):,}</b> / {len(df):,}</span>'
    f'<span class="chip">PERIOD <b>{start_date:%d %b %Y} → {end_date:%d %b %Y}</b></span>'
    f'</div>',
    unsafe_allow_html=True
)


# ============================================================
# FILTERED KPIs
# ============================================================

revenue = filtered_df["total_spent"].sum()
transactions = filtered_df["transaction_id"].nunique()
customers = filtered_df["customer_id"].nunique()
aov = revenue / transactions if transactions > 0 else 0
quantity = filtered_df["quantity"].sum()
discount_pct = (
    filtered_df["discount_applied"].eq(1).sum() / len(filtered_df) * 100
    if len(filtered_df) > 0
    else 0
)

section_header("Executive KPIs", "headline numbers for your current filters")

kpi_grid([
    ("💰", "Revenue", f"₹{revenue:,.0f}", VIOLET, "#6D28D9"),
    ("🧾", "Transactions", f"{transactions:,}", CYAN, "#0EA5E9"),
    ("👥", "Customers", f"{customers:,}", PINK, "#DB2777"),
    ("📈", "Avg order value", f"₹{aov:,.2f}", AMBER, "#F59E0B"),
    ("📦", "Total quantity", f"{quantity:,.0f}", GREEN, "#10B981"),
    ("🏷️", "Discounted orders", f"{discount_pct:.1f}%", "#60A5FA", "#6366F1"),
])


# ============================================================
# CHECK EMPTY DATA
# ============================================================

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()


# ============================================================
# REVENUE TREND
# ============================================================

section_header("Revenue Trend", "month by month")

monthly_revenue = (
    filtered_df
    .groupby(filtered_df["transaction_date"].dt.to_period("M"))["total_spent"]
    .sum()
    .reset_index()
)
monthly_revenue["transaction_date"] = monthly_revenue["transaction_date"].dt.to_timestamp()

fig_revenue = px.area(
    monthly_revenue,
    x="transaction_date",
    y="total_spent",
    markers=True,
    title="Monthly Revenue Trend"
)
fig_revenue.update_traces(
    line=dict(color=VIOLET, width=3),
    fillcolor="rgba(139,92,246,0.22)",
    marker=dict(color=CYAN, size=7)
)
fig_revenue.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue (₹)",
    hovermode="x unified"
)
st.plotly_chart(style_fig(fig_revenue), use_container_width=True)


# ============================================================
# CATEGORY ANALYSIS
# ============================================================

section_header("Category Performance")

category_revenue = (
    filtered_df
    .groupby("category")["total_spent"]
    .sum()
    .reset_index()
    .sort_values("total_spent", ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    fig_category = px.bar(
        category_revenue,
        x="category",
        y="total_spent",
        title="Revenue by Category",
        text_auto=".2s",
        color="category",
        color_discrete_sequence=COLORWAY
    )
    fig_category.update_traces(marker_line_width=0)
    fig_category.update_layout(
        xaxis_title="Category",
        yaxis_title="Revenue (₹)",
        showlegend=False
    )
    st.plotly_chart(style_fig(fig_category), use_container_width=True)

with col2:
    fig_category_pie = px.pie(
        category_revenue,
        names="category",
        values="total_spent",
        title="Revenue Share by Category",
        hole=0.6,
        color_discrete_sequence=COLORWAY
    )
    fig_category_pie.update_traces(
        marker=dict(line=dict(color=BG, width=2))
    )
    st.plotly_chart(style_fig(fig_category_pie), use_container_width=True)


# ============================================================
# PAYMENT METHOD
# ============================================================

section_header("Payment Method Analysis")

payment_revenue = (
    filtered_df
    .groupby("payment_method")["total_spent"]
    .sum()
    .reset_index()
    .sort_values("total_spent", ascending=False)
)

fig_payment = px.bar(
    payment_revenue,
    x="payment_method",
    y="total_spent",
    color="payment_method",
    title="Revenue by Payment Method",
    text_auto=".2s",
    color_discrete_sequence=COLORWAY
)
fig_payment.update_layout(
    xaxis_title="Payment Method",
    yaxis_title="Revenue (₹)",
    showlegend=False
)
st.plotly_chart(style_fig(fig_payment), use_container_width=True)


# ============================================================
# DISCOUNT ANALYSIS
# ============================================================

section_header("Discount Analysis")

discount_analysis = (
    filtered_df
    .groupby("discount_status")
    .agg(
        Revenue=("total_spent", "sum"),
        Transactions=("transaction_id", "nunique"),
        Quantity=("quantity", "sum")
    )
    .reset_index()
)

col1, col2 = st.columns(2)

with col1:
    fig_discount = px.bar(
        discount_analysis,
        x="discount_status",
        y="Revenue",
        title="Revenue by Discount Status",
        text_auto=".2s",
        color="discount_status",
        color_discrete_sequence=[CYAN, PINK, VIOLET, AMBER]
    )
    fig_discount.update_layout(showlegend=False)
    st.plotly_chart(style_fig(fig_discount), use_container_width=True)

with col2:
    fig_discount_pie = px.pie(
        discount_analysis,
        names="discount_status",
        values="Transactions",
        title="Transactions by Discount Status",
        hole=0.6,
        color_discrete_sequence=[CYAN, PINK, VIOLET, AMBER]
    )
    fig_discount_pie.update_traces(
        marker=dict(line=dict(color=BG, width=2))
    )
    st.plotly_chart(style_fig(fig_discount_pie), use_container_width=True)


# ============================================================
# CATEGORY × MONTH HEATMAP
# ============================================================

section_header("Category × Monthly Revenue Heatmap")

heatmap_data = (
    filtered_df
    .assign(month_period=filtered_df["transaction_date"].dt.to_period("M"))
    .groupby(["category", "month_period"])["total_spent"]
    .sum()
    .reset_index()
)
heatmap_data["month_period"] = heatmap_data["month_period"].astype(str)

heatmap_pivot = heatmap_data.pivot(
    index="category",
    columns="month_period",
    values="total_spent"
).fillna(0)

fig_heatmap = px.imshow(
    heatmap_pivot,
    aspect="auto",
    title="Monthly Revenue by Category",
    labels={"x": "Month", "y": "Category", "color": "Revenue"},
    color_continuous_scale=["#141A40", VIOLET, PINK, AMBER]
)
st.plotly_chart(style_fig(fig_heatmap), use_container_width=True)


# ============================================================
# TOP ITEMS
# ============================================================

section_header("Top Performing Items")

item_revenue = (
    filtered_df
    .groupby("item")["total_spent"]
    .sum()
    .reset_index()
    .sort_values("total_spent", ascending=False)
    .head(10)
)

fig_items = px.bar(
    item_revenue,
    x="total_spent",
    y="item",
    orientation="h",
    title="Top 10 Items by Revenue",
    text_auto=".2s",
    color="total_spent",
    color_continuous_scale=[CYAN, VIOLET, PINK]
)
fig_items.update_layout(
    xaxis_title="Revenue (₹)",
    yaxis_title="Item",
    yaxis={"categoryorder": "total ascending"},
    coloraxis_showscale=False
)
st.plotly_chart(style_fig(fig_items), use_container_width=True)


# ============================================================
# YEARLY PERFORMANCE
# ============================================================

section_header("Yearly Performance")

yearly_data = (
    filtered_df
    .groupby("year")
    .agg(
        Revenue=("total_spent", "sum"),
        Transactions=("transaction_id", "nunique"),
        Customers=("customer_id", "nunique"),
        Quantity=("quantity", "sum")
    )
    .reset_index()
)
yearly_data["year"] = yearly_data["year"].astype("Int64").astype(str)

fig_year = px.bar(
    yearly_data,
    x="year",
    y="Revenue",
    text_auto=".2s",
    title="Revenue by Year",
    color_discrete_sequence=[VIOLET]
)
fig_year.update_layout(xaxis_title="Year", yaxis_title="Revenue (₹)")
st.plotly_chart(style_fig(fig_year), use_container_width=True)


# ============================================================
# CUSTOMER ANALYSIS
# ============================================================

section_header("Customer Analysis")

customer_data = (
    filtered_df
    .groupby("customer_id")
    .agg(
        Total_Spent=("total_spent", "sum"),
        Transactions=("transaction_id", "nunique"),
        Quantity=("quantity", "sum")
    )
    .reset_index()
    .sort_values("Total_Spent", ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**🏆 Top Customers**")
    st.dataframe(
        customer_data.head(10),
        use_container_width=True,
        hide_index=True
    )

with col2:
    fig_customer = px.scatter(
        customer_data,
        x="Transactions",
        y="Total_Spent",
        size="Quantity",
        hover_name="customer_id",
        title="Customer Spending vs Transactions",
        color="Total_Spent",
        color_continuous_scale=[CYAN, VIOLET, PINK]
    )
    fig_customer.update_layout(coloraxis_showscale=False)
    st.plotly_chart(style_fig(fig_customer), use_container_width=True)


# ============================================================
# DATA QUALITY
# ============================================================

section_header("Data Quality Overview")

quality_col1, quality_col2, quality_col3 = st.columns(3)

with quality_col1:
    st.metric("Rows", f"{len(filtered_df):,}")

with quality_col2:
    st.metric("Columns", f"{len(filtered_df.columns):,}")

with quality_col3:
    st.metric("Missing Values", f"{int(filtered_df.isnull().sum().sum()):,}")


# ============================================================
# DATA PREVIEW
# ============================================================

st.write("")

with st.expander("📋 View Dataset"):
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# DATASET NOTE
# ============================================================

st.info(
    """
    **Dashboard Data Note**

    The dataset contains transaction, customer, category, item,
    payment, date, quantity, revenue and discount information.

    Customer Acquisition Cost (CAC) and Churn Rate cannot be
    calculated from this dataset because acquisition-cost and
    customer-churn fields are not present.

    Geographic heatmaps are also not included because the
    `location`/geographic field is not available in this
    15-column dataset.
    """
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    f'<div class="footer"><b>{APP_NAME}</b> · Built with Streamlit &amp; Plotly</div>',
    unsafe_allow_html=True
)
