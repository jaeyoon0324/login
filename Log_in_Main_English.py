import pickle 
import time

with open("data.log_in_id", "rb") as fw:
    id_ = pickle.load(fw)
with open("data.log_in_name", "rb") as pkl:
    id_name = pickle.load(pkl)
with open("data.log_in_id", "wb") as fw:
    pickle.dump(id_, fw)
with open("data.log_in_name", "wb") as pkl:
    pickle.dump(id_name, pkl)


current_user = 00

def source_log_in_():

    def log_in():

        account_ask = input("Do you have an account? Y / N : ")
        if account_ask == "N" or account_ask == "n":
            print("Making New Account...\n")
            account_making()
        elif account_ask == "y" or account_ask == "Y":
            print("Proceeding Log in...\n")
            log_in_account()

    def account_making():

        m_name = input("Enter Your Name : ")
        m_id = input("Enter Your New Id. : ")
        m_pw = input("Enter Your New Password.")
        id_[m_id] = m_pw
        id_name[m_id] = m_name
        search_history = []
        with open("data.log_in_id", "wb") as fw:
            pickle.dump(id_, fw)
        with open("data.log_in_name", "wb") as pkl:
            pickle.dump(id_name, pkl)
        with open("data.user_data; %s"%m_id, "wb") as user_data_pickle:
            pickle.dump(search_history, user_data_pickle)
        print("\n________________\nStart Log in\n_________________")
        log_in_account()

    def log_in_account():

        global current_user

        

        time.sleep(1)
        with open("data.log_in_id", "rb") as fw:
            data = pickle.load(fw)
        with open("data.log_in_name", "rb") as pkl:
            data3 = pickle.load(pkl)
        lg_id = input("Please Enter ID.\n________________\n")
        while True:
            if lg_id in data:
                while True:
                    lg_pw = input("Please Enter Password.\n________________\n")
                    if data[lg_id] == lg_pw:
                        name = data3[lg_id]
                        print("welcome "+name + ".\n________________")

                        break
                    elif id_[lg_id] != lg_pw:
                        print("Check Your Password.\n")
            else:
                print("Check Your Id\n")
                log_in_account()
        
            break
        current_user = lg_id
        
        

    log_in()

log_in_reqest = input("Do you want to log in? : Y / N : ")

if log_in_reqest == "y" or log_in_reqest == "Y":
    print("Proceeding log in...")
    time.sleep(0.5)
    source_log_in_()

elif log_in_reqest == "n" or log_in_reqest == "N":
    print("Start with guest account...\n")
    time.sleep(0.5)



if log_in_reqest == "y" or log_in_reqest == "Y":
    with open("data.user_data; %s"%current_user, "rb") as user_data_pickle:
        my_searched_list = pickle.load(user_data_pickle)
