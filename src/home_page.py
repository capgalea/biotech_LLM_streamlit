import streamlit as st
import pandas as pd
import plotly.express as px
import initialize_llm

st.set_page_config("Australian BioTech", layout='wide', initial_sidebar_state='auto')

# Function to load the data
@ st.cache_data
def load_csv(file1):
    df = pd.read_csv(file1)
    return df

# Load the data
data = load_csv("data/bioTech_data.csv")

# def load_patents(file2):
#     df2 = pd.read_csv(file2)
#     return df2

# # Load the data
# patents = load_patents("data/patents.csv")

# Function to convert URLs to Markdown hyperlinks
def make_clickable(url_companies):
    return f'<a href="{url_companies}" target="_blank">{url_companies}</a>'

# Home Page
def home_page():

    #Create two columns
    col1, col2 = st.columns([0.5, 10])

    with col1:
        # Add an image to the left column
        st.image("images/AusBioTech_logo.png", width=10)   

    with col2:
        # Add a header to the right column
        st.markdown("<h1 style='text-align: center;'>Australian Biotechnology Companies</h1>", unsafe_allow_html=True)

    # Add vertical space between header and plots
    st.write("")
    st.write("")

    # Display the data
    # Create two columns
    col1, col2 = st.columns([2, 2])

    with col1:
        # Create bar plotly bar chart showing the number of companies by city
        st.write("Number of Companies by State")
        city_counts = data["City"].value_counts()
        st.bar_chart(city_counts)

    

    # Create a sidebar to choose the company or city
    choice = st.sidebar.radio("Menu", ["Company", "City", "Category"])

    # Create a sidebar to choose the company or city
    if choice == "City":
        # Create table showing the selected city
        city_list = data["City"].unique().tolist()
        selected_city = st.sidebar.selectbox("Select a City", city_list, index=None) 
        
        # Create checkbox to show all data
        if st.sidebar.checkbox("Show All Data"):
            # Display the data in an expander
            with st.expander("View Data"):
                st.dataframe(data[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                column_config={"url": st.column_config.LinkColumn("Company Website")}
                                )
                df = data
        else:
            # Display the data in an expander
            with st.expander("View Data"):
                city_df = data[data["City"] == selected_city]
                st.dataframe(city_df[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                column_config={"url": st.column_config.LinkColumn("Company Website")}
                                )
                df = city_df
        
    # Create a sidebar to choose the company or city
    elif choice == "Company":   
        company_list = data["Companies"].unique().tolist()
        selected_company = st.sidebar.selectbox("Select a Company", company_list, index=None) 

        # Create checkbox to show all data
        if st.sidebar.checkbox("Show All Data"):
            # Display the data in an expander
            with st.expander("View Data"):
                st.dataframe(data[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                column_config={"url": st.column_config.LinkColumn("Company Website")}
                                )
                df = data
        else:
            # Display the data in an expander
            with st.expander("View Data"):
                company_df = data[data["Companies"] == selected_company]
                st.dataframe(company_df[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                column_config={"url": st.column_config.LinkColumn("Company Website")}
                                )
                df = company_df
    # Create a sidebar to choose the company or city
    elif choice == "Category":   
        category_list = data["Category"].unique().tolist()
        selected_category = st.sidebar.selectbox("Select a Category", category_list, index=None) 

        # Create checkbox to show all data
        if st.sidebar.checkbox("Show All Data"):
            # Display the data in an expander
            with st.expander("View Data"):
                st.dataframe(data[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                column_config={"url": st.column_config.LinkColumn("Company Website")}
                                )
                df = data
        else:
            # Display the data in an expander
            with st.expander("View Data"):
                category_df = data[data["Category"] == selected_category]
                st.dataframe(category_df[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                column_config={"url": st.column_config.LinkColumn("Company Website")}
                                )
                df = category_df
        
    with col2:
        # Create plotly map showing the location of each company using the latitude and lognitude columns
        # Ensure the data contains latitude and longitude columns
        if 'Latitude' not in data.columns or 'Longitude' not in data.columns:
            st.error("The data does not contain latitude and longitude information.")
        
        # Create a sidebar to choose the company or city
        elif choice == "Company":
                # Create a Plotly map
                fig = px.scatter_mapbox(
                df,
                lat="Latitude",
                lon="Longitude",
                hover_name="Companies",
                hover_data={"Latitude": False, "Longitude": False, "Location": True, 
                            "url": True, "Contact": True, "Category": True},
                zoom=2,
                height=300,
                center={"lat": -25.2744, "lon": 133.7751}  # Center on Australia
                )

                fig.update_layout(mapbox_style="open-street-map")
                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


                # Display the map in the Streamlit app
                st.plotly_chart(fig, key="map")
        
        # Create a sidebar to choose the company or city
        elif choice == "City":
                # Create a Plotly map
                fig = px.scatter_mapbox(
                df,
                lat="Latitude",
                lon="Longitude",
                hover_name="Companies",
                hover_data={"Latitude": False, "Longitude": False, "Location": True, 
                            "url": True, "Contact": True, "Category": True},
                zoom=2,
                height=300,
                center={"lat": -25.2744, "lon": 133.7751}  # Center on Australia
                )
    
                fig.update_layout(mapbox_style="open-street-map")
                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    
                # Display the map in the Streamlit app
                st.plotly_chart(fig, key="map")

        # Create a sidebar to choose the company or city
        elif choice == "Category":
                # Create a Plotly map
                fig = px.scatter_mapbox(
                df,
                lat="Latitude",
                lon="Longitude",
                hover_name="Companies",
                hover_data={"Latitude": False, "Longitude": False, "Location": True, 
                            "url": True, "Contact": True, "Category": True},
                zoom=2,
                height=300,
                center={"lat": -25.2744, "lon": 133.7751}  # Center on Australia
                )

                fig.update_layout(mapbox_style="open-street-map")
                fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


                # Display the map in the Streamlit app
                st.plotly_chart(fig, key="map")