import pandas as pd
import tkinter as tk

input_dic = {"Weather": [], "Activity type": [], "Budget per person": [], "Number of friends minimum": [],
             "Number of friends maximum": [], "Location": [], "Time available minimum": [], "Time available maximum": []}
data = pd.read_excel("database.xlsx")
filter_basis_for_time = ""
final_results = ""


# Ask for weather
def get_weather():
    weather_input = input("\n\nIs the weather good today? Swipe!").lower()
    if weather_input == "left":
        weather_for_inputdic = "bad"
    else:
        weather_for_inputdic = "good"
    input_dic["Weather"].append(weather_for_inputdic)


# Type of activity
def get_activity():
    activity_input = input("\n\nDo you want to do something sporty? Swipe!").lower()
    if activity_input == "left":
        ask_again_activity_a = input("\nI see you might prefer something cultural then? Swipe!").lower()
        if ask_again_activity_a == "left":
            activity_for_inputdic = "relaxed"
        else:
            activity_for_inputdic = "cultural"
    else:
        activity_for_inputdic = "active"
    input_dic["Activity type"].append(activity_for_inputdic)


# Budget per person
def get_budget():
    budget_input = input("\n\nIs the budget per person less than 10€? Swipe!").lower()
    if budget_input == "left":
        ask_again_budget_a = input("\nSo more like 20€ per person? Swipe!").lower()
        if ask_again_budget_a == "left":
            ask_again_budget_b = input("\nOh you really want it? So 50€ per person? Swipe!").lower()
            if ask_again_budget_b == "left":
                budget_max_for_inputdic = 100
            else:
                budget_max_for_inputdic = 50
        else:
            budget_max_for_inputdic = 20
    else:
        budget_max_for_inputdic = 10
    input_dic["Budget per person"].append(budget_max_for_inputdic)


# How many people are you
def get_people():
    people_input = input("\n\nAre you by yourself today? Swipe!").lower()
    if people_input == "left":
        ask_again_people_a = input("\nAre you more than 3? Swipe!").lower()
        if ask_again_people_a == "right":
            ask_again_people_b = input("\nAll right, all right! But more than 5? Swipe!").lower()
            if ask_again_people_b == "right":
                ask_again_people_c = input("\nDamn, you got a lot of friends! But even more than 10? Swipe!").lower()
                if ask_again_people_c == "right":
                    people_min_for_inputdic = 10
                    people_max_for_inputdic = 20
                else:
                    people_min_for_inputdic = 5
                    people_max_for_inputdic = 10
            else:
                people_min_for_inputdic = 3
                people_max_for_inputdic = 5
        else:
            people_min_for_inputdic = 1
            people_max_for_inputdic = 3
    else:
        people_min_for_inputdic = 1
        people_max_for_inputdic = 1
    input_dic["Number of friends minimum"].append(people_min_for_inputdic)
    input_dic["Number of friends maximum"].append(people_max_for_inputdic)


# Location
def get_location():
    location_input = input("\n\nFinal question, do you want the results for a specific city? Swipe!").lower()
    if location_input == "right":
        location_for_inputdic = input("\nThen please type in the city name here: ")
    else:
        location_for_inputdic = "Unspecified"
    input_dic["Location"].append(location_for_inputdic)


# How much time do you have for the activity?
def get_time():
    time_input = input("\n\nDo you have more than 60 minutes of time? Swipe!")
    if time_input == "right":
        ask_again_time_a = input("\nEven more than 2 hours though? Swipe")
        if ask_again_time_a == "right":
            ask_again_time_b = input("\nMore than 4 hours though? Swipe!")
            if ask_again_time_b == "right":
                ask_again_time_c = input("\nShould it be a full day trip? Swipe!")
                if ask_again_time_c == "right":
                    time_min_for_inputdic = 24
                    time_max_for_inputdic = 48
                else:
                    time_min_for_inputdic = 4
                    time_max_for_inputdic = 6
            else:
                time_min_for_inputdic = 2
                time_max_for_inputdic = 4
        else:
            time_min_for_inputdic = 1
            time_max_for_inputdic = 2
    else:
        time_min_for_inputdic = 0
        time_max_for_inputdic = 1
    input_dic["Time available minimum"].append(time_min_for_inputdic)
    input_dic["Time available maximum"].append(time_max_for_inputdic)


# Above are all INPUT FUNCTIONS
#
#
#
# Beneath are all SEARCH FUNCTIONS


# Look through database for fitting parameters
def filter_by_all_except_time(weather, activity_type, budget_max, people_max, people_min):
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
    filtered_by_people_min = filtered_by_people_max[filtered_by_people_max.minimum_people <= people_min]
    if filtered_by_people_min.empty:
        return print("We found no perfect match in our database")
    else:
        filter_basis_for_time = filtered_by_people_min


# then filter for the available time // min and max
def filter_for_time_span(time_min):
    global final_results
    global filter_basis_for_time
    print(filter_basis_for_time)
    is_activity_max_valid = filter_basis_for_time[filter_basis_for_time.time_maximum >= time_min]
    is_user_min_valid = is_activity_max_valid[is_activity_max_valid.time_minimum <= time_min]
    if is_activity_max_valid.empty:
        return print("We found no perfect match in our database")
    else:
        final_results = is_activity_max_valid


# RUNNING THE WHOLE PROGRAM
get_weather()
get_activity()
get_budget()
get_people()
get_location()
get_time()
print(f"\n\n\n{input_dic}\n\n")
USERS_WEATHER = input_dic["Weather"][0]
USERS_ACTIVITY = input_dic["Activity type"][0]
USERS_BUDGET_MAX = input_dic["Budget per person"][0]
USERS_PEOPLE_MIN = input_dic["Number of friends minimum"][0]
USERS_PEOPLE_MAX = input_dic["Number of friends maximum"][0]
USERS_TIME_MIN = input_dic["Time available minimum"][0]
USERS_TIME_MAX = input_dic["Time available maximum"][0]
filter_by_all_except_time(weather=USERS_WEATHER, activity_type=USERS_ACTIVITY, budget_max=USERS_BUDGET_MAX,
                          people_max=USERS_PEOPLE_MAX, people_min=USERS_PEOPLE_MIN)
filter_for_time_span(time_min=USERS_TIME_MIN)
print(final_results)


# Create Tkinter User Interface
#window = tk.Tk()
#window.title("ADVENTURE INCOMING")
# setting window size
#window.geometry("400x600")
# creating canvas
#canvas = tk.Canvas(width=400, height=600)
# swiping buttons
#swipe_left_button = tk.Button(text="Swipe LEFT", width=10, height=3)
#swipe_left_button.grid(row=3, column=0)
#swipe_right_button = tk.Button(text="Swipe RIGHT", width=10, height=3)
#swipe_right_button.grid(row=3, column=5)


#window.mainloop()
