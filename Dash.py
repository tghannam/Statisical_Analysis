USERNAME_PASSWORD_PAIRS = [['talal', 'ghannam']]
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP]) #external_stylesheets=[dbc.themes.SOLAR]
#auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
#server = app.server

app.layout = html.Div([
                dbc.Row([dbc.Col([
            
            #DashBoard Heading
                    dbc.Row([
                        
                        #Heading logo + hyperlink
                        dbc.Col(dcc.Link([html.Img( src=app.get_asset_url('theon-logo-horizontal-white.webp'),
                                            height='56px',
                                            className='mt-5')
                                        ], href= 'https://theontechnology.com/', target = "_blank"), sm=4, lg=12, md=3, width=4),
                        
                            ], id="heading"),
                            ]),
                            
                        dbc.Col([dbc.Card(
                                    dbc.CardBody([html.H3(children = [html.I(className="h-50"),"Raw Data Statistical Tests"], className="card-title", style = {'color':'#CFFF00'}),
                                        ], #persistence = True, persistence_type='local', className = 'select_box'
                                        ),color = 'black', inverse=True, outline= False, className='text-start m-3')
                                 ], width = 8
                                ),
                        ]),
                    
                    dbc.Row(dbc.Card(dbc.CardBody([],                                     
                                        className= 'border-top border-3 border-success'
                                                        ), color = 'black', inverse=True, outline= False,
                                             ),
                        ),
                        
                    #Plots pick   
                    dbc.Row([
                        dbc.Col([
                                html.H5(children = [html.I(className="bi bi-caret-right-fill me-2"), 'Chose Data Type:'], style = {'color':'#CFFF00'}),
                                dbc.RadioItems(data_type, value = data_type[0], id = 'type-picker',className="btn-group",
                                                inputClassName="btn-check",
                                                labelClassName="btn btn-outline-#CFFF00",
                                                labelCheckedClassName="active",
                                                label_checked_style={'color':'#CFFF00'}, 
                                                style = {'color':'#CFFF00',}),
                                #Data type description                  
                                dbc.Row(dbc.Card(dbc.CardBody([html.H5("Data Type Description", className="card-title", style = {'color':'#CFFF00', }, ),
                                                            dcc.Markdown(id='data-explain',  link_target="_blank", className='card-text', style={'textAlign': 'justify'})]), 
                                            color = 'black', inverse=True, outline= False),
                                        justify="center"
                                        ),
                                #Plot description
                                dbc.Row(dbc.Card(dbc.CardBody([html.H5("Plot Description", className="card-title", style = {'color':'#CFFF00'}),
                                                            dcc.Markdown(id='plot-explain',  link_target="_blank", className='card-text',style={'textAlign': 'justify'})]), 
                                            color = 'black', inverse=True, outline= False)
                                        )
                                ], width = {'size': 3, 'offset':0, 'order': 'first' }, md={'size': 3, 'offset':0, 'order': 'first' }),
                                
                                
                        #Graph area
                        #Data picker
                        dbc.Col([
                                html.P(children = [html.I(className="bi bi-caret-right-fill me-2"), 'Chose Data:'], style = {'color':'#CFFF00'}),
                                dcc.Dropdown(id = 'data-picker', multi = True, style={'color': 'blue', 'font-size': 20, 'width':'90%'},  ),#value = data_dict['F'][3]
                                dbc.Row(html.Br()   ),
                                html.P(children = [html.I(className="bi bi-caret-right-fill me-2"), 'Chose Plot:'], style = {'color':'#CFFF00'}),
                                dbc.RadioItems(value = 'chi',id='plot-picker',className="btn-group",
                                                inputClassName="btn-check",
                                                labelClassName="btn btn-outline-#CFFF00",
                                                labelCheckedClassName="active", 
                                                label_checked_style={'color':'#CFFF00'}, 
                                                style = {'color':'#CFFF00',} ), #value = 'chi',
                                #v value = data_dict['F'][3],
                             
                                #Progress animation
                                dcc.Interval(id="progress-interval", n_intervals=0, interval=500),
                                #dbc.Progress(value=80, id="animated-progress", animated=False, striped=True),
                                
                                #Graph
                                dbc.Row(dbc.Card(
                                            dcc.Loading(children=[dcc.Graph(id="plot", style={'width':'90%','height': '80vh', 'float': 'left','display':'inline-block'},
                                                                            figure={'layout': {'plot_bgcolor': '#060606', 'paper_bgcolor': '#060606' }})], 
                                                        color="blue", type="cube", fullscreen=False, debug = True, className='Loading Plot'),
                                            # spinner_style={"width": "10rem", "height": "10rem"}),
                                            # spinnerClassName="spinner"),
                                            # dcc.Loading(children=[dcc.Graph(id="loading-output")], color="#119DFF", type="dot", fullscreen=True,),
                                            #dbc.Spinner(children=[dcc.Graph(id="plot", style={'width':'90%','height': '80vh', 'float': 'left','display':'inline-block'})], size="lg", color="primary", type="border", fullscreen=True,),
                                            color = 'black', inverse=True, outline= False),
                                        
                                       
                                        ),]
                                # dcc.Graph(id = 'plot', style={'width':'90%','height': '80vh', 'float': 'left','display':'inline-block'}) ]
                                    #html.P('Chose R-test type:'), dcc.RadioItems(id = 'R-type', options = ['chose']),
                                    #html.Button(id = 'submit-button', n_clicks=0, children='Submit Here', style={'fontSize':24}),
                                    #figure={'data':[go.Scatter(x=np.arange(10), y = np.arange(10))]} 
                                    )
                    
                                ], style = {'heigt' :'50%'}),
            
    #bottom logos + hyperlinks
    dbc.Row([
            dbc.Row(html.Br()),
                dbc.Col([
                    dbc.Card([dbc.CardLink([dbc.CardImg( src=app.get_asset_url('theon-logo-horizontal-white.webp'), top=True, style={"width": "10rem"})], 
                                               href= 'https://theontechnology.com/', target = "_blank")], 
                             color = 'black', inverse=True, outline= False
                             )],
                        ),
                dbc.Col([
                    dbc.Card([dbc.CardLink([dbc.CardImg( src=app.get_asset_url('linkedin-icon.webp'), top=True, style={"width": "3rem"}, className="display-5")], 
                                               href= 'https://www.linkedin.com/company/theon-technology/', target = "_blank"), 
                             dbc.CardLink([dbc.CardImg( src=app.get_asset_url('youtube-icon.webp'), top=True, style={"width": "3rem"}, className="display-5")], 
                                               href= 'https://www.youtube.com/channel/UCAMwwJNdJDo7voaYeNLlAhA', target = "_blank")],
                             
                             color = 'black', inverse=True, outline= False, style= {'display':'inline-block', 'float':'right'}
                             )],
                        ),

            ]),
    #Disclaimer
    dbc.Row(dbc.Card(dbc.CardBody([dcc.Markdown("© 2023 All Rights Reserved. Designed by Talal Ghannam.", style = {'color':'white', 'size':'3', 'font_size':' 1.4rem', }),
                                        dcc.Markdown(id='disclaimer',  link_target="_blank", className='card-text',)], 
                                  className= 'border-top border-3 border-success'), 
                        color = 'black', inverse=True, outline= False)
                    )                   
                                                
                        ])





@app.callback(Output('data-picker','options'), [Input('type-picker', 'value')])
def data_picker(type_pick):
    return data_dict[type_pick]

@app.callback(Output('plot-picker','options'), [Input('type-picker', 'value')])
def plot_picker(type_pick):
    if type_pick == 'R':
        return ['chi', 'ks', 'ks_D_below', 'ad', 'chi_row', 'ad_row']
    if type_pick == 'M':
        return ['chi', 'ks', 'ad']
    if type_pick == 'F':
        return ['chi', 'ks', 'ks_1', 'ad']

# @app.callback(
#     [Output("progress", "value"), Output("progress", "label")],
#     [Input("progress-interval", "n_intervals")],
# )
# def update_progress(n):
#     # check progress of some background process, in this example we'll just
#     # use n_intervals constrained to be in 0-100
#     progress = min(n % 110, 100)
#     # only add text after 5% progress to ensure text isn't squashed too much
#     return progress, f"{progress} %" if progress >= 5 else ""

@app.callback(Output('plot','figure'), 
              [Input('type-picker', 'value'), Input('plot-picker', 'value'),Input('data-picker', 'value'),]) #Input('data-picker', 'value'), [State('plot-picker', 'options')],   Input('submit-button', 'n_clicks')

def plot_data(type_pick, plot_pick, data_pick,):
         
    if type_pick == 'R':
        #['chi', 'ks', 'ks_D_below', 'ad', 'chi_row', 'ad_row']
        #chi test
        if plot_pick == 'chi':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                r_stat = stat_calc(path, 'r', alpha=0.05)
                names.append(name)
                round = len(r_stat['header'])
                rounds.append(round)
                chi_1 = r_stat['chi']
                trace = go.Scatter(x = np.arange(1, len(chi_1)+1)/len(chi_1), y = sorted([x[0] for x in chi_1]), mode ='lines+markers', name='chi_'+name)
                data.append(trace)
            layout = go.Layout(title='chi_square for {}, #tests: {} ({}_test)'.format(names, rounds, type_pick),
                               template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_chi = go.Figure(data, layout)
            # fig_chi.add_hline(y=np.mean([x[0] for x in chi_1]), line_width=1, line_dash="dash", line_color="red", annotation_text='mean_'+name, annotation_position="bottom right")
            # fig_chi.add_hline(y=np.median([x[0] for x in chi_1]), line_width=1, line_dash="dash", line_color="orange", annotation_text='median_'+name, annotation_position="bottom left")
            fig_chi.update_xaxes(title_text = 'Individual Tests')
            fig_chi.update_yaxes(title_text = 'p_value')
            fig_chi.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            fig_chi.update_layout(autosize=False, width=800, height=800,)
            return fig_chi
                
        elif plot_pick == 'chi_row':
            data_row = []   
            names = []
            rounds = []
            for data_ in data_pick: 
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                r_stat = stat_calc(path, 'r', alpha=0.05)
                names.append(name)
                round = len(r_stat['header'])
                rounds.append(round)
                chi_1_row = r_stat['chi_row']
                trace= go.Scatter(x = np.arange(1, len(chi_1_row)+1)/len(chi_1_row), y = sorted([x[0] for x in chi_1_row]), mode ='lines+markers', name='chi_'+name)
                data_row.append(trace)
            layout_row = go.Layout(title='chi_square for{}, #tests: {} ({}_test)'.format(names, rounds, type_pick),
                                   template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_chi_row = go.Figure(data_row, layout_row)
            fig_chi_row.add_hline(y=np.mean([x[0] for x in chi_1_row]), line_width=1, line_dash="dash", line_color="red", annotation_text='mean_'+name, annotation_position="bottom right")
            fig_chi_row.add_hline(y=np.median([x[0] for x in chi_1_row]), line_width=1, line_dash="dash", line_color="orange", annotation_text='median_'+name, annotation_position="bottom left")
            fig_chi_row.update_xaxes(title_text = 'Individual Tests')
            fig_chi_row.update_yaxes(title_text = 'p_value')
            fig_chi.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            return fig_chi_row

        #ks test
        elif plot_pick == 'ks_D_below':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                r_stat = stat_calc(path, 'r', alpha=0.05)
                names.append(name)
                round = len(r_stat['header'])
                rounds.append(round)
                ks_1_below = [(x[0][0], x[1]) for x in r_stat['ks'] if x[0][0] <= x[0][1]]
                ks_1_list = []
                for h in r_stat['header']:
                    ks_ = []
                    for x in ks_1_below:
                        if x[1] == h:
                            ks_.append(x[0])
                    ks_1_list.append(ks_)
                header_1 =r_stat['header']
                y_1 = [len(x) for x in ks_1_list]
                trace = go.Bar(x = header_1, y =y_1,text = y_1,)
                data.append(trace)
            layout_1 = go.Layout(title='Number of rows in each of {} tests (for {} {}_row test) that their respective D_value is leass than D_critical for that specific test. <br>Mean = {}, min = {}, max = {}'.format(rounds,names, type_pick, np.mean(y_1), min(y_1), max(y_1)),
                                 template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_1 = go.Figure(data, layout_1)
            fig_1.update_xaxes(title_text = 'Individual Tests')
            fig_1.update_yaxes(title_text = 'D_value')
            fig_1.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            return fig_1

        elif plot_pick == 'ks':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                r_stat = stat_calc(path, 'r', alpha=0.05)
                names.append(name)
                round = len(r_stat['header'])
                rounds.append(round)
                ks_1 = r_stat['ks']
                D_crit_1 = r_stat['D_critical']
                
                # df_1 = pd.DataFrame({'x': np.arange(1, len(ks_1)+1)/len(ks_1), 'y1': sorted([x[0][0] for x in ks_1])})
                # df_1_c = pd.DataFrame({'x': np.arange(1, len(ks_1)+1)/len(ks_1), 'y2': test_1.D_critical[0]})

                # fig_1 = intersection_point(df_1, df_1_c, type_pick)
                # fig_1.update_xaxes(title_text = 'Individual Tests')
                # fig_1.update_yaxes(title_text = 'D_value')
                # layout_1 = go.Layout(title='ks_test D_critical for {} for alpha = [0.01], #tests: {} for {}_test'.format(name, len(test_1.header), type_pick))
                # fig_1.layout = layout_1
                # self.ks = fig_1
                trace = go.Scatter(x = np.arange(1, len(ks_1)+1)/len(ks_1), y = sorted([x[0][0] for x in ks_1]), mode ='lines+markers', name='KS_'+name)
                data.append(trace)
            layout = go.Layout(title='ks_test D_value for {}, #tests: {} ({}_test)]'.format(names, rounds, type_pick),
                               template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_ks = go.Figure(data, layout)
            fig_ks.update_xaxes(title_text = 'Individual Tests')
            fig_ks.update_yaxes(title_text = 'D_value')
            fig_ks.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            
            return fig_ks
            
            
        #AD test
        elif plot_pick == 'ad_row':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                r_stat = stat_calc(path, 'r', alpha=0.05)
                names.append(name)
                round = len(r_stat['header'])
                rounds.append(round)
                ad_1_row = r_stat['ad_row']
                len_1 = len([x[0] for x in r_stat['ad_row'] if 0.01<x[1]<0.99])
                trace = go.Scatter(x = np.arange(1, len(ad_1_row)+1)/len(ad_1_row), y = sorted([x[1] for x in ad_1_row]), mode ='lines+markers', name='AD_'+name+' /{}'.format(len_1))
                data.append(trace)
            layout = go.Layout(title='AD_test_row plot for {}, #tests: {} ({}_test)'.format(names, rounds, type_pick),
                               template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_ad_row = go.Figure(data, layout)
            fig_ad_row.add_hline(y=np.mean([x[1] for x in ad_1_row]), line_width=1, line_dash="dash", line_color="red", annotation_text='mean_'+name, annotation_position="bottom right")
            fig_ad_row.add_hline(y=np.median([x[1] for x in ad_1_row]), line_width=1, line_dash="dash", line_color="orange", annotation_text='median_'+name, annotation_position="top right")
            fig_ad_row.update_xaxes(title_text = 'Individual rows')
            fig_ad_row.update_yaxes(title_text = '1-p')
            fig_ad_row.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            return fig_ad_row
        
        #collective
        elif plot_pick == 'ad':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                r_stat = stat_calc(path, 'r', alpha=0.05)
                names.append(name)
                round = len(r_stat['header'])
                rounds.append(round)
                ad_1 = r_stat['ad']
                p_tot_1 = r_stat['p_tot']
                trace = go.Scatter(x = np.arange(1, len(p_tot_1)+1)/len(p_tot_1), y = sorted(p_tot_1), mode ='lines+markers', name='P_'+name+', AD = {}'.format(np.round(ad_1[1], 3)))
                data.append(trace)
            layout = go.Layout(title='AD_test plot for {}, #tests: {} ({}_test)'.format(names, rounds, type_pick),
                               template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_ad = go.Figure(data, layout)
            fig_ad.update_xaxes(title_text = 'Individual tests')
            fig_ad.update_yaxes(title_text = '1-p')
            fig_ad.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            return fig_ad


    elif type_pick == 'F':
        #['chi', 'ks', 'ks_1',  'ad']
        #Chi
        if plot_pick == 'chi':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                f_stat = stat_calc(path, 'f', alpha=0.05)
                names.append(name)
                round = len(f_stat['header'])
                rounds.append(round)
                chi_1 = f_stat['chi']
                trace = go.Scatter(x = np.arange(1, len(chi_1)+1)/len(chi_1), y = sorted([x[0] for x in chi_1]), mode ='lines+markers', name='chi_'+name)
                data.append(trace)
            layout = go.Layout(title='chi_square for {}, #tests: {} ({}_test)'.format(names, rounds,type_pick),
                               template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_chi = go.Figure(data, layout)
            fig_chi.add_hline(y=np.mean([x[0] for x in chi_1]), line_width=1, line_dash="dash", line_color="red", annotation_text='mean_'+name, annotation_position="bottom right")
            fig_chi.add_hline(y=np.median([x[0] for x in chi_1]), line_width=1, line_dash="dash", line_color="orange", annotation_text='median_'+name, annotation_position="bottom left")
            fig_chi.update_xaxes(title_text = 'Individual Tests')
            fig_chi.update_yaxes(title_text = 'p_value')
            fig_chi.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            fig_chi.update_layout(autosize=False, width=1000, height=500,)
            return fig_chi
    
        #KS
        elif plot_pick == 'ks_1':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                f_stat = stat_calc(path, 'f', alpha=0.05)
                ks_1 = f_stat['ks']
                D_crit_1 = f_stat['D_critical']
                names.append(name)
                round = len(f_stat['header'])
                rounds.append(round)
                df_1 = pd.DataFrame({'x': np.arange(1, len(ks_1)+1)/len(ks_1), 'y1': sorted([x[0][0] for x in ks_1])})
                df_1_c = pd.DataFrame({'x': np.arange(1, len(ks_1)+1)/len(ks_1), 'y2': D_crit_1[0]})

                fig_1 = intersection_point(df_1, df_1_c, type_pick)
                fig_1.update_xaxes(title_text = 'Individual Tests')
                fig_1.update_yaxes(title_text = 'D_value')
            layout_1 = go.Layout(title='ks_test D_critical for {} for alpha = [0.01], #tests: {} for {}_test'.format(names, rounds, type_pick),
                                 template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_1.layout = layout_1
            fig_1.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            return fig_1
        
        elif plot_pick == 'ks':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                f_stat = stat_calc(path, 'f', alpha=0.05)
                names.append(name)
                round = len(f_stat['header'])
                rounds.append(round)
                ks_1 = f_stat['ks']
                D_crit_1 = f_stat['D_critical']
                trace = go.Scatter(x = np.arange(1, len(ks_1)+1)/len(ks_1), y = sorted([x[0][0] for x in ks_1]), mode ='lines+markers', name='KS_'+name)
                data.append(trace)
            layout = go.Layout(title='ks_test D_value for {}, #tests: {} ({}_test)]'.format(names, rounds, type_pick),
                               template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_ks = go.Figure(data, layout)
            fig_ks.update_xaxes(title_text = 'Individual Tests')
            fig_ks.update_yaxes(title_text = 'D_value')
            fig_ks.add_hline(y=D_crit_1[0], line_width=1, line_dash="dash", line_color="red", annotation_text='0.01_'+name, annotation_position="bottom right")
            fig_ks.add_hline(y=D_crit_1[1], line_width=1, line_dash="dash", line_color="orange", annotation_text='0.05_'+name, annotation_position="bottom left")
            fig_ks.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            return fig_ks
        
        #AD
        elif plot_pick == 'ad':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                f_stat = stat_calc(path, 'f', alpha=0.05)
                names.append(name)
                round = len(f_stat['header'])
                rounds.append(round)
                ad_1 = f_stat['ad']
                trace = go.Scatter(x = np.arange(1, len(ad_1)+1)/len(ad_1), y = [ad_1[1]], mode ='lines+markers', name='AD_'+name+' AD = {}'.format(ad_1[1]))
                data.append(trace)
            layout = go.Layout(title='AD plot for {}, #tests: {} ({}_test)'.format(names, rounds, type_pick),
                               template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_ad = go.Figure(data, layout)
            fig_ad.update_xaxes(title_text = 'Individual tests')
            fig_ad.update_yaxes(title_text = '1-p')
            fig_ad.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            return fig_ad
        
        
    elif type_pick == 'M': 
        #['chi', 'ks',  'ad']
        #chi
        if plot_pick == 'chi':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                m_stat = stat_calc(path, 'm', alpha=0.05)
                names.append(name)
                round = len(m_stat['header'])
                rounds.append(round)
                chi_1 = m_stat['chi']
                trace = go.Scatter(x = np.arange(1, len(chi_1)+1)/len(chi_1), y = sorted([x[0] for x in chi_1]), mode ='lines+markers', name='chi_'+name)
                data.append(trace)
            layout = go.Layout(title='chi_square for {}, #tests: {} ({}_test)'.format(names, rounds,type_pick),
                               template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_chi = go.Figure(data, layout)
            fig_chi.add_hline(y=np.mean([x[0] for x in chi_1]), line_width=1, line_dash="dash", line_color="red", annotation_text='mean_'+name, annotation_position="bottom right")
            fig_chi.add_hline(y=np.median([x[0] for x in chi_1]), line_width=1, line_dash="dash", line_color="orange", annotation_text='median_'+name, annotation_position="bottom left")
            fig_chi.update_xaxes(title_text = 'Individual Tests')
            fig_chi.update_yaxes(title_text = 'p_value')
            fig_chi.update_xaxes(title_text = 'Individual n rows for each m test (total of nxm points)')
            fig_chi.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            return fig_chi
    
        elif plot_pick == 'ks':
                data = []
                names = []
                rounds = []
                for data_ in data_pick:
                    path = data_ + '//' + type_pick.lower()+ '_test'
                    name = data_
                    m_stat = stat_calc(path, 'm', alpha=0.05)
                    names.append(name)
                    round = len(m_stat['header'])
                    rounds.append(round)
                    ks_1 = m_stat['ks']
                    D_crit_1 = m_stat['D_critical']
                    trace = go.Scatter(x = np.arange(1, len(ks_1)+1)/len(ks_1), y = sorted([x[0][0] for x in ks_1]), mode ='lines+markers', name='KS_'+name)
                    data.append(trace)
                layout = go.Layout(title='ks_test D_value for {}, #tests: {} ({}_test)]'.format(names, rounds, type_pick),
                                   template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
                fig_ks = go.Figure(data, layout)
                fig_ks.update_xaxes(title_text = 'Individual Tests')
                fig_ks.update_yaxes(title_text = 'D_value')
                fig_ks.add_hline(y=D_crit_1[0], line_width=1, line_dash="dash", line_color="red", annotation_text='0.01_'+name, annotation_position="bottom right")
                fig_ks.add_hline(y=D_crit_1[1], line_width=1, line_dash="dash", line_color="orange", annotation_text='0.05_'+name, annotation_position="bottom left")
                fig_ks.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
                return fig_ks
       

        #AD_plot
        elif plot_pick == 'ad':
            data = []
            names = []
            rounds = []
            for data_ in data_pick:
                path = data_ + '//' + type_pick.lower()+ '_test'
                name = data_
                m_stat = stat_calc(path, 'm', alpha=0.05)  
                names.append(name)
                round = len(m_stat['header'])
                rounds.append(round)  
                ad_1 = m_stat['ad']
                trace = go.Scatter(x = np.arange(1, len(ad_1)+1)/len(ad_1), y = sorted([x[1] for x in ad_1]), mode ='lines+markers', name='AD_'+name)
                data.append(trace)
            layout = go.Layout(title='AD_test for {}, #tests: {} ({}_test)'.format(names, rounds, type_pick),
                               template = 'plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            fig_ad = go.Figure(data, layout)
            fig_ad.add_hline(y=np.mean([x[1] for x in ad_1]), line_width=1, line_dash="dash", line_color="red", annotation_text='mean_'+name, annotation_position="bottom right")
            fig_ad.add_hline(y=np.median([x[1] for x in ad_1]), line_width=1, line_dash="dash", line_color="orange", annotation_text='median_'+name, annotation_position="top right")
            fig_ad.update_xaxes(title_text = 'Individual rows')
            fig_ad.update_yaxes(title_text = '1-p')
            fig_ad.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
            return fig_ad
    
#Data Type Description callback
@app.callback(Output('data-explain', 'children'), [Input('type-picker', "value")])
def update_chart_info(picker_test):
    if picker_test == 'F':
        text = """We look at the frequency of all the possible 8 bits sections at all iterations at all numbers included in test and check if the frequency of the different possible
        segments can reject the random hypothesis. """
    elif picker_test == 'M':
        text = """This is a frequency test of all possible 8 bits sections at specific iterations at all numbers included in the test, and we did it for all the iterations. 
        We always look at 8 bits segments, including in the case of 4×64. This is because working with a table of 264 is behind the abilities of our tools. 
        So even though 4×64 has only 4 iterations, we treat it as 32 iterations (8×32)."""
    elif picker_test == 'R':
        text = """
        We investigate the frequency of all the connected pairs of 8 bits segments (i.e., 64 bits number of 8 segments of 8 bits has 7 pairs). For every given 8 bits combination, 
        we count how many times any 8 bits combination appears in the next iteration) so if P(B/A) = P(B), then P(B/A) is also uniform (where A and B are 8 bits of different iterations). 
        Or in other words that there is no correlation between A and B. We use two methods: 1- look at all test pairs together (to check general distribution). 
        2- split the pairs based on the first segment and look at each one separately (to check for conditional probability).
        """
    else:
        return ""
    return [text]

#Plot Description callback
@app.callback(Output('plot-explain', 'children'), [Input('plot-picker', "value")])
def update_chart_info(picker_test):
    if picker_test == 'chi':
        text = "The Chi-Square (CS) Test: We calculate the chi-square p-values and compare them to the critical value of 0.01 (1%). "
    elif picker_test == 'ks':
        text = """
        We order the 8 bits segments based on their values and calculate the KS statistic. We then compare the results to the KS critical value of 0.01 (D = 1.63/√(number of samples)). 
        In essence, the test answers the question, “What is the probability that this collection of samples could have been drawn from a probability distribution (uniform in our case).”
        """
    elif picker_test == 'ks_1':
        text = """
        We order the 8 bits segments based on their values and calculate the KS statistic. We then compare the results to the KS critical value of 0.01 (D = 1.63/√(number of samples)). 
        In essence, the test answers the question, “What is the probability that this collection of samples could have been drawn from a probability distribution (uniform in our case).
        """
    elif picker_test == 'ad':
        text = """
        The Anderson-Darling (AD) Test: The Anderson-Darling test is a statistical test that determines whether a given sample of data is drawn from a given probability distribution
        (uniform in our case) with an additional check that the uniform origin is of random distribution. We perform the AD test on the CS performed above to check if the p-values 
        are uniformly distributed as expected based on the hypothesis of random distribution. 
        """
    elif picker_test == 'ks_D_below':
        text = """
        The number of rows (for each testing round) that are below D-critical. 
        """
    elif picker_test == 'chi_row':
        text = """
        For each test, we calculate the chi-square p-values for pairs with the same first segment (a row in our matrix of results).  
        """
    elif picker_test == 'ad_row':
        text = """
        For each test, we calculate the chi-square p-values for pairs with the same first segment (a row in our matrix of results). 
        We then take all the CS’s p-values from the different tests and calculate the AD p-values for them. In total, we got 128 AD values for each case 
        (the number of 8 bits possibilities). 
        """
    else:
        return ""
    return [text]
          
        #KS_plot     
        # elif plot_pick == 'ks_1':
        #     data = []
        #     for data_ in data_pick:
        #         path = data_ + '//' + type_pick.lower()+ '_test'
        #         name = data_
        #         m_stat = stat_calc(path, 'm', alpha=0.05)
        #         ks_1 = m_stat['ks_1']
        #         D_crit_1 = m_stat['D_critical']  
                
        #         df_1 = pd.DataFrame({'x': np.arange(1, len(ks_1)+1)/len(ks_1), 'y1': sorted([x[0][0] for x in ks_1])})
        #         df_1_c = pd.DataFrame({'x': np.arange(1, len(ks_1)+1)/len(ks_1), 'y2': D_crit_1[0]})

        #         fig_1 = intersection_point(df_1, df_1_c, type_pick)
        #         fig_1.update_xaxes(title_text = 'Individual Tests')
        #         fig_1.update_yaxes(title_text = 'D_value')
        #     layout_1 = go.Layout(title='ks_test D_critical for {} for alpha = [0.01], #tests: {} for {}_test'.format(name, m_stat['header'], type_pick))
        #     fig_1.layout = layout_1
        #     return fig_1
    
            # data = [go.Scatter(x = np.arange(1, len(ks_1)+1)/len(ks_1), y = sorted([x[0][0] for x in ks_1]), mode ='lines+markers', name='KS_'+'{}'.format(self.name_1))]
            # layout = go.Layout(title='ks_test D_value for {}, #tests: {} ({}_test)]'.format(self.name_1, len(test_1.header), self.type))
            # fig_ks = go.Figure(data, layout)
            # fig_ks.update_xaxes(title_text = 'Individual Tests')
            # fig_ks.update_yaxes(title_text = 'D_value')
            
if __name__ =='__main__':
    app.run_server(debug=False, use_reloader=False)
