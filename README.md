Final Project Proposal<br>BU CS 506: Data Science Tools and Applications<br>Lance Galletti<br>Xinyu Li, Wenshou He, Benjamin Pfeiffer<br>Monday, February 10<sup>th</sup>, 2025

# Impact of Socioeconomic Factors on Cancer Incidence and Outcomes

## 1. Project Description

Cancer remains one of the leading causes of death worldwide, and multiple studies suggest that socioeconomic factors may play a role in cancer incidence and mortality rates. This project investigates the relationship between socioeconomic status and cancer rates by analyzing key variables such as median income and poverty levels across different U.S. counties.

The study aims to determine whether lower income levels correlate with higher cancer incidence and mortality rates and whether certain regions are disproportionately affected due to socioeconomic disparities. By leveraging statistical modeling techniques, this project will assess the strength and significance of these relationships.

---

## 2. Project Goals

The primary objectives of this study are:

- **Analyze the correlation** between socioeconomic factors and cancer rates
- **Determine the statistical significance** of income and poverty levels on cancer incidence and mortality
- **Apply hypothesis testing and regression models** to quantify relationships
- **Visualize findings** using effective data visualizations

---

## 3. Data Collection Plan

The data used in this study consists of county-level cancer rates and socioeconomic variables. The primary sources include:

- **Cancer incidence and mortality data** (e.g., obtained from the CDC, SEER database, or public health datasets)
- **Socioeconomic data** such as median household income and poverty rates (e.g., U.S. Census Bureau, American Community Survey)
- **Additional demographic and regional data** to control for potential confounding factors

If necessary, data will be preprocessed by cleaning missing values, normalizing numerical variables, and encoding categorical features.

---

## 4. Data Modeling Approach

To evaluate the impact of socioeconomic factors on cancer rates, the following methods will be implemented:

- **Linear Regression:** To model the relationship between median income/poverty levels and cancer rates
- **Hypothesis Testing** (e.g., Alexander-Govern Test): To determine if significant differences exist among different income groups
- **Correlation Analysis:** To assess how strongly different socioeconomic variables relate to cancer incidence and mortality
- **Potential Advanced Models:** If necessary, decision trees or machine learning approaches (e.g., XGBoost) may be explored

---

## 5. Data Visualization Plan

To effectively communicate the findings, the following visualizations will be used:

- **Scatter plots** to illustrate the correlation between cancer rates and socioeconomic variables
- **Bar charts** showing differences in cancer rates across income groups
- **Heatmaps** for correlation matrices to identify strong relationships
- **Geospatial visualizations** to highlight regional disparities

---

## 6. Test Plan

To validate the findings and ensure model robustness:

- Data will be split into **training (80%) and testing (20%) sets** for model validation
- **Cross-validation techniques** may be applied to prevent overfitting
- **Statistical significance testing** will be conducted to confirm findings
- If time permits, **sensitivity analysis** will be performed to check how different model assumptions impact the results.

---

## 7. Project Timeline (Two-Month Plan)

(Note: This is an initial plan and may be subject to changes based on data availability, unforeseen challenges, and project requirements.) A structured timeline is crucial to ensure project completion. Below is the proposed schedule:

### Week 1-2: Initial Setup and Data Collection
- Define research scope and finalize data sources
- Collect and preprocess data (clean missing values, normalize data, encode categorical features)
- Conduct exploratory data analysis (EDA) and generate descriptive statistics

### Week 3-4: Initial Modeling and Analysis
- Apply correlation analysis to identify key variables
- Implement initial linear regression and hypothesis testing
- Begin drafting preliminary visualizations

### Week 5-6: Model Refinement and Advanced Techniques
- Test alternative models (e.g., decision trees, XGBoost if needed)
- Conduct statistical significance tests
- Fine-tune models and perform feature selection

### Week 7: Finalization of Results and Interpretation
- Generate final visualizations
- Interpret and summarize findings
- Ensure reproducibility by refining code and data documentation

### Week 8: Report Writing and Presentation Preparation
- Write final project report summarizing methods, results, and conclusions
- Create a presentation with key insights and visualizations
- Conduct peer reviews and finalize all deliverables
