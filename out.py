import os
from obj2html import obj2html
from IPython.display import display, HTML
import streamlit as st

os.chdir('/content/3D-Reconstruction/pifuhd/results/pifuhd_final/recon')

st.title("3D Model")

obj_files = [f for f in os.listdir() if f.endswith(".obj")]
obj_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

if obj_files:
    most_recent_obj = obj_files[0]
    obj2html(most_recent_obj, 'index.html')

    st.write("3D Reconstructed Model:")
    st.components.v1.html(open('index.html').read(), width=320, height=200)

    st.markdown("Download Object File:")
    with open(most_recent_obj, 'rb') as f:
        st.download_button('Download model.obj', f, key=most_recent_obj, file_name=most_recent_obj)

    st.link_button("Visualize using Online 3D Viewer", "https://3dviewer.net/")

else:
    st.write("No .obj files found in the directory.")
