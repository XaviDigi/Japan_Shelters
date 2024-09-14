Japan Earthquake Shelter Finder
This Streamlit app helps users locate the nearest earthquake shelters in Japan by entering a town name or zip code. It reads data from a CSV file containing shelter information, uses geolocation services via Nominatim, and displays an interactive map using Folium.

Features
Users can input a town name or zip code to find nearby earthquake shelters.
Uses geolocation to determine the user's location.
Calculates the distance from the user's location to the nearest shelter.
Displays an interactive map with markers for the user's location and the nearest shelter.
Provides detailed information about the shelter, including name and address.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/japan-earthquake-shelter-finder.git
cd japan-earthquake-shelter-finder
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Prepare the CSV file:

Add a file named japan_shelters.csv to the project directory.
Ensure the file contains columns for name, address, latitude, and longitude.
Run the Streamlit app:

bash
Copy code
streamlit run app.py
CSV Format
The japan_shelters.csv file should follow this structure:

name	address	latitude	longitude
Shelter A	123 Main St, Tokyo	35.6895	139.6917
Shelter B	456 Side St, Kyoto	35.0116	135.7681
...	...	...	...
Usage
Run the app and enter a town name or zip code in the input field.
The app will locate the nearest shelter and display relevant details.
An interactive map will show both your location and the nearest shelter, along with the calculated distance.
Dependencies
The app relies on the following Python libraries:

Streamlit: for the app's user interface.
Pandas: for handling shelter data.
Geopy: for geolocation and distance calculations.
Folium: for map visualization.
Streamlit-Folium: to display Folium maps within Streamlit.
Future Enhancements
Add the ability to filter shelters based on capacity.
Display multiple nearby shelters with distance information.
Improve the geolocation accuracy and handle edge cases for invalid user inputs.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Useful Links
For more resources, visit xavidigi.com.
