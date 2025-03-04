Trans-carpathia 2024

This Streamlit application allows users to input geographic coordinates in Degrees, Minutes, Seconds (DMS) format and generates links to view the location on Google Maps and mapy.cz. The application is designed to simplify the process of converting DMS coordinates into a decimal format and creating accessible map links.


Features

DMS to Decimal Conversion: The app converts DMS coordinates into decimal degrees, which are needed for map URL generation.
Google Maps Link Generation: Users can get a direct link to view the entered coordinates on Google Maps.
mapy.cz Link Generation: Users can also get a direct link to view the coordinates on mapy.cz, a popular mapping service in Central Europe.

How to Use

Input Coordinates: Enter the DMS coordinates in the following format:

Copy Code
44°17'56.5"N 16°16'54.9"E
Ensure that the coordinates are accurately formatted with degrees (°), minutes ('), and seconds (") followed by the hemisphere indicator (N, S, E, W).

Generate Links: Once the coordinates are entered, the application automatically processes them and provides:

A clickable link to view the location on Google Maps.
A clickable link to view the location on mapy.cz.
View Location: Click on the provided links to open the map service and view the location.


Error Handling

The application is designed to handle invalid input gracefully. If there is an error in processing the input, an error message will be displayed to help you correct the format or content of the DMS coordinates.


Installation

To run the application locally, you need to have Python and Streamlit installed. Follow these steps:


Clone the repository or download the script.
Navigate to the directory containing the script.
Install the required dependencies (if any are specified in a requirements.txt).
Run the Streamlit app using the following command:
bash
Copy Code
streamlit run app.py

Replace app.py with the actual name of your script file.


Notes

Ensure that your input follows the exact format for DMS coordinates with correct symbols and hemisphere indicators.
The application assumes the input is well-formed and does not perform extensive validation beyond basic error handling.

Dependencies

Streamlit: Ensure Streamlit is installed to run the application. Use pip install streamlit if necessary.

Example

To test the application, you can use the following sample coordinate:


DMS Input: 44°17'56.5"N 16°16'54.9"E
Generated Links:
[Google Maps](https://www.google.com/maps/place/44%C2%B017'56.5%22N+16%C2%B016'54.9%22E\)
[mapy.cz](https://en.mapy.cz/zakladni?q=44%C2%B017%2756.5%22N%2016%C2%B016%2754.9%22E&source=coor\)
