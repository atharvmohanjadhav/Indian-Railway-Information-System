import streamlit as st
from scripts.news.rail_news import fetch_railway_news

class RunNewsChain:
    def __init__(self) -> None:
        st.subheader("📰 Latest Indian Railway News")

        news_list = fetch_railway_news()

        if news_list:
            for article in news_list:
                if article.get('urlToImage'):
                    st.image(article['urlToImage'],width=300)
                
                st.markdown(f"### [{article['title']}]({article['url']})")
                st.write(f"**Source:** {article['source']['name']}  \n**Published:** {article['publishedAt'][:10]}")
                st.write(article['description'] or "No description available.")
                st.write("---")
        else:
            st.warning("Sorry, couldn't fetch the latest news at the moment. Please try again later!")


