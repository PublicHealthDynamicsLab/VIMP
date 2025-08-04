# README: Influenza Agent-Based Model

This document provides an overview of the [FRED](https://github.com/PublicHealthDynamicsLab/FRED)-based agent-based model (ABM) for simulating influenza transmission dynamics.

-----

## Table of Contents

* [📝 Model Overview](#-model-overview)
* [📂 Model Components](#-model-components)
* [🔬 Simulation Scenarios & Interventions](#-simulation-scenarios--interventions)
    * [Negative Interventions (Decreased Vaccination)](#negative-interventions-decreased-vaccination)
    * [Positive Interventions (Increased Vaccination)](#positive-interventions-increased-vaccination)
* [⚙️ Key Parameters & Calibration](#️-key-parameters--calibration)
    * [Disease Transmission](#disease-transmission)
    * [Vaccination](#vaccination)
    * [Immunity](#immunity)
    * [Behavioral Response](#behavioral-response)
* [🚀 Running the Model & Analysis Approach](#-running-the-model--analysis-approach)
* [📊 Data Sources](#-data-sources)
  
-----

## 📝 Model Overview

This ABM, built using the FRED (Framework for Reconstructing Epidemic Dynamics) programming language, simulates the spread of H3N2 influenza within a synthetic population. The model is based on previous research investigating vaccine efficacy and uptake. It simulates the population of Allegheny County, Pennsylvania (N=1,218,695) using a 2010 U.S. Census-derived synthetic population dataset. The simulation period runs from August 15, 2023, to August 9, 2024.

The model incorporates several modules to create a realistic simulation environment:

  * Disease progression and transmission
  * Seasonality of transmission
  * Pre-existing immunity
  * Vaccination
  * Behavioral responses (e.g., staying home when sick)
  * Scheduled school closures
  * Detailed tracking of outcomes by demographic groups

-----

## 📂 Model Components

The model is comprised of several FRED files, each responsible for a specific aspect of the simulation:

  * **`influenzamodel.fred`**: The main model file used to run a FRED job. It contains global and personal variables for the flu type being modeled and allows for the inclusion of "accessory models" like vaccination and school breaks.
  * **`flu.fred`**: The basic model for influenza.
  * **`antiviral_flu.fred`**: An alternative base model that includes the effect of antivirals, which can decrease hospitalization and death rates for a proportion of symptomatic individuals.
  * **`fluvaccine.fred`**: The base model for vaccination, where parameters such as vaccination proportion, timing, and waning of protection can be adjusted.
  * **`IMMUNITY.fred`**: This model administers a distribution of pre-existing immunity in the population and wanes that immunity over time.
  * **`GROUP.fred`**: Tracks infections, hospitalizations, and deaths by CDC age groups.
  * **`TRACK.fred`**: Tracks the combined vaccination and infection status of agents, including breakthrough infections.
  * **`WHERE.fred`**: Tracks the location of infection transmission, including Household, Neighborhood, School, Classroom, Workplace, Office, and external locations.
  * **`breaks.fred`**: This model handles school closures for winter, spring, and summer breaks, with adjustable dates.

-----

## 🔬 Simulation Scenarios & Interventions

The primary outcomes of this study are the cumulative number of infections, symptomatic cases, hospitalizations, and deaths over a simulated influenza season. These outcomes are tracked for each simulation scenario and compared to a baseline to assess the impact of different interventions.

We simulated two main categories of interventions based on effect sizes reported in recent literature: those that decrease vaccination intent and uptake, and those that increase it. These interventions were modeled as changes to the age-specific vaccination coverage rates in the simulation.

### Negative Interventions (Decreased Vaccination)

  * **Misinformation Campaign (Intent):** Based on the findings of Loomba et al. (2021), this scenario reflects a significant decrease in the intent to vaccinate, implemented as an average absolute reduction of 6.2 percentage points in the vaccination coverage rate across age groups.
  * **Vaccine-Skeptical Content (Intent):** Informed by the work of Allen et al. (2023), this scenario applies a 2.3 percentage point absolute reduction in vaccination coverage for all age groups.

### Positive Interventions (Increased Vaccination)

  * **Normative Information Campaign (Intent):** Drawing from Moehring et al. (2022), this intervention was modeled as a 5-percentage-point reduction in the proportion of the population that is "unsure" about vaccination, with those individuals being moved to the "intending to vaccinate" group.
  * **Text-Based Nudges (Uptake):** Based on a megastudy by Milkman et al. (2021), this intervention was modeled as a 5% relative increase in the baseline vaccination coverage rates for all age groups.
  * **Pharmacy-Based Reminders (Uptake):** Based on a megastudy by Milkman et al. (2022), we simulated a scenario with a 2.0 percentage point absolute increase in the vaccination coverage rate across all age groups.

-----

## ⚙️ Key Parameters & Calibration

The baseline simulation model was calibrated to reflect realistic influenza transmission dynamics. The age-specific vaccination coverage rates for the 2023-2024 influenza season were obtained from the CDC: 55.4% for ages 6 months to 17 years, 32.8% for ages 18-49, 46.2% for ages 50-64, and 69.7% for those 65 and older. The vaccine effectiveness was set at 44%, also based on CDC estimates for the 2023-2024 season. Probabilities for hospitalization and mortality, stratified by age and vaccination status, were derived from published literature.

### Disease Transmission

  * **Transmissibility**: The base transmissibility is set to 0.75, which is typical for an H3N2-type influenza. Seasonality is implemented using a sinusoidal function that modifies daily transmissibility, peaking in winter and reaching a minimum in summer.
  * **Latent Period**: The time from exposure to becoming infectious follows a log-normal distribution with a mean of 1.9 and a standard deviation of 1.23 days.
  * **Infectious Period**: The duration of symptomatic and asymptomatic infectiousness follows a log-normal distribution with a mean of 5.0 and a standard deviation of 1.5 days.
  * **Asymptomatic Infections**: Individuals under 65 have a 25% chance of an asymptomatic infection, while those 65 and older are always symptomatic. Asymptomatic individuals are 50% as infectious as symptomatic individuals.

### Vaccination

  * **Vaccine Effectiveness (VE)**: The model assumes a baseline VE of 42%.
  * **Vaccination Timing**: Vaccination becomes available on September 16th. Eligible individuals receive the vaccine after a random delay of 1 to 45 days. Vaccine-induced immunity takes effect 14 days after vaccination.
  * **Vaccine Waning**: Vaccine-induced immunity wanes at a rate of 0.07 per month for those without prior immunity.

### Immunity

  * **Pre-existing Immunity**: A portion of the population begins with pre-existing immunity, with age-stratified estimates ranging from 4.32% to 25.08%. This immunity wanes over time, with susceptibility increasing by 0.03 per month.

### Behavioral Response

  * **Stay-at-Home Behavior**: Symptomatic individuals have a 40% probability of staying home from school or work.

-----

## 🚀 Running the Model & Analysis Approach

An agent-based model (ABM) using the [FRED (Framework for Reconstructing Epidemic Dynamics)](https://github.com/PublicHealthDynamicsLab/FRED) platform was employed to simulate the transmission of an H3N2-like influenza virus in a synthetic population representing Allegheny County, Pennsylvania. A baseline scenario was established using current age-specific influenza vaccination rates.

Each of the five intervention scenarios was then simulated by adjusting the baseline vaccination coverage rates according to the effect sizes detailed in the Interventions section. For each scenario, 100 simulations were run to account for stochastic variability. The resulting disease burden outcomes (infections, symptomatic cases, hospitalizations, and deaths) from each intervention scenario were then compared to the baseline to quantify the projected impact of these real-world phenomena on population health.

The `METHODS` shell script provides instructions for running the FRED simulation. The general command to execute a FRED job is:

```bash
fred_job -k <key> -p <model_file> -t <threads> -n <runs>
```

  * `fred_job`: The command to initiate a FRED simulation.
  * `-k <key>`: A unique key to identify the simulation run.
  * `-p <model_file>`: The main FRED model file (e.g., `influenzamodel.fred`).
  * `-t <threads>`: The number of processor threads to use for the simulation.
  * `-n <runs>`: The number of simulation runs to perform.

The `METHODS` script demonstrates how to run different scenarios by modifying the `cfac_params.fred` file with different vaccination rate parameters before executing the `fred_job` command.

-----

## 📊 Data Sources

The effect sizes for the simulated interventions were derived from the following studies:

  * Allen, J., et al. (2023). "Quantifying the impact of misinformation and vaccine-skeptical content on Facebook."
  * Loomba, S., et al. (2021). "Measuring the impact of COVID-19 vaccine misinformation on vaccination intent in the UK and USA."
  * Milkman, K. L., et al. (2021). "A megastudy of text-based nudges encouraging patients to get vaccinated at an upcoming doctor’s appointment."
  * Milkman, K. L., et al. (2022). "A 680,000-person megastudy of nudges to encourage vaccination in pharmacies."
  * Moehring, A., et al. (2022). "Providing normative information increases intentions to accept a COVID-19 vaccine."

Additional data sources include:

  * **2010 U.S. Census-derived synthetic population dataset**: Used to model the population of Allegheny County, PA.
  * **CDC's estimated 2019-2020 disease burden**: Used to estimate pre-existing immunity levels.
  * **CDC's VE estimates for the 2023-2024 season**: Used to determine vaccine effectiveness.
  * **National Immunization Survey-Flu (NIS-Flu) and the Behavioral Risk Factor Surveillance System (BRFSS)**: The `experiment_readme.txt` file indicates that influenza vaccination coverage data was obtained from these sources.

### Data Source Links from Model Files

The following links to data sources are embedded within the model's `.fred` files:

  * **Hospitalization Rates (Adults)**: [https://academic.oup.com/cid/advance-article/doi/10.1093/cid/ciad677/7456016](https://academic.oup.com/cid/advance-article/doi/10.1093/cid/ciad677/7456016)
  * **Hospitalization Rates (Children)**: [https://academic.oup.com/cid/article/73/9/1722/6193428](https://academic.oup.com/cid/article/73/9/1722/6193428)
  * **Decreased Death Rates for Vaccinated Individuals**: [https://www.sciencedirect.com/science/article/pii/S0264410X21005624?dgcid=author](https://www.sciencedirect.com/science/article/pii/S0264410X21005624?dgcid=author)
  * **Stay-at-Home Behavior**: [https://wwwnc.cdc.gov/eid/article/26/1/19-0743\_article](https://wwwnc.cdc.gov/eid/article/26/1/19-0743_article)
  * **Prior Immunity (H3N2)**: [https://www.cdc.gov/flu/about/burden/2019-2020.html](https://www.cdc.gov/flu/about/burden/2019-2020.html)
  * **Antiviral Effects**:
      * **Consultation Rates for Influenza**: [https://doi.org/10.1017/S0950268800050779](https://doi.org/10.1017/S0950268800050779)
      * **Antiviral Prescription Rates**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6557305/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6557305/)
      * **Reduced Symptom Duration**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6464969/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6464969/)
      * **Reduced Hospitalization and Death Risk**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6637757/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6637757/)
  * **Influenza Vaccination Coverage**: [https://data.cdc.gov/Flu-Vaccinations/Influenza-Vaccination-Coverage-for-All-Ages-6-Mont/vh55-3he6/about\_data](https://data.cdc.gov/Flu-Vaccinations/Influenza-Vaccination-Coverage-for-All-Ages-6-Mont/vh55-3he6/about_data)
