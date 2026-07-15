# Reaction Kinetics Analyzer

## Overview

RC1e Reactor Designer is a chemical reaction engineering software developed using **Python** and **Streamlit** for processing RC1e calorimetry experiments, estimating reaction kinetics, and assisting reactor design.

The software converts raw RC1e calorimetric data into useful engineering parameters including:

* Heat Release
* Conversion
* Reactant Concentration
* Reaction Rate
* Reaction Order
* Rate Constant
* Reactor Volume
* Residence Time
* Expected Conversion

The objective of this project is to automate the complete workflow from RC1e experimental data to reactor design calculations using a transparent, physics-based methodology.

---

# Features

### Data Validation

* Validates uploaded Excel files
* Checks mandatory columns
* Detects missing values
* Detects duplicate time points
* Ensures increasing time sequence
* Verifies numeric data

---

### Thermodynamic Analysis

Automatically calculates:

* Heat Flow Integration
* Cumulative Heat Released
* Reaction Heat Profile

---

### Conversion Calculation

Calculates reaction conversion using calorimetric heat release.

Outputs:

* Instantaneous Conversion
* Final Conversion

---

### Concentration Calculation

Calculates reactant concentrations throughout the experiment.

Outputs include:

* Concentration of Reactant A
* Concentration of Reactant B

---

### Reaction Rate Calculation

Calculates reaction rate using concentration profiles.

Outputs:

* Reaction Rate (mol/L/min)

---

### Kinetic Parameter Estimation

Uses nonlinear regression to estimate kinetic parameters.

Calculates:

* Reaction Order (n)
* Rate Constant (k)
* Model R²
* RMSE

Current kinetic model:

Rate = k × CAⁿ

---

### Reactor Designer

Allows users to design a Plug Flow Reactor (PFR).

User Inputs:

* Reactor Diameter
* Reactor Length
* Flow Rate
* Operating Temperature
* Activation Energy

Software Calculates:

* Reactor Volume
* Residence Time
* Temperature Corrected Rate Constant
* Expected Conversion

---

### Interactive Visualizations

The software generates:

* Conversion vs Time
* Concentration vs Time
* Reaction Rate vs Time

---

# Software Workflow

```
Upload RC1e Excel
        │
        ▼
Data Validation
        │
        ▼
Thermodynamic Analysis
        │
        ▼
Conversion Calculation
        │
        ▼
Concentration Calculation
        │
        ▼
Reaction Rate Calculation
        │
        ▼
Kinetic Parameter Estimation
        │
        ▼
Reactor Design
        │
        ▼
Results & Plots
```

---

# Project Structure

```
RC1e_Reactor_Designer/

│
├── streamlit_app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── excel_reader.py
│   ├── validator.py
│   ├── thermodynamics.py
│   ├── conversion.py
│   ├── concentration.py
│   ├── rate_calculator.py
│   ├── kinetics.py
│   ├── reactor.py
│   └── plots.py
│
└── sample_data/
    └── SAP_001_RC1e_Gold_Standard.xlsx
```

---

# Input Excel Format

The software requires an Excel workbook containing two sheets.

## Sheet 1 — Experiment_Info

Typical information includes:

* Reaction Name
* Initial Volume
* Initial Concentration of Reactant A
* Initial Concentration of Reactant B
* Heat of Reaction
* Density

---

## Sheet 2 — RC1_Data

Required columns:

* Time(min)
* Reactor_Temperature(C)
* Jacket_Temperature(C)
* HeatFlow(W)
* Pressure(bar)

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your_username/RC1e_Reactor_Designer.git

cd RC1e_Reactor_Designer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
streamlit run streamlit_app.py
```

---

# Deployment

The application can be deployed using:

* Streamlit Community Cloud
* Docker
* Azure
* AWS
* Google Cloud Platform

---

# Software Dependencies

* Streamlit
* Pandas
* NumPy
* SciPy
* Plotly
* OpenPyXL
* Scikit-Learn

---

# Current Limitations

Current Version supports:

* Single RC1e experiment
* Plug Flow Reactor (PFR)
* Constant density assumption
* Isothermal reactor design

The software currently uses one experiment to estimate kinetic parameters. More advanced kinetic analysis requires experiments performed at multiple temperatures.

---

# Planned Improvements

Future versions will include:

* Automatic Arrhenius parameter estimation
* Multiple RC1e experiment support
* Batch Reactor Design
* Continuous Stirred Tank Reactor (CSTR) Design
* Plug Flow Reactor with temperature-dependent kinetics
* Energy balance calculations
* Pressure drop estimation
* Reactor sizing optimization
* Automatic PDF report generation
* Excel report export
* Interactive engineering dashboard
* Sensitivity analysis
* Parameter uncertainty estimation

---

# Engineering Applications

This software can be used for:

* Reaction kinetics estimation
* Process development
* Process safety studies
* Laboratory scale-up
* Pilot plant design
* Reactor sizing
* Residence time estimation
* Conversion prediction
* Chemical process optimization

---

# Disclaimer

This software is intended for educational, research, and preliminary engineering calculations.

All reactor designs should be independently verified using appropriate engineering practices before industrial implementation.

---

# Author

**Ankit Yadav**

Chemical Engineering | Reaction Engineering | Process Development | Python | Data Analytics

---

# Version

Current Release:

**Version 1.0**
