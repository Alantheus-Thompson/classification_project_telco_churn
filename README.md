# classification_project_telco_churn
Goal:
Find drivers of customer churn at Telco

Why:
Reducing churn is paramount to business brand, reputation, and profitability. Customers have access to numerous channels that can amplify a bad review and lower our NPS. CAC can be 9x's more expensive than retention efforts.

Overview:
Walk through data pipeline process (acquire, prepare, explore, and modeling), conclusions, recommendations, and potentials for further investigation.

# Initial Hypothesis: 

Customers churn due to affordability, lack of speed of service, and inconvenience

# Data Dictionary

| Column Name             | Description                                      | Data Type          | Example           |
|-------------------------|--------------------------------------------------|--------------------|-------------------|
| customer_id             | Unique identifier for each customer              | String (or int)    | "C123456"         |
| monthly_charges         | Monthly charges for telecom services             | Float              | 75.0              |
| contract_type           | month to month, 1 yr, or 2 yr                    | Object             | "month_to_month   |
| internet_service_type   | Type of internet service (DSL, Fiber, None)      | Object             | "Fiber"           |
| payment_type            | Payment method                                   | Object             | "Electronic check"|
| churn                   | Customer churn status (Yes or No)                | Object             | "Yes"             |

# Plan/Process

(1) Acquire data from Codeup MySql.

(2) Prepare data by dropping duplicate columns, fill nulls in Internet Service Type with No Internet Service, change Total Charges from Object to Float, & shorten Payment Type names for graphing purposes.

(3) Explore:  

Monthly charges, internet service type, contract type, and payment type are the features that most closely align to inital hypothesis.¶

Do the 4 identified features have a relationship to churn?

To answer questions examine churn vs no churn across categorical features using a bar plot.  Use a histogram plot for continuous features.

(4) Insights

(5) Model using Decision Tree Classification methodology.

Find optimal depth

# Duplication Instructions

Gain access to Codeup MySql\
Clone this repository
Create env with credentials
Run this notebook

# Takeaways & Conclusions
Fiber Optic is the top contributor within Internet Service Type Churn
Mailed Checks is the top contributor within Payment Type Churn
Mont-to_month is the top contributor within Contract Type
Monthly charges are not a significant contributor to churn with the monthly charge distribution.

Monthly charges seems to be a significant contributor to churn for one year and two year contracts but less so for month-to-month.
Montly charges does not appear to be a significant contributor to Fiber Optic, No Internet Service, or DSL.
Monthly charges appears to be a significant contributor to mailed check churn, credit card, and bank transfer, but not so a significant contributor to electronic check.

# Recommendations
Look into driver of Fiber Optic churn.  Fiber indicates speed and complexity.  Assumption is that there is a relationship to tech support.
Run statistical test on monthly charges to mailed check by churn.  Once confirmed assumption is that there is also a relationship to month-to-month and mailed check.  

