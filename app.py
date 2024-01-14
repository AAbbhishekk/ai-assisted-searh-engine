import streamlit as st
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain import HuggingFaceHub
from langchain.tools import Tool, ShellTool
import os
from datetime import datetime
from langchain.tools import DuckDuckGoSearchRun


token = os.environ['HF_TOKEN']

hub_llm = HuggingFaceHub(
        repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
    huggingfacehub_api_token=token)

# Set the page title and icon
st.set_page_config(
    page_title="AI Driven Search",
    page_icon="🔍",
    layout="wide",  # Wide layout for additional space
)

# Custom CSS style for the title block
st.markdown(
    """
    <style>
        .title-block {
            background-color: #3498db;
            color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .subtitle {
            color: #2c3e50;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title block with custom styling
st.markdown('<div class="title-block">', unsafe_allow_html=True)
st.title("🌐 AI powered Search Engine")
st.markdown("### Find what you're looking for with the power of AI!")
st.markdown("</div>", unsafe_allow_html=True)

# Subtitle and description with custom styling
st.markdown('<div class="subtitle">', unsafe_allow_html=True)
st.subheader("How it works:")
st.write(
    "Our search engine is powered by DuckDuck Go search and uses language models "
    "that understand your queries and provide accurate results. "
)
st.markdown("</div>", unsafe_allow_html=True)

# Add any other content or functionality as needed

# Example search input
# search_query = st.text_input("Enter your search query:")
with st.form(key="form"):
    user_input = st.text_input("Ask your question")
    submit_clicked = st.form_submit_button("Enter your search")


# Example search button
# if st.button("Search", key="search_button"):
if submit_clicked:

    # Add your AI-powered search functionality here
    

# Define a new tool that returns the current datetime
    datetime_tool = Tool(
        name="Datetime",
        func=lambda x: datetime.now().isoformat(),
        description="Returns the current datetime",
    )
    search = DuckDuckGoSearchRun()
    search_tool = Tool(
        name="search",
        func=search,
        description="search over the internet using this tool"
    )



    agent_chain = initialize_agent(
        [search_tool],
        hub_llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors =True,
    )
    result = agent_chain.run(user_input)
    st.success(result)

# Add any other components or features as needed

# Footer with custom styling
st.markdown(
    '<p style="text-align:center; color:#7f8c8d;">Built with ❤️ by Abhishek | <a href="https://github.com/your_username/your_repo" style="color:#3498db;">GitHub Repo</a></p>',
    unsafe_allow_html=True,
)
