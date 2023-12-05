import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def explore_categorical(train, target, cat_var, alpha=0.05):
    '''
    Explore the relationship between a binary target variable and a categorical variable.

    Parameters:
    train: The training data split set.
    target (str): The name of the binary target variable.
    cat_var (str): The name of the categorical variable to explore.
    alpha (float): Significance level for hypothesis testing.

    '''
    # Print the name of the categorical variable
    print()
    print(cat_var, '&', target)
    print('')

    # Calculate the chi-squared test statistic, p-value, degrees of freedom, and expected values
    ct = pd.crosstab(train[cat_var], train[target], margins=True)
    chi2, p, dof, expected = stats.chi2_contingency(ct)
    print(f"Chi2: {chi2}")
    print(f"P-value: {p}")
    print(f"Degrees of Freedom: {dof}")
    print('')

    # Check for statistical significance
    if p < alpha:
        print('The null hypothesis can be rejected due to statistical significance.')
        print('Ergo there is a relationship between the target variable and corresponding feature(s)')
    else:
        print('The null hypothesis cannot be rejected at the chosen significance level.')
        print('Ergo there is not a relationship between the target variable and corresponding feature(s)')

def plot_categorical_by_churn(train, categories):
    # Set up the subplot grid
    num_cols = 2  # Number of columns in the subplot grid
    num_rows = (len(categories) + 1) // num_cols  # Calculate the number of rows

    # Create subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))

    # Flatten the axes for easier iteration
    axes = axes.flatten()

    # Iterate through categories and create count plots or stacked histograms
    for i, category in enumerate(categories):
        if train[category].dtype == 'object':
            sns.countplot(x=category, hue='churn', data=train, ax=axes[i])
            axes[i].set_title(f'{category} by Churn')
            axes[i].set_xlabel(category)
            axes[i].set_ylabel('Count')
        else:
            sns.histplot(data=train, x=category, hue='churn', multiple='stack', ax=axes[i])
            axes[i].set_title(f'Histogram of {category} by Churn')
            axes[i].set_xlabel(category)
            axes[i].set_ylabel('Frequency')

    # Adjust layout for better appearance
    plt.tight_layout()
    plt.show()

def plot_boxplots_by_subgroups(train, subgroups):
    # Get the number of unique combinations for subplot layout
    num_subplots = len(subgroups)

    # Set up the subplot grid
    num_cols = 2  # Number of columns in the subplot grid
    num_rows = (num_subplots + 1) // num_cols  # Calculate the number of rows

    # Create subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))

    # Flatten the axes for easier iteration
    axes = axes.flatten()

    # Iterate through subgroups and create boxplots
    for i, subgroup in enumerate(subgroups):
        sns.boxplot(x=subgroup, y='monthly_charges', hue='churn', data=train, ax=axes[i])
        axes[i].set_title(f'Monthly Charges by {subgroup} and Churn Status')
        axes[i].set_xlabel(subgroup)
        axes[i].set_ylabel('Monthly Charges')

    # Adjust layout for better appearance
    plt.tight_layout()
    plt.show()