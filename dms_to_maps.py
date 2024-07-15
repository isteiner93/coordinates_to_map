import streamlit as st


def dms_to_decimal(degrees, minutes, seconds):
    return degrees + minutes / 60 + seconds / 3600


def parse_dms(dms_str):
    parts = dms_str.split('°')
    degrees = int(parts[0])
    minutes_parts = parts[1].split("'")
    minutes = int(minutes_parts[0])
    seconds_parts = minutes_parts[1].split('"')
    seconds = float(seconds_parts[0])
    return degrees, minutes, seconds


def generate_google_maps_link(dms_str):
    lat_dms, lon_dms = dms_str.split(' ')

    lat_parts = parse_dms(lat_dms[:-1])
    lon_parts = parse_dms(lon_dms[:-1])

    latitude = dms_to_decimal(*lat_parts)
    longitude = dms_to_decimal(*lon_parts)

    # Adjust for N/S and E/W
    if lat_dms[-1] == 'S':
        latitude = -latitude
    if lon_dms[-1] == 'W':
        longitude = -longitude

    return f"https://www.google.com/maps/place//@{latitude},{longitude},14z/data=!4m2!3m1!1s0x0:0x0?entry=s&sa=X"


st.title('DMS to Google Maps Link Converter')

dms_str = st.text_input('Enter DMS coordinates (e.g., 44°17\'56.5"N 16°16\'54.9"E):', '')

if dms_str:
    try:
        link = generate_google_maps_link(dms_str)
        st.write('Google Maps Link:')
        st.write(link)
        st.markdown(f'[Open in Google Maps]({link})')
    except Exception as e:
        st.error(f"Error: {e}")
