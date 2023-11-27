import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import random
from PIL import Image
import graphviz
import pydeck as pdk
from datetime import time
from datetime import datetime

st.set_page_config(layout='wide')
st.sidebar.header("General Features 🎑")

def Display_almost_anything():
    st.markdown('''
    # Display almost anything
    
    ## How to display and style data?

    Using Streamlit you can do almost everything: draw chars, diagrams, show images, dataframes, write text and ect.
    At first, I need to present *st.write* and *magic commands*.

    #### ***st.write***
    This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, write() has some unique properties:
    - You can pass in multiple arguments, all of which will be written.
    - Its behavior depends on the input types as follows.
    - It returns None, so its "slot" in the App cannot be reused.
    
    **Function signature**: *st.write(*args, unsafe_allow_html=False, **kwargs)*
    ''')

    if st.toggle(('Show write examples')):
        tab1, tab2 = st.tabs(['Outputs', 'Code'])
        with tab1:
            st.write('Hello, *World!* :sunglasses:')

            st.divider()

            st.write(pd.DataFrame({
                'first column': [1, 2, 3, 4],
                'second column': [10, 20, 30, 40],
            }))
            st.divider()

            df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
            c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
            st.write(c)

        with tab2:
            st.code('''
                import streamlit as st
                import pandas as pd

                st.write('Hello, *World!* :sunglasses:')

                st.divider() 

                st.write(pd.DataFrame({ 'first column': [1, 2, 3, 4],
                                        'second column': [10, 20, 30, 40] }))

                st.divider()

                df = pd.DataFrame( np.random.randn(200, 3), columns=['a', 'b', 'c'])
                c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
                st.write(c)
                ''')

    st.markdown('\n')

    st.markdown('''
    #### ***Magic commands***
    
    Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data, charts) 
    without having to type an explicit command at all. Just put the thing you want to show on its own line of code, 
    and it will appear in your app. Here's an example:
    ''')

    if st.toggle(('Show magic examples')):
        tab3, tab4 = st.tabs(['Outputs', 'Code'])
        with tab3:
            df = pd.DataFrame({'col1': [1, 2, 3]})
            df

            st.divider()

            x = 10
            'x', x

            st.divider()

            # Also works with most supported chart types

            arr = np.random.normal(1, 1, size=100)
            fig, ax = plt.subplots()
            ax.hist(arr, bins=20)
            fig

        with tab4:
            st.code('''
                        import pandas as pd
            df = pd.DataFrame({'col1': [1,2,3]})
            df  # 👈 Draw the dataframe

            x = 10
            'x', x  # 👈 Draw the string 'x' and then the value of x

            # Also works with most supported chart types
            import matplotlib.pyplot as plt
            import numpy as np

            arr = np.random.normal(1, 1, size=100)
            fig, ax = plt.subplots()
            ax.hist(arr, bins=20)

            fig  # 👈 Draw a Matplotlib chart
            ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
    ##### Differences in Use 
    
    Although these methods are pretty similar, there are some reasons to use magic commands to get some additional 
    advantages:
    1. Magic and *st.write()* inspect the type of data that you've passed in, and then decide how to best render it in 
    the app. Sometimes you want to draw it another way. For example, instead of drawing a dataframe as an interactive 
    table, you may want to draw it as a static table by using *st.table(df)*
    2. The second reason is that other methods return an object that can be used and modified, either by adding data to 
    it or replacing it
    3. Finally, if you use a more specific Streamlit method you can pass additional arguments to customize its behavior
    ''')

    return None

def Text_elements():
    st.markdown('''
    # Text elements
    
    In Streamlit you can use both Markdown and LaTeX write text and formulas using their own syntax. 
    It is also possible to insert code.
    ''')
    tab1, tab2 = st.tabs(['Text', 'Code'])
    with tab1:
        st.markdown(
            ''' :red[Streamlit] :orange[can] :green[write] :blue[text]. ''')

        st.divider()

        st.text('This is some text.')

        st.divider()

        st.latex(r'''
                        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
                        \sum_{k=0}^{n-1} ar^k =
                        a \left(\frac{1-r^{n}}{1-r}\right)
                        ''')
    with tab2:
        st.code('''
        st.markdown(' :red[Streamlit] :orange[can] :green[write] :blue[text]. ')
        
        st.text('This is some text.')
        
        st.latex(r'
                a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
                \sum_{k=0}^{n-1} ar^k =
                a \left(\\frac{1-r^{n}}{1-r}\\right)
                ')
        ''')
    return None

def Data_elements():
    st.markdown('''
    # Data elements
    
    Using Streamlit you can display data in many ways''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
    ### **st.dataframe**
    Display a dataframe as an interactive table.
    
    This command works with dataframes from Pandas, PyArrow, Snowpark, and PySpark. It can also display several other types 
    hat can be converted to dataframes, e.g. numpy arrays, lists, sets and dictionaries.
    ''')
    if st.toggle('Show dataframe examples'):
        tab1, tab2 = st.tabs(['Output', 'Code'])
        with tab1:
            df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

            st.dataframe(df)

            st.divider()
            st.markdown('''You can customize the dataframe via ***column_config***,  &nbsp; ***hide_index***, &nbsp; or 
            ***column_order***:''')

            df0 = pd.DataFrame(
                {
                    "name": ["Roadmap", "Extras", "Issues"],
                    "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app",
                            "https://issues.streamlit.app"],
                    "stars": [random.randint(0, 1000) for _ in range(3)],
                    "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
                }
            )
            st.dataframe(
                df0,
                column_config={
                    "name": "App name",
                    "stars": st.column_config.NumberColumn(
                        "Github Stars",
                        help="Number of stars on GitHub",
                        format="%d ⭐",
                    ),
                    "url": st.column_config.LinkColumn("App URL"),
                    "views_history": st.column_config.LineChartColumn(
                        "Views (past 30 days)", y_min=0, y_max=5000
                    ),
                },
                hide_index=True,
            )

        with tab2:
            st.code('''
            import streamlit as st
            import pandas as pd
            import numpy as np

            df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

            st.dataframe(df)  # Same as st.write(df)
            
            ---
            
            import random
            import pandas as pd
            import streamlit as st

            df = pd.DataFrame(
                {
                    "name": ["Roadmap", "Extras", "Issues"],
                    "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                    "stars": [random.randint(0, 1000) for _ in range(3)],
                    "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
                }
            )
            st.dataframe(
                df,
                column_config={
                    "name": "App name",
                    "stars": st.column_config.NumberColumn(
                        "Github Stars",
                        help="Number of stars on GitHub",
                        format="%d ⭐",
                    ),
                    "url": st.column_config.LinkColumn("App URL"),
                    "views_history": st.column_config.LineChartColumn(
                        "Views (past 30 days)", y_min=0, y_max=5000
                    ),
                },
                hide_index=True,
            )

            ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
    ### st.edit
    Display a data editor widget.
    The data editor widget allows you to edit dataframes and many other data structures in a table-like UI.
    ''')
    if st.toggle('Show example'):
        tab3, tab4 = st.tabs(['Output', 'Code'])
        with tab3:
            df1 = pd.DataFrame(
                [
                    {"command": "st.selectbox", "rating": 4, "is_widget": True},
                    {"command": "st.balloons", "rating": 5, "is_widget": False},
                    {"command": "st.time_input", "rating": 3, "is_widget": True},
                ]
            )
            edited_df = st.data_editor(df1, num_rows="dynamic")

            favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
            st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

        with tab4:
            st.code('''
            import streamlit as st
            import pandas as pd

            df = pd.DataFrame(
                [
                   {"command": "st.selectbox", "rating": 4, "is_widget": True},
                   {"command": "st.balloons", "rating": 5, "is_widget": False},
                   {"command": "st.time_input", "rating": 3, "is_widget": True},
               ]
            )
            edited_df = st.data_editor(df, num_rows="dynamic")

            favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
            st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
            ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
        ### st.metric
        Display a metric in big bold font, with an optional indicator of how the metric changed.''')
    if st.toggle('Show function example'):
        tab5, tab6 = st.tabs(['Output', 'Code'])
        with tab5:
            col1, col2, col3 = st.columns(3)
            col1.metric("Temperature", "70 °F", "1.2 °F")
            col2.metric("Wind", "9 mph", "-8%")
            col3.metric("Humidity", "86%", "4%")

        with tab6:
            st.code('''
            import streamlit as st

            col1, col2, col3 = st.columns(3)
            col1.metric("Temperature", "70 °F", "1.2 °F")
            col2.metric("Wind", "9 mph", "-8%")
            col3.metric("Humidity", "86%", "4%")
            ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
    ### st.json
    Display object or string as a pretty-printed JSON string.''')
    if st.toggle('Show a simple example'):
        tab7, tab8 = st.tabs(['Output', 'Code'])
        with tab7:
            st.json({
                'foo': 'bar',
                'baz': 'boz',
                'stuff': [
                    'stuff 1',
                    'stuff 2',
                    'stuff 3',
                    'stuff 5',
                ],
            })
        with tab8:
            st.code('''
            import streamlit as st

            st.json({
                'foo': 'bar',
                'baz': 'boz',
                'stuff': [
                    'stuff 1',
                    'stuff 2',
                    'stuff 3',
                    'stuff 5',
                ],
            })
            ''')

    return None

def Chart_elements():
    st.markdown('''
    # Chart elements
    
    Streamlit supports several popular data charting libraries like Matplotlib, Altair, deck.gl, and more. 
    In this section, you can find some examples of bar charts, line charts, maps ect.
    ''')

    st.markdown('''
    ### Basic charts
    ''')

    st.markdown('\n')

    st.markdown('''
        #### Area chart
        ''')
    tab_area1, tab_area2 = st.tabs(['Output', 'Code'])
    with tab_area1:
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        st.area_chart(chart_data)
    with tab_area2:
        st.code('''
        import streamlit as st
        import pandas as pd
        import numpy as np

        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        st.area_chart(chart_data)
                ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
            #### Bar chart
            ''')
    tab_bar1, tab_bar2 = st.tabs(['Output', 'Code'])
    with tab_bar1:
        chart_data = pd.DataFrame(
            {
                "col1": list(range(20)) * 3,
                "col2": np.random.randn(60),
                "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
            }
        )

        st.bar_chart(chart_data, x="col1", y="col2", color="col3")
    with tab_bar2:
        st.code('''
        import streamlit as st
        import pandas as pd
        import numpy as np

        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        st.bar_chart(chart_data)
                ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
                #### Line chart
                ''')
    tab_line1, tab_line2 = st.tabs(['Output', 'Code'])
    with tab_line1:
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        st.line_chart(chart_data)
    with tab_line2:
        st.code('''
        import streamlit as st
        import pandas as pd
        import numpy as np

        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        st.line_chart(chart_data)
                ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''#### Scatter plot''')
    tab_scatter1, tab_scatter2 = st.tabs(['Output', 'Code'])
    with tab_scatter1:
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
        chart_data['col4'] = np.random.choice(['A', 'B', 'C'], 20)
        st.scatter_chart(
            chart_data,
            x='col1',
            y='col2',
            color='col4',
            size='col3',
        )
    with tab_scatter2:
        st.code('''
        import streamlit as st
        import pandas as pd
        import numpy as np

        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
        chart_data['col4'] = np.random.choice(['A','B','C'], 20)

        st.scatter_chart(
            chart_data,
            x='col1',
            y='col2',
            color='col4',
            size='col3',
        )
                ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''#### Map''')
    tab_map1, tab_map2 = st.tabs(['Output', 'Code'])
    with tab_map1:
        df = pd.DataFrame({
            "col1": np.random.randn(1000) / 50 + 37.76,
            "col2": np.random.randn(1000) / 50 + -122.4,
            "col3": np.random.randn(1000) * 100,
            "col4": np.random.rand(1000, 4).tolist(),
        })

        st.map(df,
               latitude='col1',
               longitude='col2',
               size='col3',
               color='col4')
    with tab_map2:
        st.code('''
        import streamlit as st
        import pandas as pd
        import numpy as np

        df = pd.DataFrame({
            "col1": np.random.randn(1000) / 50 + 37.76,
            "col2": np.random.randn(1000) / 50 + -122.4,
            "col3": np.random.randn(1000) * 100,
            "col4": np.random.rand(1000, 4).tolist(),
        })

        st.map(df,
            latitude='col1',
            longitude='col2',
            size='col3',
            color='col4')
                ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
    #### Chart using PyDeck library
    
    ***st.pydeck_chart*** draws a chart using the PyDeck library.
    
    This supports 3D maps, point clouds, and more! More info about PyDeck at https://deckgl.readthedocs.io/en/latest/.''')
    tab_pydeck1, tab_pydeck2 = st.tabs(['Output', 'Code'])
    with tab_pydeck1:
        chart_data = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon'])

        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=37.76,
                longitude=-122.4,
                zoom=11,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=chart_data,
                    get_position='[lon, lat]',
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=chart_data,
                    get_position='[lon, lat]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=200,
                ),
            ],
        ))
    with tab_pydeck2:
        st.code('''
        import streamlit as st
        import pandas as pd
        import numpy as np
        import pydeck as pdk

        chart_data = pd.DataFrame(
           np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
           columns=['lat', 'lon'])

        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=37.76,
                longitude=-122.4,
                zoom=11,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                   'HexagonLayer',
                   data=chart_data,
                   get_position='[lon, lat]',
                   radius=200,
                   elevation_scale=4,
                   elevation_range=[0, 1000],
                   pickable=True,
                   extruded=True,
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=chart_data,
                    get_position='[lon, lat]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=200,
                ),
            ],
        ))
                    ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''#### Chart using GraphViz library''')
    tab_graph1, tab_graph2 = st.tabs(['Output', 'Code'])
    with tab_graph1:
        graph = graphviz.Digraph()
        graph.edge('run', 'intr')
        graph.edge('intr', 'runbl')
        graph.edge('runbl', 'run')
        graph.edge('run', 'kernel')
        graph.edge('kernel', 'zombie')
        graph.edge('kernel', 'sleep')
        graph.edge('kernel', 'runmem')
        graph.edge('sleep', 'swap')
        graph.edge('swap', 'runswap')
        graph.edge('runswap', 'new')
        graph.edge('runswap', 'runmem')
        graph.edge('new', 'runmem')
        graph.edge('sleep', 'runmem')

        st.graphviz_chart(graph)

    with tab_graph2:
        st.code('''
        import streamlit as st
        import graphviz

        # Create a graphlib graph object
        graph = graphviz.Digraph()
        graph.edge('run', 'intr')
        graph.edge('intr', 'runbl')
        graph.edge('runbl', 'run')
        graph.edge('run', 'kernel')
        graph.edge('kernel', 'zombie')
        graph.edge('kernel', 'sleep')
        graph.edge('kernel', 'runmem')
        graph.edge('sleep', 'swap')
        graph.edge('swap', 'runswap')
        graph.edge('runswap', 'new')
        graph.edge('runswap', 'runmem')
        graph.edge('new', 'runmem')
        graph.edge('sleep', 'runmem')

        st.graphviz_chart(graph)
                ''')

def Input_widgets():
    st.markdown('''
    # Input widgets
    
    With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, 
    sliders, text inputs, and more.
    ''')

    st.markdown('\n\n\n')

    st.markdown('''
    #### **Buttons**
    Widget can be in the form of simple button, download button and link button.
    You can also modify buttons with ***st.session_state.***.
    ''')
    if st.toggle('Show buttons examples'):
        tab_but1, tab_but2 = st.tabs(['Widget', 'Code'])
        with tab_but1:
            st.button("Reset", type="primary")
            if st.button('Say hello'):
                st.write('Why hello there')
            else:
                st.write('Goodbye')

            st.divider()

            st.link_button("Go to gallery", "https://streamlit.io/gallery")

            st.divider()

            st.markdown('Download a string as a file:')
            text_contents = '''This is some text'''
            st.download_button('Download some text', text_contents)

        with tab_but2:
            st.code('''
            import streamlit as st

            st.button("Reset", type="primary")
            if st.button('Say hello'):
                st.write('Why hello there')
            else:
                st.write('Goodbye')
            
            st.link_button("Go to gallery", "https://streamlit.io/gallery")
            
            # Download a string as a file:
            text_contents = 'This is some text'
            st.download_button('Download some text', text_contents)
            ''')

    st.markdown('---')
    st.markdown('\n\n\n')

    st.markdown('''
        #### **st.checkbox**
        Display a checkbox widget.
        ''')
    if st.toggle('Show checkbox example'):
        tab_check1, tab_check2 = st.tabs(['Widget', 'Code'])
        with tab_check1:
            agree = st.checkbox('I agree')

            if agree:
                st.write('Great!')

        with tab_check2:
            st.code('''
            import streamlit as st

            agree = st.checkbox('I agree')

            if agree:
                st.write('Great!')
                        ''')

    st.markdown('---')
    st.markdown('\n\n\n')

    st.markdown('''
        #### **st.toggle**
        Display a toggle widget.
        ''')
    if st.toggle('Show toggle example'):
        tab_t1, tab_t2 = st.tabs(['Widget', 'Code'])
        with tab_t1:
            on = st.toggle('Activate feature')

            if on:
                st.write('Feature activated!')

        with tab_t2:
            st.code('''
            import streamlit as st
            
            on = st.toggle('Activate')

            if on:
                st.write('Activated!')
            ''')

    st.markdown('---')
    st.markdown('\n\n\n')

    st.markdown('''
        #### **st.radio**
        Display a radio button widget.
        Here is also an example how to hide widgets lables and make widgets disabled.
        ''')
    if st.toggle('Show radio example'):
        tab_rad1, tab_rad2 = st.tabs(['Widget', 'Code'])
        with tab_rad1:
            if "visibility" not in st.session_state:
                st.session_state.visibility = "visible"
                st.session_state.disabled = False
                st.session_state.horizontal = False

            col1, col2 = st.columns(2)

            with col1:
                st.checkbox("Disable radio widget", key="disabled")
                st.checkbox("Orient radio options horizontally", key="horizontal")

            with col2:
                st.radio(
                    "Set label visibility 👇",
                    ["visible", "hidden", "collapsed"],
                    key="visibility",
                    label_visibility=st.session_state.visibility,
                    disabled=st.session_state.disabled,
                    horizontal=st.session_state.horizontal,
                )

        with tab_rad2:
            st.code('''
            import streamlit as st
            
            if "visibility" not in st.session_state:
                st.session_state.visibility = "visible"
                st.session_state.disabled = False
                st.session_state.horizontal = False

            col1, col2 = st.columns(2)

            with col1:
                st.checkbox("Disable radio widget", key="disabled")
                st.checkbox("Orient radio options horizontally", key="horizontal")

            with col2:
                st.radio(
                    "Set label visibility 👇",
                    ["visible", "hidden", "collapsed"],
                    key="visibility",
                    label_visibility=st.session_state.visibility,
                    disabled=st.session_state.disabled,
                    horizontal=st.session_state.horizontal,
                )

            ''')

    st.markdown('---')
    st.markdown('\n\n\n')

    st.markdown('''
        #### **st.selectbox**
        Display a select widget
        ''')
    if st.toggle('Show selectbox example'):
        tab_select1, tab_select2 = st.tabs(['Widget', 'Code'])
        with tab_select1:
            option = st.selectbox(
                'How would you like to be contacted?',
                ('Email', 'Home phone', 'Mobile phone'))

            st.write('You selected:', option)
        with tab_select2:
            st.code('''
            import streamlit as st
            
            option = st.selectbox(
                'How would you like to be contacted?',
                ('Email', 'Home phone', 'Mobile phone'))

            st.write('You selected:', option)
             ''')

    st.markdown('---')
    st.markdown('\n\n\n')

    st.markdown('''
            #### **st.multiselect**
            Display a multiselect widget.
            ''')
    if st.toggle('Show multiselect example'):
        tab_mselect1, tab_mselect2 = st.tabs(['Widget', 'Code'])
        with tab_mselect1:
            options = st.multiselect(
                'What are your favorite colors',
                ['Green', 'Yellow', 'Red', 'Blue'],
                ['Yellow', 'Red'])

            st.write('You selected:', options)

        with tab_mselect2:
            st.code('''
            import streamlit as st
            
            options = st.multiselect(
                'What are your favorite colors',
                ['Green', 'Yellow', 'Red', 'Blue'],
                ['Yellow', 'Red'])

            st.write('You selected:', options)
            ''')

    st.markdown('---')
    st.markdown('\n\n\n')

    st.markdown('''
                #### **st.slider**
                Display a slider widget.
                
                This supports int, float, date, time, and datetime types.
                This also allows you to render a range slider by passing a two-element tuple or list as the value.
                ''')
    if st.toggle('Show slider xample'):
        tab_sl1, tab_sl2 = st.tabs(['Widget', 'Code'])
        with tab_sl1:

            age = st.slider('How old are you?', 0, 130, 25)
            st.write("I'm ", age, 'years old')

            values = st.slider(
                'Select a range of values',
                0.0, 100.0, (25.0, 75.0))
            st.write('Values:', values)

            appointment = st.slider(
                "Schedule your appointment:",
                value=(time(11, 30), time(12, 45)))
            st.write("You're scheduled for:", appointment)

            start_time = st.slider(
                "When do you start?",
                value=datetime(2020, 1, 1, 9, 30),
                format="MM/DD/YY - hh:mm")
            st.write("Start time:", start_time)

        with tab_sl2:
            st.code('''
             import streamlit as st
             from datetime import time
             from datetime import datetime
                
            age = st.slider('How old are you?', 0, 130, 25)
            st.write("I'm ", age, 'years old')

            values = st.slider(
                'Select a range of values',
                0.0, 100.0, (25.0, 75.0))
            st.write('Values:', values)

            appointment = st.slider(
                "Schedule your appointment:",
                value=(time(11, 30), time(12, 45)))
            st.write("You're scheduled for:", appointment)

            start_time = st.slider(
                "When do you start?",
                value=datetime(2020, 1, 1, 9, 30),
                format="MM/DD/YY - hh:mm")
            st.write("Start time:", start_time)
                ''')

    st.markdown('---')
    st.markdown('\n\n\n')

    st.markdown('''
                #### **st.date_input**
                Display a date input widget.
                ''')
    if st.toggle('Show date_input example'):
        tab_date1, tab_date2 = st.tabs(['Widget', 'Code'])
        with tab_date1:
            d = st.date_input("When's your birthday", value=None)
            st.write('Your birthday is:', d)

        with tab_date2:
            st.code('''
                import streamlit as st
                
                d = st.date_input("When's your birthday", value=None)
                st.write('Your birthday is:', d)
                ''')

    st.markdown('---')
    st.markdown('\n\n\n')

    st.markdown('''
                    #### **st.time_input**
                    Display a time input widget.
                    ''')
    if st.toggle('Show time_input example'):
        tab_time1, tab_time2 = st.tabs(['Widget', 'Code'])
        with tab_time1:
            t = st.time_input('Set an alarm for', value=None)
            st.write('Alarm is set for', t)
        with tab_time2:
            st.code('''
            import datetime
            import streamlit as st

            t = st.time_input('Set an alarm for', value=None)
            st.write('Alarm is set for', t)
            ''')

    st.markdown('---')
    st.markdown('\n\n\n')

    st.markdown('''
        #### **st.file_uploader**
        Display a file uploader widget.
        
        By default, uploaded files are limited to 200MB. You can configure this using the server.maxUploadSize config 
        option. 
        For more info on how to set config options, see 
        https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options
        
        Example below allows to upload multiple files at a time.
        ''')
    if st.toggle('Show file uploader example'):
        tab_file1, tab_file2 = st.tabs(['Widget', 'Code'])
        with tab_file1:
            uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)

        with tab_file2:
            st.code('''
            import streamlit as st

            uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
            ''')

    st.markdown('---')
    st.markdown('\n\n\n')

    st.markdown('''
                #### **st.color_picker**
                Display a color picker widget.
                ''')
    if st.toggle('Show color picker example'):
        tab_c1, tab_c2 = st.tabs(['Widget', 'Code'])
        with tab_c1:
            color = st.color_picker('Pick A Color', '#00f900')
            st.write('The current color is', color)

        with tab_c2:
            st.code('''
            import streamlit as st

            color = st.color_picker('Pick A Color', '#00f900')
            st.write('The current color is', color)
            ''')

    return None

def Media_elements():
    st.markdown('''
    # Media elements
    ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
    #### Images
    ***st.image*** displays an image of list of images
    ''')
    tab1, tab2 = st.tabs(['Image', 'Code'])
    with tab1:
        st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.australiangeographic.com.au%2Ffact-file%2Ffact-file-galah-cacatua-roseicapilla%2F&psig=AOvVaw28iiO0zgyXLzWFK6kV5Jn7&ust=1701195893429000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCICvgNnm5IIDFQAAAAAdAAAAABAE", caption='Yes. Pink parrots aka galahs.')
    with tab2:
        st.code('''
        import streamlit as st
        from PIL import Image

        image = Image.open('/parrots.jpg')

        st.image(image, caption='Yes. Pink parrots galahs.')
        ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
    #### Audio
    ***st.audio***  displays an audio player.
    
    In the example below you can listen to extra heart-warming composition "Guren No Yamiya" from "Attack On Titan" ☺️
    ''')
    tab3, tab4 = st.tabs(['Audio', 'Code'])
    with tab3:
        st.audio("https://github.com/RenLinV/Streamlit_presentation/blob/main/pythonProject5/Aot_guren_no_yamiya.mp3", 'rb',format='audio/ogg')
    with tab4:
        st.code('''
        st.audio("https://github.com/RenLinV/Streamlit_presentation/blob/main/pythonProject5/Aot_guren_no_yamiya.mp3", 'rb',format='audio/ogg')
        ''')

    st.markdown('\n')
    st.markdown('\n')

    st.markdown('''
        #### Video
        ***st.video***  displays an video player.

        In the example below why not to continue with AOT 🙃.
        ''')
    tab5, tab6 = st.tabs(['Audio', 'Code'])
    with tab5:
        st.video("https://youtu.be/rwCJvSKzQkc?si=QO0ldGJwOOLFozY_")
    with tab6:
        st.code('''
        st.video("https://youtu.be/rwCJvSKzQkc?si=QO0ldGJwOOLFozY_")
        ''')


def Layouts_and_containers():
    st.markdown('''
    # Layouts and containers
    
    Streamlit provides several options for controlling how different elements are laid out on the screen.
    ''')

    col1, col2 = st.columns(2)

    with col1:
        with st.container():
            st.markdown('\n\n\n')
            st.markdown('\n\n\n')
            st.markdown('\n\n\n')

        with st.container():
            st.image('https://docs.streamlit.io/images/api/sidebar.jpg')
            st.markdown('#### **Sidebar**')
            st.caption('Display items in a sidebar.')
            st.code('''
                    st.sidebar.write('This lives in the sidebar')
                    st.sidebar.button('Click me!')
                    ''')

        with st.container():
            st.markdown('\n\n\n')
            st.markdown('\n\n\n')
            st.markdown('\n\n\n')
            st.markdown('\n\n\n')
            st.markdown('\n\n\n')
            st.markdown('\n\n\n')

        with st.container():
            st.image('https://docs.streamlit.io/images/api/tabs.jpg')
            st.markdown('#### **Tabs**')
            st.caption('Insert containers separated into tabs.')
            st.code('''
            tab1, tab2 = st.tabs(['Tab1', 'Tab 2'])
            tab1.write('this is tab 1')
            tab2.write('this is tab 2')
            ''')

        with st.container():
            st.markdown('\n\n\n')
            st.markdown('\n\n\n')

        with st.container():
            st.image('https://docs.streamlit.io/images/api/container.jpg')
            st.markdown('#### **Container**')
            st.caption('Insert a multi-element container.')
            st.code('''
            c = st.container()
            st.write('This will show last')
            c.write('This will show first')
            c.write('This will show second')
            ''')

    with col2:
        with st.container():
            st.image('https://docs.streamlit.io/images/api/columns.jpg')
            st.markdown('#### **Columns**')
            st.caption('Insert containers laid out as side-by-side columns.')
            st.code('''
                        col1, col2 = st.columns(2)
                        col1.write('this is column 1')
                        col2.write('this is column 2')
                        ''')

        with st.container():
            st.markdown('\n\n\n')

        with st.container():
            st.image('https://docs.streamlit.io/images/api/expander.jpg')
            st.markdown('#### **Expander**')
            st.caption('Insert a multi-element container that can be expanded/collapsed.')
            st.code('''
            with st.expander('Open to see more'):
               st.write('This is more content')
            ''')

        with st.container():
            st.markdown('\n\n\n')
            st.markdown('\n\n\n')

        with st.container():
            st.image('https://docs.streamlit.io/images/api/empty.jpg')
            st.markdown('#### **Empty**')
            st.caption('Insert a single-element container.')
            st.code('''
                        c = st.container()
                        st.write('This will show last')
                        c.write('This will be replaced')
                        c.write('This will show first')
                        ''')



info = st.sidebar.radio(
    "API reference",
    ["Display almost anything", "Text elements", "Data elements", "Chart elements", 'Input widgets', 'Media elements',
     'Layouts and containers']
)

if info == "Display almost anything":
    Display_almost_anything()
elif info == "Text elements":
    Text_elements()
elif info == "Data elements":
    Data_elements()
elif info == "Chart elements":
    Chart_elements()
elif info == 'Input widgets':
    Input_widgets()
elif info == 'Media elements':
    Media_elements()
elif info == 'Layouts and containers':
    Layouts_and_containers()
