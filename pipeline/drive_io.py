import os
import zipfile
import gdown
import config


def fetch_resumes_from_drive():
    """
    Fetch resumes from Google Drive. Downloads a ZIP file
    and extracts its contents to a local folder.
    Returns a list of file paths to the resumes.
    """
    try:
        # Download the dataset ZIP file
        url = config.GDOWN_URL
        output = config.RESUME_DATASET_ZIP
        gdown.download(url, output, quiet=False)

        # Extract the ZIP file to the specified folder
        with zipfile.ZipFile(output, 'r') as zip_ref:
            zip_ref.extractall(config.RESUME_FOLDER)

        # Walk the folder to list all resume file paths
        file_paths = []
        for root, dirs, files in os.walk(config.RESUME_FOLDER):
            for file in files:
                file_paths.append(os.path.join(root, file))
        return file_paths
    except Exception as e:
        print(f"Can not fetch resumes from drive: {e}")
