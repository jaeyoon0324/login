you need to install pickle module python -m pip install pickle on cmd

***** you should run Setting for log_in first and then run log_in main, if not, Error occur

if you want to access one account's own old data, please add this code

with open("data.user_data; %s"%current_user, "rb") as user_data_pickle: my_old_data = pickle.load(user_data_pickle)
