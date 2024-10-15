def claculate_data(type_pick, data_pick):
         
    if type_pick == 'R':
        R_dict = {}
        for data_ in data_pick:
            path = data_ + '//' + type_pick.lower()+ '_test'
            name = data_
            r_stat = stat_calc(path, 'r', alpha=0.05)
            r_dict= {name:r_stat}
        R_dict|r_dict
        return R_dict

    elif type_pick == 'F':
        F_dict = {}
        for data_ in data_pick:
            path = data_ + '//' + type_pick.lower()+ '_test'
            name = data_
            f_stat = stat_calc(path, 'f', alpha=0.05)
            f_dict= {name:f_stat}
        F_dict|f_dict
        return F_dict
        
    elif type_pick == 'M':
        M_dict = {}
        for data_ in data_pick:
            path = data_ + '//' + type_pick.lower()+ '_test'
            name = data_
            m_stat = stat_calc(path, 'm', alpha=0.05)
            m_dict= {name:m_stat}
        M_dict|m_dict
        return M_dict  
