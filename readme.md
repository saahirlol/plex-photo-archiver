# Photo Archiving Tool

## Overview

The Photo Archiving Tool is a Python script designed to automate the process of copying media files from a Plex playlist to a local directory and compressing them into multiple archive formats. It uses SSH to securely transfer files from a remote server where your Plex server is hosted. The script supports ZIP, TAR.GZ, and 7z compression formats, providing flexibility in how you archive your media.

## Features

- **Automatic Directory Creation:** The script dynamically creates a local directory named after the Plex playlist.
- **Secure File Transfer:** Files are securely transferred from the remote Plex server using SSH and SCP.
- **Multi-format Compression:** Archives the copied files into ZIP, TAR.GZ, and 7z formats with high compression.
- **Easy Configuration:** All sensitive information and customizable parameters are located at the top of the script for easy access.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.6+**
- **Pip** (Python package manager)
- **Required Python libraries**:
  - `paramiko`
  - `scp`
  - `plexapi`
  - `shutil` (built-in)
  - `tarfile` (built-in)
  - `subprocess` (built-in)

You can install the required libraries using pip:

```bash
pip install paramiko scp plexapi
```

- **p7zip** for 7z compression (Install using your package manager):
  - On Ubuntu/Debian: `sudo apt-get install p7zip-full`
  - On Fedora: `sudo dnf install p7zip`
  - On macOS (with Homebrew): `brew install p7zip`

## Setup

1. **Clone the Repository**: (If applicable)

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Configure the Script**:

   Open the script in a text editor and fill in the required details at the top:

   - `server_host`: IP address of the Plex server.
   - `token`: Plex authentication token.
   - `remote_user`: SSH username for the Plex server.
   - `remote_password`: SSH password for the Plex server.
   - `playlist_name`: Name of the Plex playlist you want to archive.

3. **Run the Script**:

   Execute the script using Python:

   ```bash
   python copy_and_compress_playlist.py
   ```

   The script will:
   - Copy the media files from the specified Plex playlist to a local directory.
   - Compress the files into ZIP, TAR.GZ, and 7z formats.
   - Save the compressed archives in the same directory.

## Example

For example, if you have a playlist named "Keido," the script will:

- Create a directory named `./Keido`.
- Copy all files from the "Keido" playlist into this directory.
- Compress the directory into `Keido.zip`, `Keido.tar.gz`, and `Keido.7z`.

## Troubleshooting

- **SSH Connection Issues**: Ensure that SSH access is properly configured on the Plex server and that the provided credentials are correct.
- **Plex Token**: Make sure you've obtained the correct Plex token; this is required to access the Plex API.
- **7z Compression**: Ensure `p7zip` is installed on your system if you wish to use 7z compression.

## Contributing

If you’d like to contribute to this project, feel free to fork the repository and submit a pull request with your improvements.

