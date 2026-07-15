import streamlit as st
import time

from modules.excel_reader import ExcelReader
from modules.validator import DataValidator
from modules.thermodynamics import Thermodynamics
from modules.conversion import Conversion
from modules.concentration import Concentration
from modules.rate_calculator import RateCalculator
from modules.kinetics import Kinetics
from modules.plots import PlotGenerator
from modules.reactor import ReactorCalculator

st.set_page_config(
    page_title="Reaction Kinetics Analyzer",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================
# CUSTOM CSS
# ===========================

st.markdown("""
<style>

.main{
    background-color:#f5f7fb;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:18px;
    border:1px solid #dcdcdc;
    box-shadow:0px 3px 8px rgba(0,0,0,0.08);
}

h1{
    color:#005792;
}

hr{
    margin-top:5px;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ===========================
# HEADER
# ===========================

st.markdown("""
# 🧪 Reaction Kinetics Analyzer

### Physics-Based Reaction Kinetics & Reactor Design Software
""")

# ===========================
# SIDEBAR
# ===========================

with st.sidebar:

    st.title("⚙ Control Panel")

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload RC1e Excel",
        type=["xlsx"]
    )

    st.markdown("---")

    st.header("🏭 Reactor Inputs")

    diameter = st.number_input(
        "Diameter (m)",
        value=0.05,
        min_value=0.001
    )

    length = st.number_input(
        "Length (m)",
        value=5.0
    )

    flowrate = st.number_input(
        "Flowrate (L/min)",
        value=2.0
    )

    operating_temperature = st.number_input(
        "Operating Temperature (°C)",
        value=25.0
    )

    activation_energy = st.number_input(
        "Activation Energy (kJ/mol)",
        value=55.0
    )

    st.markdown("---")

    st.info(
        "Version 1.0\n\n"
        "Developed by Ankit Yadav"
    )

# ===========================
# WAIT FOR FILE
# ===========================

if uploaded_file is None:

    st.info("👈 Upload an RC1e Excel file from the sidebar.")

    st.stop()

# ===========================
# SAVE FILE
# ===========================

with open("temp.xlsx","wb") as f:

    f.write(uploaded_file.getbuffer())

progress = st.progress(0)

status = st.empty()

# ===========================
# READ EXCEL
# ===========================

status.info("Reading Excel...")

reader = ExcelReader("temp.xlsx")

experiment, rc1_data = reader.read()

progress.progress(15)

# ===========================
# VALIDATE
# ===========================

status.info("Validating data...")

validator = DataValidator(
    experiment,
    rc1_data
)

errors = validator.validate()

if errors:

    st.error("Validation Failed")

    for e in errors:

        st.error(e)

    st.stop()

progress.progress(25)

# ===========================
# THERMODYNAMICS
# ===========================

status.info("Calculating thermodynamics...")

thermo = Thermodynamics(rc1_data)

rc1_data = thermo.calculate_cumulative_heat()

progress.progress(40)

# ===========================
# CONVERSION
# ===========================

status.info("Calculating conversion...")

conversion = Conversion(
    rc1_data,
    experiment
)

rc1_data = conversion.calculate()

progress.progress(55)

# ===========================
# CONCENTRATION
# ===========================

status.info("Calculating concentration...")

concentration = Concentration(
    rc1_data,
    experiment
)

rc1_data = concentration.calculate()

progress.progress(70)

# ===========================
# REACTION RATE
# ===========================

status.info("Calculating reaction rate...")

rate = RateCalculator(
    rc1_data
)

rc1_data = rate.calculate()

progress.progress(80)

# ===========================
# KINETICS
# ===========================

status.info("Estimating kinetics...")

kinetics = Kinetics(rc1_data)

results = kinetics.estimate()

reaction_order = results["Reaction Order"]

rate_constant = results["Rate Constant"]

r2 = results["R2"]

rmse = results["RMSE"]

progress.progress(90)

# ===========================
# REACTOR DESIGN
# ===========================

status.info("Designing reactor...")

reactor = ReactorCalculator(
    rate_constant,
    reaction_order
)

volume = reactor.reactor_volume(
    diameter,
    length
)

residence_time = reactor.residence_time(
    volume,
    flowrate
)

k_operating = reactor.arrhenius(
    activation_energy * 1000,
    25,
    operating_temperature
)

CA0 = experiment["Initial_EA_M"].iloc[0]

predicted_conversion = reactor.predict_conversion(
    CA0,
    residence_time,
    k_operating
)

progress.progress(100)

status.success("Analysis Completed Successfully!")

time.sleep(0.5)

progress.empty()

# ===========================
# KPI DASHBOARD
# ===========================

st.markdown("---")

st.subheader("📊 Reaction Kinetics Dashboard")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Reaction Order",
    f"{reaction_order:.3f}"
)

c2.metric(
    "Rate Constant",
    f"{rate_constant:.6f}"
)

c3.metric(
    "R²",
    f"{r2:.4f}"
)

c4.metric(
    "RMSE",
    f"{rmse:.6f}"
)

c5.metric(
    "Final Conversion",
    f"{rc1_data['Conversion'].iloc[-1]*100:.2f}%"
)

st.markdown("---")

# ===========================
# TABS
# ===========================

tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Process Analysis",
    "⚗ Kinetics",
    "🏭 Reactor Designer",
    "📋 Processed Data"
])

# ===========================
# TAB 1
# ===========================

with tab1:

    st.subheader("Conversion Profile")

    plots = PlotGenerator(rc1_data)

    st.plotly_chart(
        plots.conversion_plot(),
        use_container_width=True
    )

    st.subheader("Reactant Concentration")

    st.plotly_chart(
        plots.concentration_plot(),
        use_container_width=True
    )

    st.subheader("Reaction Rate")

    st.plotly_chart(
        plots.rate_plot(),
        use_container_width=True
    )

# ===========================
# TAB 2
# ===========================

with tab2:

    st.subheader("Estimated Kinetic Parameters")

    left, right = st.columns(2)

    with left:

        st.metric(
            "Reaction Order (n)",
            f"{reaction_order:.4f}"
        )

        st.metric(
            "Rate Constant (k)",
            f"{rate_constant:.6f}"
        )

    with right:

        st.metric(
            "Model R²",
            f"{r2:.4f}"
        )

        st.metric(
            "RMSE",
            f"{rmse:.6f}"
        )

    st.info(
        "Current kinetic model:\n\n"
        "Rate = k × CAⁿ"
    )

# ===========================
# TAB 3
# ===========================

with tab3:

    st.subheader("Reactor Design Results")

    r1, r2c = st.columns(2)

    with r1:

        st.metric(
            "Reactor Volume",
            f"{volume:.2f} L"
        )

        st.metric(
            "Residence Time",
            f"{residence_time:.2f} min"
        )

    with r2c:

        st.metric(
            "Operating k",
            f"{k_operating:.6f}"
        )

        st.metric(
            "Predicted Conversion",
            f"{predicted_conversion*100:.2f}%"
        )

    st.success(
        "Reactor calculations completed successfully."
    )
    # ===========================
# TAB 4
# ===========================

with tab4:

    st.subheader("Experiment Summary")

    try:

        st.dataframe(
            experiment,
            use_container_width=True
        )

    except:

        st.write(experiment)

    st.markdown("---")

    with st.expander("📋 View Processed RC1e Data", expanded=False):

        st.dataframe(
            rc1_data,
            use_container_width=True,
            height=500
        )

    csv = rc1_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Processed Data (.csv)",
        data=csv,
        file_name="Processed_RC1e_Data.csv",
        mime="text/csv"
    )

# ===========================
# ENGINEERING SUMMARY
# ===========================

st.markdown("---")

st.subheader("📑 Engineering Summary")

left, right = st.columns(2)

with left:

    st.markdown("### Reaction")

    st.write(f"**Reaction Order:** {reaction_order:.4f}")

    st.write(f"**Rate Constant:** {rate_constant:.6f}")

    st.write(f"**Operating Rate Constant:** {k_operating:.6f}")

    st.write(f"**Model R²:** {r2:.4f}")

    st.write(f"**RMSE:** {rmse:.6f}")

with right:

    st.markdown("### Reactor")

    st.write(f"**Volume:** {volume:.2f} L")

    st.write(f"**Residence Time:** {residence_time:.2f} min")

    st.write(
        f"**Predicted Conversion:** {predicted_conversion*100:.2f}%"
    )

    st.write(
        f"**Operating Temperature:** {operating_temperature:.1f} °C"
    )

# ===========================
# QUICK STATUS
# ===========================

st.markdown("---")

good = True

if r2 < 0.90:

    good = False

    st.warning(
        "Model fit is moderate. Additional experimental data may improve kinetic estimation."
    )

if predicted_conversion < 0.90:

    st.info(
        "Predicted conversion is below 90%. Consider increasing reactor volume, residence time, or operating temperature."
    )

if good:

    st.success(
        "Reaction kinetics successfully estimated and reactor design completed."
    )

# ===========================
# FOOTER
# ===========================

st.markdown("---")

st.markdown(
    """
<div style='text-align:center; color:grey;'>

### 🧪 Reaction Kinetics Analyzer

Physics-Based Reaction Kinetics & Reactor Design

Version 1.0

Developed by **Ankit Yadav**

</div>
""",
unsafe_allow_html=True
)