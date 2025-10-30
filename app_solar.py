import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from itertools import combinations
import numpy as np

st.set_page_config(
    page_title="Solar Energy Vietnam",
    page_icon="🌞",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
    <style>
    /* Main content - white background */
    .main {
        background-color: #ffffff;
    }
    .stApp {
        max-width: 100%;
        background-color: #ffffff;
    }
    
    /* Navigation bar - black background white text */
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-right: 1px solid #333;
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] strong {
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] .stRadio > label {
        color: #ffffff !important;
        font-weight: 500;
    }
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #ffffff !important;
        font-weight: 600;
    }
    [data-testid="stSidebar"] hr {
        border-color: #444;
    }
    
    /* Radio buttons in sidebar */
    [data-testid="stSidebar"] .stRadio > div {
        background-color: transparent;
    }
    [data-testid="stSidebar"] .stRadio label {
        padding: 8px 12px;
        border-radius: 5px;
        transition: all 0.2s;
    }
    [data-testid="stSidebar"] .stRadio label:hover {
        background-color: #333;
    }
    
    /* Main headings - BOLD and CLEAR */
    h1 {
        color: #000000 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
        margin-bottom: 1rem;
        font-size: 2.5rem !important;
    }
    h2 {
        color: #000000 !important;
        font-weight: 700 !important;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        font-size: 1.8rem !important;
    }
    h3 {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 1.4rem !important;
    }
    h4 {
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
    }
    
    /* Text in main content */
    .main p, .main li, .main label, .main span, .main div {
        color: #000000;
        font-weight: 500;
        line-height: 1.7;
    }
    
    .reportview-container .main .block-container {
        padding: 2.5rem 3.5rem;
    }
    
    /* Fix for selectbox, multiselect - ensure white background black text */
    .stSelectbox, .stMultiSelect {
        color: #000000 !important;
    }
    .stSelectbox > div > div,
    .stMultiSelect > div > div {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    .stSelectbox label,
    .stMultiSelect label {
        color: #000000 !important;
        font-weight: 600;
    }
    .stSelectbox input,
    .stMultiSelect input,
    .stSelectbox select,
    .stMultiSelect select {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    /* Dropdown options */
    [role="option"],
    [role="listbox"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    [role="option"] * {
        color: #000000 !important;
    }
    [data-baseweb="select"] > div,
    [data-baseweb="select"] div,
    [data-baseweb="select"] span,
    [data-baseweb="popover"],
    [data-baseweb="popover"] div {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    /* Menu dropdown */
    ul[role="listbox"] {
        background-color: #ffffff !important;
    }
    ul[role="listbox"] li {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    ul[role="listbox"] li:hover {
        background-color: #f0f0f0 !important;
    }
    
    /* Slider */
    .stSlider label {
        color: #000000 !important;
        font-weight: 600;
    }
    .stSlider div[data-testid="stTickBar"] {
        color: #000000 !important;
    }
    
    /* Metrics - highlighted */
    div[data-testid="stMetricValue"] {
        font-size: 32px;
        color: #000000 !important;
        font-weight: 700;
    }
    div[data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    /* Fix for all text in metrics */
    [data-testid="stMetric"] * {
        color: #000000 !important;
    }
    [data-testid="stMetric"] label {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricLabel"] > div {
        color: #000000 !important;
    }
    
    /* Data tables */
    .dataframe {
        border: 1px solid #e0e0e0;
        border-radius: 5px;
    }
    
    /* Buttons and controls */
    .stButton>button {
        border-radius: 5px;
        font-weight: 600;
        border: 1px solid #ddd;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        border-color: #000;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Divider */
    hr {
        margin: 2rem 0;
        border-color: #e0e0e0;
    }
    
    /* Markdown content */
    .stMarkdown {
        color: #000000;
    }
    
    /* Create elevation effect for sections */
    .element-container {
        transition: all 0.2s;
    }
    
    /* Remove extra whitespace at end of page */
    .main > div:last-child {
        padding-bottom: 0 !important;
        margin-bottom: 0 !important;
    }
    .block-container {
        padding-bottom: 1rem !important;
    }
    footer {
        visibility: hidden;
        height: 0;
        margin: 0;
        padding: 0;
    }
    /* Ensure no excess scroll */
    .main .block-container > div:last-child {
        margin-bottom: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    monthly = pd.read_csv("solar_monthly_vietnam_full.csv")
    annual = pd.read_csv("solar_annual_vietnam_full.csv")
    
    monthly['YearMonth'] = pd.to_datetime(monthly['YearMonth'])
    
    annual['Year'] = annual['Year'].astype(int)
    monthly['Year'] = monthly['Year'].astype(int)
    
    return monthly, annual

monthly_df, annual_df = load_data()

st.sidebar.subheader("NAVIGATION MENU")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Select content:",
    [
        "Home",
        "1. Radiation Distribution",
        "2. Time Trends",
        "3. Geographic Location",
        "4. Climate Correlation",
        "5. Composite Map",
        "6. Potential energy network",
        "7. Conclusion"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Project:** Solar Energy: Solar Radiation and Solar Power Potential in Vietnam

**Data Source:** NASA POWER API (2015-2024)
""")

if menu == "Home":
    st.title("SOLAR ENERGY")
    st.header("Solar Radiation and Solar Power Potential in Vietnam")
    
    st.subheader("Project Story")
    
    st.write("""
    **"How much 'solar power' does Vietnam receive annually – and which region has the most energy?"**
    
    Solar energy is becoming one of the most important renewable energy sources for Vietnam's future. 
    With its favorable geographic location near the equator, Vietnam receives abundant solar radiation year-round.
    
    This study analyzes data from NASA POWER API during the period 2015-2024, surveying **12 provinces** 
    representing different climate regions of Vietnam to answer the questions:
    
    - How is solar radiation distributed among provinces?
    - How does solar energy trend change over the years?
    - Does latitude affect the amount of solar radiation?
    - What climate factors impact solar energy?
    - Which region has the greatest solar power potential?
    """)
    
    st.markdown("---")
    
    st.subheader("Overall Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Provinces Surveyed",
            value=len(monthly_df['Province'].unique())
        )
    
    with col2:
        st.metric(
            label="Time Period",
            value="2015-2024"
        )
    
    with col3:
        avg_ghi = monthly_df['GHI_kWh_m2_day'].mean()
        st.metric(
            label="Average GHI",
            value=f"{avg_ghi:.2f} kWh/m²/day"
        )
    
    with col4:
        max_province = monthly_df.groupby('Province')['GHI_kWh_m2_day'].mean().idxmax()
        st.metric(
            label="Highest Energy Province",
            value=max_province
        )
    
    st.markdown("---")
    
    st.subheader("What is GHI (Global Horizontal Irradiance)?")
    
    st.write("""
    **GHI** is the total amount of solar radiation incident on a horizontal surface on the ground, 
    including both direct and diffuse radiation. Unit of measurement: **kWh/m²/day**.
    
    GHI is the most important indicator for assessing the solar energy potential of an area.
    The higher the GHI value, the greater the solar power generation potential.
    """)
    
    st.markdown("---")
    
    st.subheader("Surveyed Provinces")
    
    provinces_info = monthly_df.groupby('Province').agg({
        'Lat': 'first',
        'Lon': 'first',
        'GHI_kWh_m2_day': 'mean'
    }).reset_index()
    provinces_info = provinces_info.sort_values('GHI_kWh_m2_day', ascending=False)
    provinces_info['GHI_kWh_m2_day'] = provinces_info['GHI_kWh_m2_day'].round(2)
    provinces_info.columns = ['Province', 'Latitude', 'Longitude', 'Average GHI (kWh/m²/day)']
    
    st.dataframe(
        provinces_info,
        use_container_width=True,
        hide_index=True
    )

elif menu == "1. Radiation Distribution":
    st.title("SOLAR RADIATION DISTRIBUTION")
    
    df_hist = annual_df.copy()
    df_hist = df_hist.rename(columns={
        "Province": "Province",
        "GHI_kWh_m2_day": "Average Radiation (kWh/m²/day)",
        "GHI_Annual_kWh_m2_year": "Annual Total Energy (kWh/m²/year)"
    })
    
    fig = px.histogram(
        df_hist,
        x="Average Radiation (kWh/m²/day)",
        color="Province",
        nbins=25,
        hover_data=["Year"],
        title="Distribution of Average Solar Radiation Among Vietnamese Provinces (2015–2024)",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    fig.update_layout(
        xaxis_title="Average Solar Radiation Level (kWh/m²/day)",
        yaxis_title="Number of Months in Period 2015-2024",
        legend_title_text="Province",
        template="plotly_white",
        title_x=0.5,
        height=600,
        font=dict(size=13)
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif menu == "2. Time Trends":
    st.title("SOLAR RADIATION TRENDS OVER TIME")
    
    df_annual = annual_df[annual_df["Year"] >= 2015].copy()
    df_annual["Year"] = df_annual["Year"].astype(int)
    
    all_provinces = sorted(df_annual['Province'].unique())
    selected_provinces = st.multiselect(
        "Select provinces to compare:",
        options=all_provinces,
        default=all_provinces
    )
    
    if selected_provinces:
        df_filtered = df_annual[df_annual['Province'].isin(selected_provinces)]
    else:
        df_filtered = df_annual
    
    fig = px.line(
        df_filtered,
        x="Year",
        y="GHI_kWh_m2_day",
        color="Province",
        markers=True,
        hover_data={"Year": True, "GHI_kWh_m2_day": ':.2f', "Province": True},
        title="☀️ Average Solar Radiation (GHI) Trend Over Time 2015–2024",
    )
    
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Average Radiation (kWh/m²/day)",
        legend_title="Province",
        template="plotly_white",
        hovermode="x unified",
        height=600,
        title_x=0.5,
        font=dict(size=13)
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif menu == "3. Geographic Location":
    st.title("RELATIONSHIP BETWEEN GEOGRAPHIC LOCATION AND SOLAR RADIATION")
    
    geo_summary = (
        monthly_df.groupby(["Province", "Lat", "Lon"])
        .agg({"GHI_kWh_m2_day": "mean"})
        .reset_index()
    )
    
    fig = px.scatter(
        geo_summary,
        x="Lat",
        y="GHI_kWh_m2_day",
        text="Province",
        color="GHI_kWh_m2_day",
        color_continuous_scale="YlOrRd",
        hover_data={"Province": True, "Lat": ':.2f', "Lon": ':.2f', "GHI_kWh_m2_day": ':.2f'},
        title="📍 Relationship Between Latitude and Average Solar Radiation in Vietnam",
        trendline="ols"
    )
    
    fig.update_traces(textposition="top center", marker=dict(size=15))
    fig.update_layout(
        xaxis_title="Latitude (°N)",
        yaxis_title="Average Radiation (kWh/m²/day)",
        coloraxis_colorbar_title="GHI<br>(kWh/m²/day)",
        template="plotly_white",
        height=600,
        title_x=0.5,
        font=dict(size=13)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.write("""
    **Observation:** Southern provinces (lower latitude) receive significantly higher solar radiation compared to the North, 
    showing that geographic location plays a crucial role in solar energy development potential.
    """)

elif menu == "4. Climate Correlation":
    st.title("CORRELATION BETWEEN CLIMATE FACTORS AND SOLAR RADIATION")
    
    df_corr = monthly_df.rename(columns={
        "GHI_kWh_m2_day": "Solar Radiation (kWh/m²/day)",
        "T2M": "Avg Temperature (°C)",
        "RH2M": "Avg Humidity (%)",
        "WS2M": "Wind Speed (m/s)",
        "PRECTOT": "Precipitation (mm)"
    })
    
    cols = [
        "Solar Radiation (kWh/m²/day)",
        "Avg Temperature (°C)",
        "Avg Humidity (%)",
        "Wind Speed (m/s)",
        "Precipitation (mm)"
    ]
    
    corr = df_corr[cols].corr(method="pearson")
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        center=0,
        fmt=".2f",
        linewidths=0.5,
        cbar_kws={"shrink": 0.8, "label": "Correlation Coefficient (r)"},
        annot_kws={"size": 12},
        ax=ax,
        vmin=-1,
        vmax=1
    )
    
    plt.title(
        "Correlation Matrix Between Climate Factors and Solar Energy\nin Vietnam (2015–2024)",
        fontsize=14, pad=20, fontweight='bold'
    )
    plt.xticks(rotation=45, ha="right", fontsize=11)
    plt.yticks(rotation=0, fontsize=11)
    plt.tight_layout()
    
    st.pyplot(fig)

elif menu == "5. Composite Map":
    st.title("SOLAR ENERGY POTENTIAL DISTRIBUTION MAP")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        year_filter = st.selectbox(
            "Select year to view:",
            options=['All Years'] + sorted(monthly_df['Year'].dropna().unique().astype(int).tolist()),
            index=0
        )
    
    with col2:
        month_filter = st.selectbox(
            "Select month:",
            options=['All Months'] + list(range(1, 13)),
            index=0
        )
    
    df_map = monthly_df.copy()
    
    if year_filter != 'All Years':
        df_map = df_map[df_map['Year'] == year_filter]
    
    if month_filter != 'All Months':
        df_map = df_map[df_map['Month'] == month_filter]
    
    df_map = df_map.dropna(subset=["Lat", "Lon", "GHI_kWh_m2_day"])
    df_map_agg = df_map.groupby(['Province', 'Lat', 'Lon']).agg({
        'GHI_kWh_m2_day': 'mean',
        'T2M': 'mean',
        'RH2M': 'mean'
    }).reset_index()
    
    fig = px.scatter_mapbox(
        df_map_agg,
        lat="Lat",
        lon="Lon",
        color="GHI_kWh_m2_day",
        size="GHI_kWh_m2_day",
        hover_name="Province",
        color_continuous_scale=px.colors.sequential.YlOrRd,
        size_max=30,
        zoom=5,
        height=750,
        mapbox_style="open-street-map",
        title="☀️ Solar Energy Potential Distribution in Vietnam",
        hover_data={
            "Lat": ':.2f',
            "Lon": ':.2f',
            "GHI_kWh_m2_day": ':.2f',
            "T2M": ':.1f',
            "RH2M": ':.1f'
        },
        labels={
            "GHI_kWh_m2_day": "Radiation (kWh/m²/day)",
            "T2M": "Temperature (°C)",
            "RH2M": "Humidity (%)"
        }
    )
    
    fig.update_layout(
        title_font=dict(size=20, family="Arial", color="#333"),
        title_x=0.5,
        paper_bgcolor="white",
        margin=dict(l=0, r=0, t=60, b=0),
        coloraxis_colorbar=dict(
            title="Irradiance<br>(kWh/m²/day)",
            ticks="outside",
            tickmode='auto'
        ),
        font=dict(size=12)
    )
    
    st.plotly_chart(
        fig, 
        use_container_width=True,
        config={
            'scrollZoom': True,
            'displaylogo': False,
            'modeBarButtonsToRemove': ['lasso2d', 'select2d'],
            'displayModeBar': True
        }
    )
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        max_ghi_province = df_map_agg.loc[df_map_agg['GHI_kWh_m2_day'].idxmax(), 'Province']
        max_ghi_value = df_map_agg['GHI_kWh_m2_day'].max()
        st.metric(
            "Highest Province",
            max_ghi_province,
            f"{max_ghi_value:.2f} kWh/m²/day"
        )
    
    with col2:
        min_ghi_province = df_map_agg.loc[df_map_agg['GHI_kWh_m2_day'].idxmin(), 'Province']
        min_ghi_value = df_map_agg['GHI_kWh_m2_day'].min()
        st.metric(
            "Lowest Province",
            min_ghi_province,
            f"{min_ghi_value:.2f} kWh/m²/day"
        )
    
    with col3:
        avg_ghi = df_map_agg['GHI_kWh_m2_day'].mean()
        st.metric(
            "Average",
            f"{avg_ghi:.2f}",
            "kWh/m²/day"
        )

elif menu == "6. Potential energy network":
    st.title("NETWORK GRAPH - CONNECTIONS OF HIGH RADIATION PROVINCES")
    
    threshold = st.slider(
        "Select GHI threshold (kWh/m²/day):",
        min_value=10,
        max_value=20,
        value=17,
        step=1,
        help="Only provinces with GHI > this threshold will be connected"
    )
    
    monthly = monthly_df.copy()
    months = monthly['YearMonth'].unique()
    G = nx.Graph()
    
    provinces = list(monthly['Province'].unique())
    for p in provinces:
        G.add_node(p)
    
    for m in months:
        m_data = monthly[(monthly['YearMonth'] == m) & (monthly['GHI_kWh_m2_day'] > threshold)]
        selected_prov = m_data['Province'].tolist()
        
        for u, v in combinations(selected_prov, 2):
            if G.has_edge(u, v):
                G[u][v]['weight'] += 1
            else:
                G.add_edge(u, v, weight=1)
    
    fig, ax = plt.subplots(figsize=(14, 10))
    pos = nx.spring_layout(G, seed=42, k=1.5, iterations=50)
    
    nx.draw_networkx_nodes(
        G, pos,
        node_color='#FFD700',
        node_size=1500,
        alpha=0.9,
        edgecolors='#FF6B35',
        linewidths=2
    )
    
    nx.draw_networkx_labels(
        G, pos,
        font_size=11,
        font_weight='bold',
        font_family='Arial'
    )
    
    edges = G.edges()
    if edges:
        weights = [G[u][v]['weight'] for u, v in edges]
        max_weight = max(weights) if weights else 1
        
        nx.draw_networkx_edges(
            G, pos,
            edge_color=weights,
            edge_cmap=plt.cm.Blues,
            width=[w/5 + 1 for w in weights],
            edge_vmin=1,
            edge_vmax=max_weight,
            alpha=0.7
        )
        
        sm = plt.cm.ScalarMappable(
            cmap=plt.cm.Blues,
            norm=plt.Normalize(vmin=1, vmax=max_weight)
        )
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=ax, shrink=0.8)
        cbar.set_label('Months Exceeding Threshold Together', fontsize=12)
    
    plt.title(
        f'Network of Provinces with GHI > {threshold} kWh/m²/day (2015-2024)',
        fontsize=16,
        fontweight='bold',
        pad=20
    )
    plt.axis('off')
    plt.tight_layout()
    
    st.pyplot(fig)

elif menu == "7. Conclusion":
    st.title("CONCLUSION")
    
    st.subheader("Key Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**1. Radiation Distribution**")
        st.write("• Ninh Thuan and Binh Thuan lead with GHI >18 kWh/m²/day")
        st.write("• Northern region has GHI 40-50% lower than the South")
        
        st.write("\n**2. Time Trends**")
        st.write("• GHI stable over 10 years (2015-2024)")
        st.write("• Fluctuation ±5-10%, possibly due to El Niño/La Niña")
    
    with col2:
        st.write("**3. Geographic Location**")
        st.write("• Latitude has strong negative correlation with GHI")
        st.write("• Southern region has natural advantage in solar energy")
        
        st.write("\n**4. Climate Factors**")
        st.write("• Temperature: positive correlation with GHI")
        st.write("• Humidity and precipitation: negative correlation with GHI")
    
    st.markdown("---")
    
    st.subheader("Recommendations")
    
    st.write("""
    **Development Priority:** Ninh Thuan, Binh Thuan and South Central Coast - suitable for large-scale solar power.
    
    **Rooftop Solar:** Encourage in major cities (HCMC, Hanoi, Da Nang).
    
    **Multi-source Integration:** Northern region should combine solar with wind and hydropower to increase stability.
    """)
    
    st.markdown("---")
    
    st.subheader("Final Words")
    
    st.write("""
    Vietnam has **great solar energy potential**, especially in the South and South Central Coast. 
    With abundant and stable solar radiation, solar energy can become a 
    **primary energy source** in the future, contributing to emission reduction, 
    environmental protection and sustainable green economic development.
    
    """)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 12px;'>
    <p>© 2024 - Solar Energy Analysis Vietnam | Developed using Streamlit</p>
</div>
""", unsafe_allow_html=True)

