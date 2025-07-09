# Data Analysis Report

Report generated on: 09/07/2025 15:09:45

## Spending by Category (Top 7 + Others)

<p align='center'><img src='ASSETS/PLOTS/PIE_CHART_TOP_7_SPENDING_CATEGORIES.png'></p>

* Top 7 categories account for 88.82% of the total spending with the highest category spending being Food at 66.29%.


## Distribution of Purchase Sizes (Histogram)

<p align='center'><img src='ASSETS/PLOTS/HISTOGRAM_DISTRIBUTION_OF_PURCHASE_SIZES.png'></p>

* The general spending amount distribution is heavily concentrated in the lower value range (left side), with a long right tail.
This pattern reflects frequent low-cost purchases (such as, daily food or transport) and a few large-value expenses, possibly one-
time or monthly essentials.


## Distribution of Purchase Sizes Without Outliers (Histogram)

<p align='center'><img src='ASSETS/PLOTS/HISTOGRAM_DISTRIBUTION_OF_PURCHASE_SIZES_WITHOUT_OUTLIERS.png'></p>

* Upon visualised, there are considerable number of outliers beyond Upper Outlier Bound.


## Purchase Size by Category

<p align='center'><img src='ASSETS/PLOTS/BOX_PLOT_PURCHASE_SIZE_BY_CATEGORY.png'></p>

* Since each category has distinct data range and descriptive statistics, it is only reasonable the outliers are detected within
each category separately. Upon outlier detection, red and white dots signify outlier and non-outlier data points respectively.


## Purchase Size by Category Without Outliers

<p align='center'><img src='ASSETS/PLOTS/BOX_PLOT_PURCHASE_SIZE_BY_CATEGORY_WITHOUT_OUTLIERS.png'></p>

* In contrast, this boxplot contains no outlier.


## Spending Behaviour by Day of the Week

<p align='center'><img src='ASSETS/PLOTS/HISTOGRAM_DISTRIBUTION_OF_PURCHASE_SIZES_WITHOUT_OUTLIERS.png'></p>

* Spending is highest on Sunday, with average transaction values approximately 18.9% above the average levels of the other days in
a week. Weekdays reflect routine low-value spending (e.g., transport, food). Mondays reflect the lowest spending level across the
days which are aligned as there is typically no outside activities (e.g. going out, eating out) on Mondays.


## Spending Behaviour by Day Type (Weekday vs Weekend)

<p align='center'><img src='ASSETS/PLOTS/SPENDING_BEHAVIOUR_WEEKEND_VS_WEEKDAY.png'></p>

* Upon looking at the presented boxplot, the Spending is greater on Weekends than it is on Weekdays. In this case the significance
of the difference needs to be assessed to obtain better understanding on the Spending Behaviours throughout the week.  From the
histogram previously, the data is extremely right-skewed.


## Spending Behaviour by Day Type (Weekday vs Weekend + Friday)

<p align='center'><img src='ASSETS/PLOTS/SPENDING_BEHAVIOUR_WEEKEND_VS_WEEKDAY_RECALCULATED.png'></p>

* Upon looking at the presented boxplot, the Spending is still greater on Weekends than it is on Weekdays. The signficance test is
going to be recalculated to confirm the findings.


## Spending Heatmap by Region

<p align='center'><img src='ASSETS/PLOTS/SPENDING_HEATMAP_BY_REGION.png'></p>

* Each point represents a region of transaction activity. Size corresponds to the number of transactions (log scale), where larger
points correspond to areas with more frequent transactions. Meanwhile, the average spending per transaction is represented by the
blue-red colour scale with blue being the lowest average spending and red being the highest.


## Volume vs. Value by District

<p align='center'><img src='ASSETS/PLOTS/VOLUME_VALUE_BY_DISTRICT.png'></p>

* The chart above compares all districts by Transaction Count (volume), Total Spending (value), and Average Amount per Transaction
(intensity), each normalised between 0 and 1 where 0 represents values close to the Minimum within the column and 1 the Maximum
within the column.


## Monthly Spending Pattern (Stacked by Year)

<p align='center'><img src='ASSETS/PLOTS/MONTHLY_SPENDING_PATTERN_STACKED.png'></p>

* The graph shows the monthly spending trend for each year. The stacked bars indicate the total spending amount per month for each
year.


## Monthly Spending Trend

<p align='center'><img src='ASSETS/PLOTS/MONTHLY_SPENDING_PATTERN_LINE_ANNOTATED.png'></p>

* The specified periods where the data is missing are highlighted in the graph using gray shading and annotated as "No Record".


## Monthly Spending Trend with Moving Average

<p align='center'><img src='ASSETS/PLOTS/MONTHLY_SPENDING_PATTERN_MOVING_AVERAGE.png'></p>

* The holistic monthly spending trend is shown in the graph, with the original data points and a 3-month, 6-month and 12-month
moving average.


## Seasonality Index (Scaled from -1 to 1)

<p align='center'><img src='ASSETS/PLOTS/SEASONALITY_INDEX.png'></p>

* To better visualise the Seasonality Index, a Bar Chart scaled from -1 to 1 is used. From the graph, it is discovered that the
range of Seasonality Index is not beyond the scale between -0.1 to 0.1. Therefore, spending is not strongly seasonal; variability
is likely driven by events, not months.


## Monthly Cash Flow: Resources (Income + Carry-over) vs Expenses

<p align='center'><img src='ASSETS/PLOTS/MONTHLY_CASH_FLOW.png'></p>

* Throughout the horizon of the analysis, the monthly cash flow reflects a consistent surplus each month triggering a growing
cumulative excess income indicating a sustainable savings habits.Occasional months reflect extremely low spending are due to the
Circuit Breaker imposed during Covid-19 pandemic and therefore, the income along with carry-over can exceed twice as much expenses
during those months. Overtime, the spending has been escalating as the cost of living and lifestyle in general have been climbing
altogether.


## Cumulative Surplus Analysis

<p align='center'><img src='ASSETS/PLOTS/CUMULATIVE_SURPLUS_FULL.png'></p>

* Since both June and July 2019 do not have any data points, these periods are skipped in the table. Logically, these periods
should remain flat and consistent with the balance of the previous month since the timeline is continuous and these two months are
periods of inactivity with no financial change. According to the Cumulative Surplus Analysis, the final cumulative surplus is
S$13560.95 on December 2023.


## Year-over-Year (YoY) Monthly Surplus Comparison

<p align='center'><img src='ASSETS/PLOTS/YOY_SURPLUS_COMPARISON.png'></p>

* Strong surpluses generally happen in January, February, March of each year linked of the low-season holiday activities since
these periods are more intensive due to exams and work. Some weaker surpluses of June, July, August are linked to the mid-of-the-
year big purchases. The absence of strong month-to-month seasonality suggests that financial behavior is primarily driven by life
circumstances or irregular events rather than fixed cycles


## Trend Break Detection

<p align='center'><img src='ASSETS/PLOTS/TREND_BREAK_DETECTION.png'></p>

* A Trend Break is detected on November 2021 which is linked with the increased spending due to the beginning of employment upon
graduation. Pelt/Binary Segmentation from the RPT package is used to detect the trend breaks. The approach is prioritise for
efficient search for the optimal breakpoints using dynamic programming and actively recursively splits the signal to detect
multiple changes.


---

For more information, please refer to the Data Analysis Report Notebook ![here](NOTEBOOKS/CASH_FLOW_DATA_ANALYSIS.ipynb) directory.
