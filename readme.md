## Dataset Description

The dataset used in this project contains daily meteorological observations sourced from the **Indonesian Agency for Meteorology, Climatology, and Geophysics (BMKG)** via [Data Online BMKG](https://dataonline.bmkg.go.id/). 

The data containing **716 observations** from 01-04-2024 to 18-03-2026 at Stasiun Klimatologi DI Yogyakarta. It captures various atmospheric conditions, making it highly suitable for our target task: predicting the Average Relative Humidity (`RH_avg`).

### Data Dictionary

Below is the detailed description of the features available in the dataset:

| Column Name | Description | Unit / Format | Role in Model |
| :--- | :--- | :--- | :--- |
| `Tanggal` | Date of the weather observation | `DD-MM-YYYY` | Identifier / Time Series |
| `Tn` | Minimum Temperature | Celsius (°C) | Feature |
| `Tx` | Maximum Temperature | Celsius (°C) | Feature |
| `Tavg` | Average Temperature | Celsius (°C) | Feature |
| `RH_avg` | Average Relative Humidity | Percentage (%) | **Target Variable (y)** |
| `RR` | Rainfall / Precipitation | Millimeters (mm) | Feature |
| `SS` | Sunshine Duration | Hours / Percentage | Feature |
| `ff_x` | Maximum Wind Speed | m/s or Knots | Feature |
| `ddd_x` | Wind Direction at Maximum Speed | Degrees (°) | Feature |
| `ff_avg` | Average Wind Speed | m/s or Knots | Feature |
| `ddd_car` | Most Frequent Wind Direction | Cardinal / Degrees | Feature |

*Note: Some columns may contain missing values (represented as NaN or 8888 in standard BMKG raw data) which are handled during the Data Preprocessing phase of this project.*

---

### Acknowledgments & Credits

All meteorological data used in this project is the intellectual property of the **Badan Meteorologi, Klimatologi, dan Geofisika (BMKG)** of the Republic of Indonesia. 

We would like to express our sincere gratitude to BMKG for providing public access to historical weather data through their official portal. This machine learning project and our research into SDG 13 (Climate Action) were made possible thanks to their commitment to transparent and accessible climate data. 

For more information and to access similar datasets, please visit: [https://dataonline.bmkg.go.id/](https://dataonline.bmkg.go.id/)

## NOTEBOOK : https://www.kaggle.com/code/ameliaochamaharani/humidity-prediction