import bpy
import requests
import tempfile


def request_model(prompt: str) -> None | str:

    url = bpy.context.preferences.addons[__name__.partition(".")[0]].preferences.url
    response = requests.post(url, data={"prompt": prompt})

    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".ply") as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name

        print(f"The PLY file has been downloaded and saved to {temp_file_path}")
        return temp_file_path

    print(f"Failed to download the PLY file. Status code: {response.status_code}")
    return None
