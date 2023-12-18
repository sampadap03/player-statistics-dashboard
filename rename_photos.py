import os
import pandas as pd

# Load the CSV file with the ID mappings
csv_file = 'spl.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Path to the folder containing images
image_folder = ".\\photos\\\\"  # Replace with your image folder path

# Iterate through the files in the folder
for filename in os.listdir(image_folder):
    if filename.endswith('.PNG') or filename.endswith('.png') or filename.endswith('.jpeg') \
        or filename.endswith('.jpg') or filename.endswith('.JPG'):  # Filter image files
        parts = filename.split('_')
        if len(parts) >= 2:
            # Extract the ID from the image file name
            image_id = parts[-1].split('.')[0]  # Extracting ID before extension

            # Find the corresponding ID in the CSV file
            matching_row = df[df['Name'] == str(image_id)]

            if not matching_row.empty:
                try:
                    # Get the new name from the CSV file
                    new_name = f"{matching_row['GID'].values[0]}.png"

                    # Rename the file
                    old_path = os.path.join(image_folder, filename)
                    new_path = os.path.join(image_folder, new_name)
                    os.rename(old_path, new_path)
                    print(f"Renamed {filename} to {new_name}")
                except Exception as e:
                    print(e)
            else:
                print(f"No matching ID found for {filename}")
