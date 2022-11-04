import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  df_m = df[df.sex == 'Male']
  x = round(df_m.age.mean(), 1)
  average_age_men = x

  # What is the percentage of people who have a Bachelor's degree?
  pop = len(df)
  bach = len(df[df.education == 'Bachelors'])
  percentage_bachelors = round((bach/pop)*100, 1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_edu = ['Bachelors','Masters','Doctorate']
  
  higher_education = df[df.education.isin(higher_edu)]
  lower_education = df[~df.education.isin(higher_edu)]

  # percentage with salary >50K
  a = higher_education[higher_education.salary == '>50K'].shape[0]
  b = higher_education.shape[0]
  higher_education_rich = round(a/b*100,1)

  c = lower_education[lower_education.salary == '>50K'].shape[0]
  d = lower_education.shape[0]
  lower_education_rich = round(c/d*100,1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = min(df['hours-per-week'])

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = df[df['hours-per-week'] == 1].shape[0]
  num_rich_min_workers = df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].shape[0]
  
  rich_percentage = round(num_rich_min_workers/num_min_workers*100,1)

  # What country has the highest percentage of people that earn >50K?
  earning_counts = df[df.salary == '>50K']['native-country'].value_counts()
  count_country = df['native-country'].value_counts()
  percentage = earning_counts/count_country*100
  
  highest_earning_country = percentage.idxmax()
  
  highest_earning_country_percentage = round(percentage[highest_earning_country],1)
  
  # Identify the most popular occupation for those who earn >50K in India.
  india_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
  india_occ_counts = india_df.occupation.value_counts()
  
  top_IN_occupation = india_occ_counts.idxmax()

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
