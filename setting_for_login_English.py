def source_setting_log_in():

    import pickle

    id_ = {}
    id_name = {}
    with open("data.log_in_id", "wb") as fw:
        pickle.dump(id_, fw)
    with open("data.log_in_name", "wb") as pkl:
        pickle.dump(id_name, pkl)
source_setting_log_in()