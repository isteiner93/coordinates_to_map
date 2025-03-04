# **Trans-carpathia 2024**

This Streamlit application allows users to input geographic coordinates in Degrees, Minutes, Seconds (DMS) format and generates links to view the location on Google Maps and mapy.cz. The application is designed to simplify the process of converting DMS coordinates into a decimal format and creating accessible map links.

## **Features**

- **DMS to Decimal Conversion**: The app converts DMS coordinates into decimal degrees, which are needed for map URL generation.
- **Google Maps Link Generation**: Users can get a direct link to view the entered coordinates on Google Maps.
- **mapy.cz Link Generation**: Users can also get a direct link to view the coordinates on mapy.cz, a popular mapping service in Central Europe.

## **How to Use**

1. **Input Coordinates**: Enter the DMS coordinates in the following format:
   
`44°17'56.5"N 16°16'54.9"E`

Ensure that the coordinates are accurately formatted with degrees (°), minutes ('), and seconds (") followed by the hemisphere indicator (N, S, E, W).

3. **Generate Links**: Once the coordinates are entered, the application automatically processes them and provides:
- A clickable link to view the location on Google Maps.
- A clickable link to view the location on mapy.cz.

3. **View Location**: Click on the provided links to open the map service and view the location.

## **Error Handling**

The application is designed to handle invalid input gracefully. If there is an error in processing the input, an error message will be displayed to help you correct the format or content of the DMS coordinates.

## **Installation**

To run the application locally, you need to have Python and Streamlit installed. Follow these steps:

1. Clone the repository or download the script.
2. Navigate to the directory containing the script.
3. Install the required dependencies (if any are specified in a `requirements.txt`).
4. Run the Streamlit app using the following command:
```bash
streamlit run app.py
