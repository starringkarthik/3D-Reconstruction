import os
directory_path = '/content/3D-Reconstruction/pifuhd/sample_images/'
filename = None
updated_time = 0
for entry in os.scandir(directory_path):
  if entry.is_file():
    mod_time = entry.stat().st_mtime_ns
    if mod_time > updated_time:
      filename = entry.name
#try:
image_path = '/content/3D-Reconstruction/pifuhd/sample_images/%s' % filename
#except:
#  image_path = '/content/pifuhd/sample_images/test.png'
image_dir = os.path.dirname(image_path)
file_name = os.path.splitext(os.path.basename(image_path))[0]

obj_path = '/content/3D-Reconstruction/pifuhd/results/pifuhd_final/recon/result_%s_256.obj' % file_name
out_img_path = '/content/3D-Reconstruction/pifuhd/results/pifuhd_final/recon/result_%s_256.png' % file_name
video_path = '/content/3D-Reconstruction/pifuhd/results/pifuhd_final/recon/result_%s_256.mp4' % file_name
video_display_path = '/content/3D-Reconstruction/pifuhd/results/pifuhd_final/result_%s_256_display.mp4' % file_name
