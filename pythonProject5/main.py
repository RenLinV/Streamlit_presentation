import streamlit as st

st.markdown("# Hi")
from st_pages import Page, Section, add_page_title, show_pages
show_pages(
        [
            Page("main.py", "Main", "🏠"),
            # Can use :<icon-name>: or the actual icon
            Section(name="Docs")
            Page("pages/cheat_sheet.py", "Cheat sheet", ":books:"),
            # Since this is a Section, all the pages underneath it will be indented
            # The section itself will look like a normal page, but it won't be clickable
            #Section(name="Cool features"),
            # The pages appear in the order you pass them
            #Page("Streamlit presentation/pages/Community.py", "Community"),
            #Page("Streamlit presentation/pages/Examples.py", "Examples"),
        ]
    )

#add_page_title()