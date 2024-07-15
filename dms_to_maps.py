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

    # Format the latitude and longitude in DMS format for the URL
    lat_dms_str = f"{abs(lat_parts[0])}°{abs(lat_parts[1])}'{abs(lat_parts[2]):.1f}\"{'N' if latitude >= 0 else 'S'}"
    lon_dms_str = f"{abs(lon_parts[0])}°{abs(lon_parts[1])}'{abs(lon_parts[2]):.1f}\"{'E' if longitude >= 0 else 'W'}"

    return f"https://www.google.com/maps/place/{lat_dms_str}+{lon_dms_str}/@{latitude},{longitude},14z/data=!4m4!3m3!8m2!3d{latitude}!4d{longitude}?entry=ttu"


def generate_mapy_cz_link(dms_str):
    lat_dms, lon_dms = dms_str.split(' ')

    # Format the latitude and longitude in DMS format for the URL
    lat_dms_encoded = lat_dms.replace('°', '%C2%B0').replace("'", '%27').replace('"', '%22')
    lon_dms_encoded = lon_dms.replace('°', '%C2%B0').replace("'", '%27').replace('"', '%22')

    return f"https://en.mapy.cz/zakladni?q={lat_dms_encoded}%20{lon_dms_encoded}&source=coor"


st.title('Trans-carpathia 2024')

dms_str = st.text_input('Enter DMS coordinates (e.g., 44°17\'56.5"N 16°16\'54.9"E):', '')

if dms_str:
    try:
        st.subheader('Google Maps Link:')
        google_maps_link = generate_google_maps_link(dms_str)
        st.write(google_maps_link)
        st.markdown(f'[Open in Google Maps]({google_maps_link})')

        st.subheader('mapy.cz Link:')
        mapy_cz_link = generate_mapy_cz_link(dms_str)
        st.write(mapy_cz_link)
        st.markdown(f'[Open in mapy.cz]({mapy_cz_link})')
    except Exception as e:
        st.error(f"Error: {e}")
