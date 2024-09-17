# 🗾 Japan Earthquake Shelter Finder 🏠

This **Streamlit** app helps users locate the nearest earthquake shelters in Japan by entering a town name or zip code. The app reads data from a CSV file containing shelter information, utilizes geolocation services via **Nominatim**, and displays an interactive map using **Folium**. 🌏

![Streamlit](https://img.shields.io/badge/streamlit-app-red?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)

## 🚀 Live Demo

[![Live](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen)](https://celest23-top100songs-app-lvaseu.streamlit.app/)

## ✨ Features

- 🔍 **Search by town name or zip code** to find nearby earthquake shelters.
- 📍 Uses **geolocation** to determine the user's location.
- 📏 **Calculates** the distance to the nearest shelter.
- 🗺️ Displays an **interactive map** with markers for the user's location and the nearest shelter.
- 🏢 Provides detailed information about the shelter, including **name and address**.

---

## ⚙️ Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/japan-earthquake-shelter-finder.git
    cd japan-earthquake-shelter-finder
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare the CSV file**:

    - Add a file named `japan_shelters.csv` to the project directory.
    - Ensure the file contains columns for `name`, `address`, `latitude`, and `longitude`.

4. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

---

## 🗂️ CSV Format

The `japan_shelters.csv` file should have the following structure:

| Name         | Address              | Latitude  | Longitude  |
|--------------|----------------------|-----------|------------|
| Shelter A    | 123 Main St, Tokyo    | 35.6895   | 139.6917   |
| Shelter B    | 456 Side St, Kyoto    | 35.0116   | 135.7681   |
| ...          | ...                   | ...       | ...        |

---

## 🚀 Usage

1. Run the app and enter a **town name** or **zip code** in the input field.
2. The app will locate the **nearest shelter** and display relevant details.
3. An **interactive map** will show both your location and the nearest shelter, along with the calculated distance.

---

## 🛠️ Dependencies

This app uses the following Python libraries:

- **[Streamlit](https://streamlit.io/)**: for building the user interface.
- **[Pandas](https://pandas.pydata.org/)**: for data manipulation and analysis.
- **[Geopy](https://geopy.readthedocs.io/)**: for geolocation and distance calculations.
- **[Folium](https://python-visualization.github.io/folium/)**: for generating maps.
- **[Streamlit-Folium](https://pypi.org/project/streamlit-folium/)**: for displaying Folium maps within Streamlit.

---

## 🚧 Future Enhancements

- 🏗️ Add a filter for shelters based on **capacity**.
- 🗺️ Display **multiple nearby shelters** with distance info.
- 🎯 Improve **geolocation accuracy** and handle edge cases for invalid inputs.

---

## 🔗 Useful Links

For more resources, visit [xavidigi.com](https://xavidigi.com/). 🔗
