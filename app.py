import streamlit as st
import pandas as pd

# Set page layout
st.set_page_config(layout="wide")

# Load the CSV file (replace with your actual data loading logic)
# Ideally this wouldn't be here - will be moved during the backend phase
csv_file = "csv/points.csv"
data = pd.read_csv(csv_file)

# JavaScript event listener code to handle map clicks
MAP_CLICK_JS = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const mapElement = document.querySelector('#kepler_map iframe');
    mapElement.contentWindow.addEventListener('click', function(event) {
        const map = mapElement.contentWindow.__keplerGl__;
        const clickedFeatures = map.mapboxMap.queryRenderedFeatures(event.point);
        if (clickedFeatures.length > 0) {
            const clickedFeature = clickedFeatures[0];
            const featureId = clickedFeature.properties.id;
            const streamlit = window.parent.Streamlit;  // Corrected the reference to window.parent.Streamlit
            if (streamlit !== undefined) {
                streamlit.setComponentValue(featureId);
            }
        }
    });
});
</script>
"""

# Inject JavaScript into the Streamlit app
st.markdown(MAP_CLICK_JS, unsafe_allow_html=True)

# Create columns with equal widths
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Points")

    # Display the Kepler.gl map
    with open('D:/Project wasiq/Project wasiq/template/home.html', 'r') as f:
        html_map = f.read()
        st.components.v1.html(html_map, height=500,
                              scrolling=True)  # Display the map

with col2:
    st.title("Data Dashboard")

    # Display images in two columns with alternating left and right alignment
    last_item = None
    for index, row in data.iterrows():
        if index % 2 != 0:
            col_left, col_right = st.columns(2)
            with col_left:
                if last_item is not None:
                    st.image(last_item['image_url'], caption=last_item['name'],
                             use_column_width=True)
                    last_item = None
            with col_right:
                st.image(row['image_url'], caption=row['name'],
                         use_column_width=True)

        else:
            last_item = row

    if last_item is not None:
        col_left, col_right = st.columns(2)
        with col_left:
            st.image(last_item['image_url'], caption=last_item['name'],
                     use_column_width=True)
        last_item = None
    # if index % 2 != 0 or index == len(data) - 1:
    #     with col_right:
    #         # Check if it's the last row or odd-indexed row to ensure pairs are displayed correctly
    #         if index % 2 != 0 or index == len(data) - 1:
    #             st.image(row['image_url'],
    #                      caption=row['name'], use_column_width=True)
    #         else:
    #             # Blank space if no second image in this row
    #             st.image('', use_column_width=True)
#     print(f"{data['id']}")
#     # Initialize session state for selected feature IDs and associated images
#     if 'selected_feature_ids' not in st.session_state:
#         st.session_state['selected_feature_ids'] = []
#     if 'selected_images' not in st.session_state:
#         st.session_state['selected_images'] = []

#     # Capture selected feature ID from JavaScript
#     selected_feature_id = st.text_input(
#         "Please enter text to search image:", key="input_feature_id")
#     if selected_feature_id:
#         feature_id = int(selected_feature_id)
#         if feature_id in st.session_state['selected_feature_ids']:
#             # If feature is already selected, deselect it
#             index = st.session_state['selected_feature_ids'].index(feature_id)
#             st.session_state['selected_feature_ids'].pop(index)
#             st.session_state['selected_images'].pop(index)
#         else:
#             # If feature is not selected, select it and fetch associated image
#             st.session_state['selected_feature_ids'].append(feature_id)
#             image_url = data[data['id'] == feature_id]['image_url'].values
#             if len(image_url) > 0:
#                 st.session_state['selected_images'].append(image_url[0])
#             else:
#                 st.session_state['selected_images'].append(None)

#     # Update selected feature ID from JavaScript clicks

#     js_selected_feature_id = st.query_params.get('selected_feature_id', None)
#     if js_selected_feature_id:
#         js_selected_feature_id = int(js_selected_feature_id[0])
#         if js_selected_feature_id not in st.session_state['selected_feature_ids']:
#             st.session_state['selected_feature_ids'].append(
#                 js_selected_feature_id)
#             image_url = data[data['id'] ==
#                              js_selected_feature_id]['image_url'].values
#             if len(image_url) > 0:
#                 st.session_state['selected_images'].append(image_url[0])
#             else:
#                 st.session_state['selected_images'].append(None)
#  # Display selected images in desired layout
#     num_images = len(st.session_state['selected_images'])
#     if num_images > 0:
#         st.write("Selected feature IDs:",
#                  st.session_state['selected_feature_ids'])  # Debug output

#         # Display images in rows of two
#         for i in range(0, num_images, 2):
#             col_img1, col_img2 = st.columns(2)

#             # Display first image in the current row
#             with col_img1:
#                 st.image(st.session_state['selected_images']
#                          [i], caption=f'Image {i+1}', width=100)

#             # Display second image if available in the current row
#             if i + 1 < num_images:
#                 with col_img2:
#                     st.image(st.session_state['selected_images']
#                              [i + 1], caption=f'Image {i+2}', width=100)
