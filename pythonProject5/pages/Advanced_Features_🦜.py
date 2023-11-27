import streamlit as st

st.set_page_config(layout=‘wide’)

st.sidebar.header("**Advanced Features 🦜**")

st.markdown("# **Advanced Features 🦜**")

st.markdown('''
&nbsp; **$\color{#008B8B}{Streamlit}$** &nbsp; has a lot to offer on a basic level, and if you want to have 
a better understanding of how different parts of &nbsp; **$\color{#008B8B}{Streamlit}$** &nbsp; work, you can explore 
 ***[Advanced features](https://docs.streamlit.io/library/advanced-features)***.
 
 ### Topics of Advanced features
''')
with st.container():
    st.markdown('''
    ### ⋮App menu
    Streamlit provides a configurable menu within your app to access convenient tools. 
    By default, you can access developer options from the app menu while logged into an account with administrative 
    access. 
    ''')

st.markdown('\n\n')

with st.container():
    st.markdown('''
    ### Command-line interface
    A command-line (CLI) tool gets installed automatically with Streamlit. 
    The purpose of this tool is to run Streamlit apps, change Streamlit configuration options, and help you diagnose 
    and fix issues.
    ''')

st.markdown('\n\n')

with st.container():
    st.markdown('''
    ### Configuration
    Streamlit provides four different ways to set configuration options. 
    This list is in reverse order of precedence, i.e. command line flags take precedence over environment variables 
    when the same configuration option is provided multiple times.
    ''')

st.markdown('\n\n')

with st.container():
    st.markdown('''
    ### Theming
    Section provides info about how page elements are affected by the various theme config options including:
    - [primaryColor](https://docs.streamlit.io/library/advanced-features/theming#primarycolor)
    - [backgroundcolor](https://docs.streamlit.io/library/advanced-features/theming#backgroundcolor)
    - [secondarybackgroundcolor](https://docs.streamlit.io/library/advanced-features/theming#secondarybackgroundcolor)
    - [textcolor](https://docs.streamlit.io/library/advanced-features/theming#textcolor)
    - [font](https://docs.streamlit.io/library/advanced-features/theming#font)
    - [base](https://docs.streamlit.io/library/advanced-features/theming#base)
    ''')

st.markdown('\n\n')

with st.container():
    st.markdown('''
    ### Caching
    Streamlit runs your script from top to bottom at every user interaction or code change. This execution model makes 
    development super easy. But it comes with two major challenges:
    - Long-running functions run again and again, which slows down your app.
    - Objects get recreated again and again, which makes it hard to persist them across reruns or sessions.
    
    But don't worry! Streamlit lets you tackle both issues with its built-in caching mechanism. Caching stores the 
    results of slow function calls, so they only need to run once. This makes your app much faster and helps with 
    persisting objects across reruns.
    ''')

st.markdown('\n\n')

with st.container():
    st.markdown('''
    ### Add statefulness to apps
    Session State is a way to share variables between reruns, for each user session. In addition to the ability to store 
    and persist state, Streamlit exposes the ability to manipulate state using Callbacks.
    ''')

st.markdown('\n\n')

with st.container():
    st.markdown('''
    ### Pre-release features
    Streamlit developers prioritise quick development and stability at the same time. There fore they provide to the an 
    opportunity to try Streamlit's bleeding-edge features.
    ''')

st.markdown('\n\n')

with st.container():
    st.markdown('''
    ### Secrets management
    Streamlit provides native file-based secrets management to easily store and securely access your secrets in your 
    Streamlit app.
    ''')

st.markdown('\n\n')

with st.container():
    st.markdown('''
    ### Working with timezones
    In general, working with timezones can be tricky. Your Streamlit app users are not necessarily in the same timezone 
    as the server running your app. It is especially true of public apps, where anyone in the world (in any timezone) 
    can access your app. As such, it is crucial to understand how Streamlit handles timezones, so you can avoid 
    unexpected behavior when displaying datetime information.
    ''')

st.markdown('\n\n')

with st.container():
    st.markdown('''
    ### Advanced notes on widget behavior
    Widgets are magical and often work how you want. BUt, on top of that, they can have behavior in some situations.
    This section provides a high-level, abstract description of widget behavior, including some common edge-cases.
    ''')
