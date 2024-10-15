def intersection_point(df_1, df_2, type):
        
        def _rect_inter_inner(x1,x2):
            n1=x1.shape[0]-1
            n2=x2.shape[0]-1
            X1=np.c_[x1[:-1],x1[1:]]
            X2=np.c_[x2[:-1],x2[1:]]
            S1=np.tile(X1.min(axis=1),(n2,1)).T
            S2=np.tile(X2.max(axis=1),(n1,1))
            S3=np.tile(X1.max(axis=1),(n2,1)).T
            S4=np.tile(X2.min(axis=1),(n1,1))
            return S1,S2,S3,S4

        def _rectangle_intersection_(x1,y1,x2,y2):
            S1,S2,S3,S4=_rect_inter_inner(x1,x2)
            S5,S6,S7,S8=_rect_inter_inner(y1,y2)

            C1=np.less_equal(S1,S2)
            C2=np.greater_equal(S3,S4)
            C3=np.less_equal(S5,S6)
            C4=np.greater_equal(S7,S8)

            ii,jj=np.nonzero(C1 & C2 & C3 & C4)
            return ii,jj

        def intersection(x1,y1,x2,y2):

            ii,jj=_rectangle_intersection_(x1,y1,x2,y2)
            n=len(ii)

            dxy1=np.diff(np.c_[x1,y1],axis=0)
            dxy2=np.diff(np.c_[x2,y2],axis=0)

            T=np.zeros((4,n))
            AA=np.zeros((4,4,n))
            AA[0:2,2,:]=-1
            AA[2:4,3,:]=-1
            AA[0::2,0,:]=dxy1[ii,:].T
            AA[1::2,1,:]=dxy2[jj,:].T

            BB=np.zeros((4,n))
            BB[0,:]=-x1[ii].ravel()
            BB[1,:]=-x2[jj].ravel()
            BB[2,:]=-y1[ii].ravel()
            BB[3,:]=-y2[jj].ravel()

            for i in range(n):
                try:
                    T[:,i]=np.linalg.solve(AA[:,:,i],BB[:,i])
                except:
                    T[:,i]=np.NaN


            in_range= (T[0,:] >=0) & (T[1,:] >=0) & (T[0,:] <=1) & (T[1,:] <=1)

            xy0=T[2:,in_range]
            xy0=xy0.T
            return xy0[:,0],xy0[:,1]

        # plotly figure
        x,y=intersection(np.array(df_1['x'].values.astype('float')),np.array(df_1['y1'].values.astype('float')),
                        np.array(df_2['x'].values.astype('float')),np.array(df_2['y2'].values.astype('float')))
        
        data = [go.Scatter(x=df_1['x'], y=df_1['y1'], mode = 'lines', name='D_value'),go.Scatter(x=df_2['x'], y=df_2['y2'], mode = 'lines', name='D_critical')]
        '''fig = go.Figure(data=
        fig.add_traces()'''
        fig = go.Figure(data)
        fig.update_xaxes(title_text = 'Individual Tests')
        fig.update_yaxes(title_text = 'D_value')
        
        if type != 'F':
            fig.add_traces(go.Scatter(x=x, y=y,
                                    mode = 'markers',
                                    marker=dict(line=dict(color='black', width = 2),
                                                    symbol = 'diamond',
                                                    size = 14,
                                                    color = 'rgba(255, 255, 0, 0.6)'),
                                        name = 'intersect at x = {} and y = {}'.format(str(round(x[0], 4)), str(round(y[0], 5)))))
            '''fig.add_annotation(x=x[0], y=y[0],
                            # text="intersect",
                            text = 'x = ' + str(round(x[0], 4)) + ' and y = ' + str(round(y[0], 5)),
                            font=dict(family="sans serif",
                                        size=18,
                                        color="black"),
                            ax=0,
                            ay=-100,
                            showarrow=True,
                            arrowhead=1)'''
        else:
            fig.add_traces(go.Scatter(x=x, y=y,
                                    mode = 'markers',
                                    marker=dict(line=dict(color='black', width = 2),
                                                symbol = 'diamond',
                                                size = 14,
                                                color = 'rgba(255, 255, 0, 0.6)'),
                                    name = 'intersect at x = {} and y = {}'.format(str(x), str(y))))
        return fig
