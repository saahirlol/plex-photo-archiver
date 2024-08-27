import os
import paramiko
from scp import SCPClient
from plexapi.server import PlexServer
import shutil
import subprocess
import tarfile  # Import the tarfile module

# --- Sensitive Information Section ---
server_host = '100.64.0.x'  # Set this once for both Plex base URL and SSH remote host
plex_port = 32400  # Default Plex port
baseurl = f'http://{server_host}:{plex_port}'
token = '<your-plex-token>'  # Plex token

# SSH details
remote_user = '<your-ssh-username>'  # SSH username
remote_password = '<your-ssh-password>'  # SSH password

# Playlist name
playlist_name = '<your-playlist>'  # Name of the Plex playlist

# --- End of Sensitive Information Section ---

# Connect to Plex
plex = PlexServer(baseurl, token)

# Get the playlist by name
playlist = plex.playlist(playlist_name)

# Dynamically create a local directory named after the playlist
local_dir = f'./{playlist.title}'
os.makedirs(local_dir, exist_ok=True)

# Collect the file paths
file_paths = []

for item in playlist.items():
    for media in item.media:
        for part in media.parts:
            file_paths.append(part.file)

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote server
ssh.connect(server_host, username=remote_user, password=remote_password)

# Create an SCP client
scp = SCPClient(ssh.get_transport())

# Copy each file to the local directory named after the playlist
for path in file_paths:
    print(f'Copying {path} to {local_dir}')
    scp.get(path, local_path=local_dir)

# Close the SCP client and SSH connection
scp.close()
ssh.close()

# Compress the directory to a ZIP file
zip_file = f'{local_dir}.zip'
shutil.make_archive(local_dir, 'zip', local_dir)
print(f"Compressed {local_dir} to {zip_file}")

# Compress the directory to a .tar.gz file (high compression)
tar_gz_file = f'{local_dir}.tar.gz'
with tarfile.open(tar_gz_file, 'w:gz') as tar:
    tar.add(local_dir, arcname=os.path.basename(local_dir))
print(f"Compressed {local_dir} to {tar_gz_file}")

# Compress the directory to a .7z file (requires p7zip installed)
seven_z_file = f'{local_dir}.7z'
subprocess.run(['7z', 'a', '-mx=9', seven_z_file, local_dir])
print(f"Compressed {local_dir} to {seven_z_file}")

print(f"All files from the playlist '{playlist.title}' copied and compressed successfully!")
