# Data Analysis Report

Report generated on: 20/07/2025 20:41:58

Because GitHub is unable to display Plotly interactive figures, a dynamic report is generated to compile each figure along with their respective captions.

For interactive features, please refer to the Jupyter notebooks in the 'NOTEBOOKS/' directory and rerun the cells to generate the plots.

<hr>

<hr>

## Descriptive Analysis

Identification on what is in the data


### Global View of Expenses & Income

*  Total amount of Expenses: S$35,268.00 and total number of expense transactions: 3667

*  Total amount of Income: S$47,037.65 and total number of income transactions: 204

#### Spending by Category (Top 7 + Others)

<p align='center'><img src='ASSETS/PLOTS/PIE_CHART_TOP_7_SPENDING_CATEGORIES.png'></p>

* Top 7 categories account for 88.82% of the total spending with the highest category spending being Food at 66.29%.


### Distribution Visualisation & Analysis

To analyse the distribution of purchase frequency in histogram and boxplot to show clarity on the skewness and common amounts


#### Distribution of Purchase Sizes (Histogram)

<p align='center'><img src='ASSETS/PLOTS/HISTOGRAM_DISTRIBUTION_OF_PURCHASE_SIZES.png'></p>

* The general spending amount distribution is heavily concentrated in the lower value range (left side), with a long right tail.
This pattern reflects frequent low-cost purchases (such as, daily food or transport) and a few large-value expenses, possibly one-
time or monthly essentials.


#### Descriptive Statistics Summary



<div align='center'>

```markdown
| Metric              | Value   |
|:--------------------|:--------|
| Count               | 3,331   |
| Mean                | 6.95    |
| Median              | 6.50    |
| Standard Deviation  | 3.51    |
| Minimum             | 0.30    |
| Lower Outlier Bound | -3.75   |
| Q1 (25%)            | 4.50    |
| Q3 (75%)            | 10.00   |
| Upper Outlier Bound | 18.25   |
| Maximum             | 18.20   |
| IQR                 | 5.50    |
| Skewness            | 0.85    |
| Kurtosis            | 0.52    |
```

</div>

*  The overall spending distribution is moderately right-skewed (0.85) indicating a higher concentration of small purchases along
with a few large outliers. The kurtosis (0.52) suggests extreme spending events are relatively rare and the distribution is more
flattened than a normal bell curve.

#### Distribution of Purchase Sizes Without Outliers (Histogram)

<p align='center'><img src='ASSETS/PLOTS/HISTOGRAM_DISTRIBUTION_OF_PURCHASE_SIZES_WITHOUT_OUTLIERS.png'></p>

* Upon visualised, there are considerable number of outliers beyond Upper Outlier Bound.


<hr>

## Behavioral Patterns

Analysis to answer the question how I spend


### General View of Purchase Size by Category

To showcase which categories have the largest typical purchase


#### Purchase Size by Category

<p align='center'><img src='ASSETS/PLOTS/BOX_PLOT_PURCHASE_SIZE_BY_CATEGORY.png'></p>

* Since each category has distinct data range and descriptive statistics, it is only reasonable the outliers are detected within
each category separately. Upon outlier detection, red and white dots signify outlier and non-outlier data points respectively.


#### Purchase Size by Category Without Outliers

<p align='center'><img src='ASSETS/PLOTS/BOX_PLOT_PURCHASE_SIZE_BY_CATEGORY_WITHOUT_OUTLIERS.png'></p>

* In contrast, this boxplot contains no outlier.


### Spending Behaviour Based on the Days within the Week

To show the spending pattern within the days of the week


#### Spending Behaviour by Day of the Week

<p align='center'><img src='ASSETS/PLOTS/BAR_PLOT_SPENDING_BEHAVIOUR_BY_DAY.png'></p>

* Spending is highest on Sunday, with average transaction values approximately 18.9% above the average levels of the other days in
a week.


*  Weekdays reflect routine low-value spending (e.g., transport, food).

*   Mondays reflect the lowest spending level across the days which are aligned as there is typically no outside activities (e.g.
going out, eating out) on Mondays.

### Weekends vs Weekdays Analysis

To show the comparison of spending between weekends and weekdays


#### Spending Behaviour by Day Type (Weekday vs Weekend)

<p align='center'><img src='ASSETS/PLOTS/SPENDING_BEHAVIOUR_WEEKEND_VS_WEEKDAY.png'></p>

* Upon looking at the presented boxplot, the Spending is greater on Weekends than it is on Weekdays. In this case the significance
of the difference needs to be assessed to obtain better understanding on the Spending Behaviours throughout the week.  From the
histogram previously, the data is extremely right-skewed.



Hypotheses for One-Tailed Test:
- Null Hypothesis: average amount spent on weekend less than or equal to average amount spent on weekday 

    i.e. $H_0: \mu_{weekend} \leq \mu_{weekday}$
- Alternative Hypothesis: average amount spent on weekend greater than average amount spent on weekday 

    i.e. $H_1: \mu_{weekend} > \mu_{weekday}$



 The result of the first statistical test is as follows:




<div align='center'>

```markdown
| Metric      | Value                      |
|:------------|:---------------------------|
| Test        | Mann-Whitney U Test        |
| p-value     | 0.00                       |
| Group1_Mean | 10.70                      |
| Group1_CI   | (9.71, 11.69)              |
| Group2_Mean | 9.23                       |
| Group2_CI   | (8.72, 9.74)               |
| Conclusion  | Reject $H_0$ (Significant) |
```

</div>

 With the p-value 0.00 < 0.01, it is discovered that there is a statistically significant difference on average spending between
weekends and weekdays. Hence, Reject $H_0$ (Significant) at 99.0% confidence level.


 Depending on culture and life stage, Friday is sometimes considered as "weekend-like" periods according to many businesses
because Friday night spending is often social or leisure. Another set of analysis is redone with the inclusion of Friday
considered as weekend


#### Spending Behaviour by Day Type (Weekday vs Weekend + Friday)

<p align='center'><img src='ASSETS/PLOTS/SPENDING_BEHAVIOUR_WEEKEND_VS_WEEKDAY_RECALCULATED.png'></p>

* Upon looking at the presented boxplot, the Spending is still greater on Weekends than it is on Weekdays. The signficance test is
going to be recalculated to confirm the findings.


 The result of the second statistical test is as follows:




<div align='center'>

```markdown
| Metric      | Value                      |
|:------------|:---------------------------|
| Test        | Mann-Whitney U Test        |
| p-value     | 0.00                       |
| Group1_Mean | 10.35                      |
| Group1_CI   | (9.53, 11.17)              |
| Group2_Mean | 9.10                       |
| Group2_CI   | (8.58, 9.63)               |
| Conclusion  | Reject $H_0$ (Significant) |
```

</div>

 With the p-value 0.00 < 0.01, it is discovered that there is a statistically significant difference on average spending between
weekends and weekdays. Hence, Reject $H_0$ (Significant) at 99.0% confidence level.


### Geospatial Visualisation

To visualise the geographical distribution of the data


#### Spending Heatmap by Region

<p align='center'><img src='ASSETS/PLOTS/SPENDING_HEATMAP_BY_REGION.png'></p>

* Each point represents a region of transaction activity. Size corresponds to the number of transactions (log scale), where larger
points correspond to areas with more frequent transactions. Meanwhile, the average spending per transaction is represented by the
blue-red colour scale with blue being the lowest average spending and red being the highest.


*  The Geospatial Heatmap displays various distinct zones of highly-frequent low-cost transactions (e.g. Clementi and Tanjong
Pagar), likely reflecting habitual daily spending patterns around home, school, and/or work.

*  On the contrary, areas such as Jalan Besar and Boon Keng show much higher average spending per visit despite of minimum visits,
representing discretionary purchases.

*  Such contrast underlines a duality of spending behaviours where on the functional zones, there is a habitual spending
concentration with occasional higher consumption on other districts.

### Volume vs Value Analysis

To compare districts where spending is frequent vs expensive to support behavioural insights


#### Volume vs. Value by District

<p align='center'><img src='ASSETS/PLOTS/VOLUME_VALUE_BY_DISTRICT.png'></p>

* The chart above compares all districts by Transaction Count (volume), Total Spending (value), and Average Amount per Transaction
(intensity), each normalised between 0 and 1 where 0 represents values close to the Minimum within the column and 1 the Maximum
within the column.


*  Clementi shows the highest normalized Transaction Volume and Total Spending, indicating it is by far the most frequently visited
location, likely reflecting a habitual area such as a school or home base. On the other hand, its Average Amount per Transaction
is low, suggesting small, routine purchases.

*  On the contrary, Outram Park has a low number of transactions, but the highest average spending per visit, suggesting it is used
for rare but expensive purchases - possibly special dining, shopping, or events.

*  Mid-tier districts like Tanjong Pagar and Jurong East show moderate activity across all metrics, suggesting balanced use cases -
both frequent and moderately costly.

 Normalization provides better comparison for visualisation, however, it is worth noting that it masks absolute differences -
Clementi's transaction count could be 10x higher than others, even if shown as only slightly above in the chart.


<hr>

## Temporal Trends

How the behaviour changes over time


### Monthly Spend

To show the seasonality of the spending on the monthly bucket


#### Monthly Spending Pattern (Stacked by Year)

<p align='center'><img src='ASSETS/PLOTS/MONTHLY_SPENDING_PATTERN_STACKED.png'></p>

* The graph shows the monthly spending trend for each year. The stacked bars indicate the total spending amount per month for each
year.


#### Monthly Spending Trend

<p align='center'><img src='ASSETS/PLOTS/MONTHLY_SPENDING_PATTERN_LINE.png'></p>

* A line chart displays the monthly spending trend throughout the data horizon to identify the overall spending trend.


*  Note: There is a visible drop in spending between June and August 2019. This reflects a period during which data was not
recorded, not a behavioral change. Interpret trends around this period with caution.  The following periods are when the data was
not recorded completely and hence, no data point: June 2019 & July 2019. Due to this, these periods need to be marked in the
subsequent steps.

#### Monthly Spending Trend

<p align='center'><img src='ASSETS/PLOTS/MONTHLY_SPENDING_PATTERN_LINE_ANNOTATED.png'></p>

* The specified periods where the data is missing are highlighted in the graph using gray shading and annotated as "No Record".


#### Monthly Spending Trend with Moving Average

<p align='center'><img src='ASSETS/PLOTS/MONTHLY_SPENDING_PATTERN_MOVING_AVERAGE.png'></p>

* The holistic monthly spending trend is shown in the graph, with the original data points and a 3-month, 6-month and 12-month
moving average.


#### Seasonality Index (Scaled from -1 to 1)

<p align='center'><img src='ASSETS/PLOTS/SEASONALITY_INDEX.png'></p>

* To better visualise the Seasonality Index, a Bar Chart scaled from -1 to 1 is used. From the graph, it is discovered that the
range of Seasonality Index is not beyond the scale between -0.1 to 0.1. Therefore, spending is not strongly seasonal; variability
is likely driven by events, not months.


### Surplus/Deficit Analysis

To analyse the surplus/deficit in the spending pattern


#### Monthly Cash Flow: Resources (Income + Carry-over) vs Expenses

<p align='center'><img src='ASSETS/PLOTS/MONTHLY_CASH_FLOW.png'></p>

* Throughout the horizon of the analysis, the monthly cash flow reflects a consistent surplus each month triggering a growing
cumulative excess income indicating a sustainable savings habits.Occasional months reflect extremely low spending are due to the
Circuit Breaker imposed during Covid-19 pandemic and therefore, the income along with carry-over can exceed twice as much expenses
during those months. Overtime, the spending has been escalating as the cost of living and lifestyle in general have been climbing
altogether.


#### Cumulative Surplus Analysis

<p align='center'><img src='ASSETS/PLOTS/CUMULATIVE_SURPLUS.png'></p>

* The graph shows the cumulative surplus analysis for each month. The bars indicate the cumulative surplus amount per month.


#### Cumulative Surplus Analysis

<p align='center'><img src='ASSETS/PLOTS/CUMULATIVE_SURPLUS_FULL.png'></p>

* Since both June and July 2019 do not have any data points, these periods are skipped in the table. Logically, these periods
should remain flat and consistent with the balance of the previous month since the timeline is continuous and these two months are
periods of inactivity with no financial change. According to the Cumulative Surplus Analysis, the final cumulative surplus is
S$13560.95 on December 2023.


<hr>

## Diagnostic & Comparative Analysis

Analysis to diagnose and compare data according to the financial events


### Year-on-Year (YoY) Comparison

To analyse the evolution of spending over the years


#### Year-over-Year (YoY) Monthly Surplus Comparison

<p align='center'><img src='ASSETS/PLOTS/YOY_SURPLUS_COMPARISON.png'></p>

* Strong surpluses generally happen in January, February, March of each year linked of the low-season holiday activities since
these periods are more intensive due to exams and work. Some weaker surpluses of June, July, August are linked to the mid-of-the-
year big purchases. The absence of strong month-to-month seasonality suggests that financial behavior is primarily driven by life
circumstances or irregular events rather than fixed cycles


### Trend Break Detection

To identify if there is a change of pattern in spending


#### Trend Break Detection

<p align='center'><img src='ASSETS/PLOTS/TREND_BREAK_DETECTION.png'></p>

* A Trend Break is detected on November 2021 which is linked with the increased spending due to the beginning of employment upon
graduation. Pelt/Binary Segmentation from the RPT package is used to detect the trend breaks. The approach is prioritise for
efficient search for the optimal breakpoints using dynamic programming and actively recursively splits the signal to detect
multiple changes.


---

For more information, please refer to the Data Analysis Report Notebook [here](NOTEBOOKS/CASH_FLOW_DATA_ANALYSIS.ipynb) directory.
