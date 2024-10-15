def data_namer(names_list):
    f_tests = []
    f_paths = []
    m_tests = []
    m_paths = []
    r_tests = []
    r_paths =[]
    for name in names_list:
        split = name.split('_')
        if 'f' in split[2]:
            f_name = name #split[0]+'_'+split[1]
            f_path = name+'//f_test'
            f_tests.append(f_name)
            f_paths.append(f_path)
        if 'm' in split[2]:
            m_name = name #split[0]+'_'+split[1]
            m_path = name+'//m_test'
            m_tests.append(m_name)
            m_paths.append(m_path)
        if 'r' in split[2]:
            r_name = name #split[0]+'_'+split[1]
            r_path = name+'//r_test'
            r_tests.append(r_name)
            r_paths.append(r_path)
    data_dict = {'F': f_tests, 'M':m_tests, 'R': r_tests }
    path_dict = {'F': f_paths, 'M':m_paths, 'R': r_paths }
    return [data_dict, path_dict]
