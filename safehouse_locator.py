import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
from streamlit_folium import folium_static

# Load the CSV file
csv_file = "japan_shelters.csv"  # Replace with your actual file name
shelters_df = pd.read_csv(csv_file)


# Function to get latitude and longitude from an address or zip code
def get_location(address):
    geolocator = Nominatim(user_agent="safehouse_locator")
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    return None


# Function to find the nearest shelter
def find_nearest_shelter(user_location, shelters_df):
    nearest_shelter = None
    shortest_distance = float('inf')

    for index, row in shelters_df.iterrows():
        shelter_location = (row['latitude'], row['longitude'])
        distance = geodesic(user_location, shelter_location).kilometers
        if distance < shortest_distance:
            shortest_distance = distance
            nearest_shelter = row

    return nearest_shelter, shortest_distance


# Streamlit app
def main():
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h1>Japan Earthquake Shelter Finder</h1>
            <p>For more useful links, click <a href="https://xavidigi.com/" target="_blank">here</a>.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("Enter your town name or zip code to find the nearest earthquake shelter.")

    # User input for town name or zip code
    user_input = st.text_input("Town name or Zip code")

    if user_input:
        # Get user location
        user_location = get_location(user_input)

        if user_location:
            # Find the nearest shelter
            nearest_shelter, distance = find_nearest_shelter(user_location, shelters_df)

            if nearest_shelter is not None:
                st.write(f"The nearest shelter is **{nearest_shelter['name']}** at **{nearest_shelter['address']}**, "
                         f"which is approximately **{distance:.2f} kilometers** away.")

                # Create a map centered on the user's location
                m = folium.Map(location=user_location, zoom_start=10)

                # Add a marker for the user's location
                folium.Marker(user_location, popup="Your Location", tooltip="You",
                              icon=folium.Icon(color="blue")).add_to(m)

                # Add a marker for the nearest shelter
                shelter_location = (nearest_shelter['latitude'], nearest_shelter['longitude'])
                folium.Marker(
                    shelter_location,
                    popup=f"{nearest_shelter['name']} - {nearest_shelter['address']}",
                    tooltip=nearest_shelter["name"],
                    icon=folium.Icon(color="green")
                ).add_to(m)

                # Display the map in Streamlit
                folium_static(m)
            else:
                st.write("No shelter found near your location.")
        else:
            st.write("Location not found. Please enter a valid town name or zip code.")


if __name__ == "__main__":
    main()
