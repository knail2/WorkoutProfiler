import streamlit as st
import pandas as pd

if 'confirmed_restricted' not in st.session_state:
    st.session_state.confirmed_restricted = False

def on_change():
    if edited_df.iloc[1]['category'] == "🔒 Restricted" and not st.session_state.confirmed_restricted:
        st.session_state.show_popup = True
    else:
        st.session_state.show_popup = False

df = pd.DataFrame({
    'category': [
        "📊 Data Exploration",
        "📈 Data Visualization",
        "🤖 LLM",
        "📊 Data Exploration",
    ],
})

edited_df = st.data_editor(
    df,
    column_config={
        "category": st.column_config.SelectboxColumn(
            "App Category",
            help="The category of the app",
            width="medium",
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
                "🔒 Restricted",
            ],
            required=True,
        )
    },
    hide_index=True,
    on_change=on_change
)

if st.session_state.get('show_popup', False):
    with st.popover("Confirmation"):
        st.write("Are you sure you want to sell your soul to the masking devil?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes"):
                st.session_state.confirmed_restricted = True
                st.session_state.show_popup = False
                st.rerun()
        with col2:
            if st.button("No"):
                edited_df.iloc[1, edited_df.columns.get_loc('category')] = "📊 Data Exploration"
                st.session_state.show_popup = False
                st.rerun()

if st.button("Click me"):
    selected_value = edited_df.iloc[1]['category']
    query = f"select {selected_value} from bondibeachtable"
    st.write(f"Generated query: {query}")