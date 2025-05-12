import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex']=='Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df.loc[df['education']=='Bachelors']) * 100/df['education'].count(),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    total_advanced_education = len(df[(df['education'].isin(['Bachelors','Masters','Doctorate']))]['salary'])
    total_low_education = len(df[(df['education'].isin(['HS-grad','Some-college','Assoc-voc','11th','Assoc-acdm','10th','7th-8th','Prof-school','9th','12th','5th-6th','1st-4th','Preschool']))]['salary'])

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df[(df['education'].isin(['Bachelors','Masters','Doctorate'])) & (df['salary']=='>50K')])
    lower_education = len(df[(df['education'].isin(['HS-grad','Some-college','Assoc-voc','11th','Assoc-acdm','10th','7th-8th','Prof-school','9th','12th','5th-6th','1st-4th','Preschool'])) & (df['salary']=='>50K')])

    # percentage with salary >50K
    higher_education_rich = round(higher_education *100 / total_advanced_education,1)
    lower_education_rich = round(lower_education * 100 / total_low_education,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    total_minimum_workers = len(df[df['hours-per-week']==1]['salary'])
    num_min_workers = len(df[(df['hours-per-week']==1) & (df['salary']=='>50K')])

    rich_percentage = round(num_min_workers * 100 / total_minimum_workers)

    # What country has the highest percentage of people that earn >50K?
    percentage_highest_country = (df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100))
    highest_earning_country = percentage_highest_country.idxmax()
    highest_earning_country_percentage = round(percentage_highest_country[highest_earning_country], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country']=='India') & (df['salary']=='>50K')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
