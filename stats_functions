def stat_calc(path, type, alpha=0.05):
       
    all_files = glob.glob(os.path.join(path, '*.csv'))
    df_1 = pd.read_csv(all_files[0], header=None)
    cols_per_file = df_1.shape[1]
    df = pd.concat((pd.read_csv(f, header=None) for f in all_files), ignore_index=False, axis=1)
    header = [re.sub('.csv', '', x) for x in os.listdir(path)]
    idx = pd.MultiIndex.from_arrays([np.repeat(header[:], cols_per_file, axis = 0), df.columns])
    df.columns=idx
    n = len(df)

    #print('general mehods: header, cols_per_file, n, df')
    
    def ad(L):
        
        ''' Calculate Anderson-Darling test for uniform distibution based on George Marsaglia Ph.D.
            If the returned statistic is larger than the critical value then
            for the corresponding significance level, the null hypothesis that
            the data come from the chosen distribution can be rejected.'''
        
        N = len(L)
        L = sorted(L)
        A_list = []
        for i in np.arange(1, N + 1):
            A_i = (2*i-1)*np.log(L[i-1]*(1-L[N-i]))
            A_list.append(A_i)
            
        A2 = -N - (1/N)*np.sum(A_list)
        #A_crit = np.around(_Avals_norm/(1.0 + 4.0/N - 25.0/N/N), 3)
        #A_crit = A2*(1.0 + 4.0/N - 25.0/N**2)
        A_crit_table = {0.01:3.903, 0.05:2.499, 0.1:1.936,}
        A_crit = A_crit_table[alpha]
        if A2 >= 2:
            p = np.exp(-np.exp(1.0776-(2.30695-(0.43424-(0.082433-(0.008056-0.0003146*A2)*A2)*A2)*A2)*A2))
        elif A2<2:
            p = (1/np.sqrt(A2))*np.exp(-1.2337141/A2)*(2.00012+(0.247105-(0.0649821-(0.03479629-(0.011672-0.00168691*A2)*A2)*A2)*A2)*A2)
        
        c = 0.01265 + 0.1757/N
        def g1(x):
            return np.sqrt(x)*(1 - x)*(49*x - 102)
        def g2(x):
            return -0.00022633 + (6.54034 - (14.6538 - (14.458 - (8.259 - 1.91864*x)*x)*x)*x)*x
        def g3(x):
            return -130.2137 + (745.2337 - (1705.091 - (1950.646 - (1116.360 - 255.7844*x)*x)*x)*x)*x
        if A2 < c:
            err = (0.0037/N**3 + 0.00078/N**2 + 0.00006/N)*g1(A2/c)
        elif c <= A2<0.8:
            err = (0.04213/N + 0.01365/N**2)*g2((A2 - c)/(.8 - c)) 
        elif 0.8<A2:
            err = g3(A2)/N
            
        p_tot = 1-(p) #err
        return (A2, p_tot)
        
    
    def ks(x):
    
        ''' H0:  the data are uniformly distributed
            Ha:  the data are not uniformly distributed
            Reject H0 if D > D_critical'''
        
        df_ = pd.DataFrame()
        df_['index'] =pd.DataFrame(x.index)+1
        #s = x.sort_values().reset_index(drop=True)
        if type == 'm' or type == 'r':
            x = x.T
            sum = x.sum()
        elif type =='f':
            x = x
            sum = df.iloc[:, 0].sum()
        Ft = x.cumsum()/sum
        Fs = (df_['index'])/len(x)
        delta = Ft-Fs
        D = np.abs(delta).max()
        D_table = {0.01:1.63, 0.05:1.36, 0.1:1.22, 0.15:1.14, 0.2:1.07}
        D_critical = D_table[alpha]/np.sqrt(sum) 
        D_critical_tot = [D_table[alpha_]/np.sqrt(sum) for alpha_ in D_table.keys()]
        return (D, D_critical, D>D_critical, D_critical_tot)
            
    
    
    if type == 'f':
        
        #print('f_test methods: chi, ad, ks, exp_val, df', 'D_critical')
        
        df = df.droplevel(1, axis=1)
        sum = df.iloc[:, 0].sum()
        df['expected'] = df[header[0]].apply(lambda x: sum/n)
        chi_tot = []
        ks_result = []
        for h in header:
            chi = ch2(df[h], df['expected'])[1]
            chi_tot.append((chi, h))
            ks_test = ks(df[h])
            ks_result.append((ks_test, h))
        anderson = ad([x[0] for x in chi_tot])
        
        report = ('Anderson-Darling:', anderson, 'ks_test:', [(x[0][2], x[1]) for x in ks_result])
        f_stat = {'header': header, 'report': report, 'chi': chi_tot, 'ad': anderson, 'ks':ks_result, 'exp_val' : df['expected'].unique()[0], 'df':df, 'D_critical':[x[0][3] for x in ks_result][0]}
        return f_stat
        # self.report = report
        # self.chi = chi_tot
        # self.ad = anderson
        # self.ks = ks_result
        # self.exp_val = df['expected'].unique()[0]
        # self.df = df
        # self.D_critical = [x[0][3] for x in ks_result][0]
        
    elif type == 'm':
        
        #print('m_test methods: chi, ad, ks, df, df_exp', 'D_critical')
        
        df_exp = pd.DataFrame().reindex_like(df).fillna(0)
        for h in header:   
            sum = df[h].sum().sum()
            n = df[h].shape[1]*df[h].shape[0]
            df_exp[h] = sum/n
        
        p_chi2_h = []
        p_chi2 = []
        for h in header:
            for i in range(len(df)):
                p = ch2(df[h].iloc[i], df_exp[h].iloc[i])[1]
                p_chi2_h.append((p, h))
                p_chi2.append(p)
        AD_tot = []
        for i in range(len(df)):
            y = len(df)
            ad_ = ad(p_chi2[i::y]) #[:2]
            AD_tot.append(ad_)
        
        ks_test = []
        for h in header:
            for i in range(len(df)):
                x = df[h].iloc[i]
                ks_ = ks(x)
                ks_test.append((ks_, h))
        m_stat= {'header': header,'chi': p_chi2_h, 'ad': AD_tot, 'df_exp' : df_exp, 'ks' : ks_test, 'D_critical' : [x[0][3] for x in ks_test][0]}
        return m_stat
        # self.chi = p_chi2_h
        # self.ad = AD_tot
        # self.df_exp = df_exp
        # self.ks = ks_test
        # self.D_critical = [x[0][3] for x in ks_test][0]
        
    elif type == 'r':
        
        #print('r_test methods: Collective: chi, p_tot, ad, df, df_exp', '\n', 'Rows: ad_row, p_r_tot, ks, df_exp_row', 'D_critical')
        
        # Collective Rows
        df_exp = pd.DataFrame().reindex_like(df).fillna(0)
        for h in header:
            col_sum = df[h].sum(axis=0)
            row_sum = df[h].sum(axis=1)
            total_sum = col_sum.sum()
            col_df = pd.DataFrame(col_sum)
            row_df = pd.DataFrame(row_sum)
            new_df = row_df.dot(col_df.T)
            new_df = new_df / total_sum
            df_exp[h] = new_df
            
        df_chi = (df - df_exp)**2/df_exp
        chi_tot = []
        for h in header:
            chi = df_chi[h].sum().sum()
            chi_tot.append((chi, h))
        p_tot = []
        for i in range(len(chi_tot)):
            n1 = df[header[0]].shape[0]
            n2 = df[header[0]].shape[1]
            dof = (n1-1)*(n2-1)
            p = distributions.chi2.sf(chi_tot[i][0], dof)
            p_tot.append(p)
        AD_coll = ad(p_tot)
        
        
        
        # Individual Rows
        df_exp_row = pd.DataFrame().reindex_like(df).fillna(0)
        for h in header:
            row_sum = df[h].sum(axis=1)
            col_sum = df[h].sum(axis=0)
            total_sum = col_sum.sum()
            row_df = pd.DataFrame(row_sum)
            new_df = row_df/256
            for i in range(len(df_exp_row[h])):
                df_exp_row[h].iloc[i] = new_df.iloc[i]
        
        p_row_tot = []
        chi_row_tot = []
        for h in header:
            p_row = []
            for i in range(len(df[h])):
                chi = ch2(df[h].iloc[i], df_exp_row[h].iloc[i])[1]
                p = ch2(df[h].iloc[i], df_exp_row[h].iloc[i])[1]
                p_row.append(p)
            chi_row_tot.append((chi, h))
            p_row_tot.append(p_row)
        p_r_tot_flat = list(np.concatenate(p_row_tot)) #.flat)
        
        AD_row = []
        for i in range(len(df)):
            AD_row.append(ad(p_r_tot_flat[i::len(df)])) #[:2]
            #AD_row.append(ad(p_row_tot[i]))
        ks_test = []
        for h in header:
            for i in range(len(df[h])):
                x = df[h].iloc[i]
                ks_ = ks(x)
                ks_test.append((ks_, h))
        r_stat =  {'header': header,'chi': chi_tot, 'ad' :AD_coll, 'df_exp' : df_exp, 'p_tot' : p_tot,
                   'ad_row': AD_row, 'df_exp_row' : df_exp_row, 'p_value': p_row_tot, 'chi_row': chi_row_tot, 'ks'  : ks_test,'D_critical' : [x[0][3] for x in ks_test][0]}
        return r_stat
        # self.chi = chi_tot
        # self.ad =AD_coll
        # self.df_exp = df_exp
        # self.p_tot = p_tot
        # self.ad_row =AD_row
        # self.df_exp_row = df_exp_row
        # self.p_value = p_row_tot
        # self.chi_row = chi_row_tot
        # self.ks  = ks_test
        # self.D_critical = [x[0][3] for x in ks_test][0]
