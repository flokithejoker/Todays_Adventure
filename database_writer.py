import csv
import pandas as pd

data = pd.read_excel("database.xlsx")
# test = data.head()
# print(test)
filter_basis_for_time = ""
final_results = ""


def lookup(weather, activity_type, budget_max, people_max, people_min):
    global filter_basis_for_time
    # first filter for weather condition
    filtered_by_weather = data[data.weather == weather]
    # then check for activity type
    filtered_by_activity_type = filtered_by_weather[filtered_by_weather.activity_type == activity_type]
    if filtered_by_activity_type.empty:
        return print("We found no perfect match in our database")
    else:
        filter_basis_for_budget = filtered_by_activity_type
    # then filter for the given budget // only max matters
    filtered_by_budget_max = filter_basis_for_budget[filter_basis_for_budget.maximum_budget <= budget_max]
    if filtered_by_budget_max.empty:
        return print("We found no perfect match in our database")
    else:
        pass
    # then filter for the amount of friends that will participate // min and max
    filtered_by_people_max = filtered_by_budget_max[filtered_by_budget_max.maximum_people >= people_max]
    if filtered_by_people_max.empty:
        return print("We found no perfect match in our database")
    else:
        pass
    filtered_by_people_min = filtered_by_people_max[filtered_by_people_max.minimum_people <= people_min]
    if filtered_by_people_min.empty:
        return print("We found no perfect match in our database")
    else:
        filter_basis_for_time = filtered_by_people_min

    # then filter for the available time // min and max
def filter_for_time_span(time_max, time_min):
    global final_results
    global filter_basis_for_time
    filter_basis_for_time = pd.DataFrame(filter_basis_for_time)
    print(filter_basis_for_time)
    # first we check if client time max is in range of activity // must be >= to activity max
    is_max_in_range = filter_basis_for_time[filter_basis_for_time.time_maximum <= time_max]
    # second we check if client time max is actually valid // must be >= to activity min
    is_max_valid = is_max_in_range[is_max_in_range.time_minimum <= time_max]
    if is_max_valid.empty:
        print("We found no perfect match in our database")
    else:
        pass
    # third we check if client time min is in range of activity // must be <= to activity max
    is_min_in_range = is_max_valid[is_max_valid.time_maximum >= time_min]
    # fourth we check if client time min is actually valid // must be <= to activity min
    is_min_valid = is_min_in_range[is_min_in_range.time_minimum >= time_min]
    if is_min_valid.empty:
        print("We found no perfect match in our database")
    else:
        final_results = is_min_valid


lookup(weather="good", activity_type="active", budget_max=10, people_max=1, people_min=1)
filter_for_time_span(time_max=3, time_min=1)
print(final_results)
