# 404-GEN BLENDER ADD-ON
[![Discord](https://img.shields.io/discord/1065924238550237194?logo=discord&logoColor=%23FFFFFF&logoSize=auto&label=Discord&labelColor=%235865F2)](https://discord.gg/404gen)
[![Create Release](https://github.com/404-Repo/three-gen-blender-plugin/actions/workflows/create-release.yml/badge.svg)](https://github.com/404-Repo/three-gen-blender-plugin/actions/workflows/create-release.yml)

*404-GEN leverages decentralized AI to transform your words into detailed 3D models, bringing your ideas to life in just a few seconds*  
[Project Repo](https://github.com/404-Repo/three-gen-subnet) | [Website](https://404.xyz/) | [X](https://x.com/404gen_)

## About
- This repository is specifically for the Blender add-on and does not include the 404-GEN Discord bot or web front-end.  
- With this add-on, users can:
  - Enter text prompts to generate **3D Gaussian Splats**
  - Import .ply files
  - Convert .ply to **mesh**
> [!IMPORTANT]
> Text-to-3D generation requires an API key, but import and conversion do not

## Installation
### Software requirements
Blender 4.0+  
### Instructions
1. Download the ZIP file of the most recent release and **_do not unzip_**
   
  <img width="480" alt="release" src="https://github.com/user-attachments/assets/e91a8530-43bb-49bd-bffe-a2540f038c25">

  <img width="480" alt="download" src="https://github.com/user-attachments/assets/0373bedd-578a-4b46-903f-9e88a4918d57">

2. In Blender, Edit ➡️ Preferences ➡️ Add-ons ➡️ Install ➡️ Select the add-on ZIP file
   
  <img width="480" alt="install" src="https://github.com/user-attachments/assets/cf4710b1-4660-4c77-ae1c-be21ac23e515">

> [!NOTE]
> If you have a previous version of this add-on enabled, you will need to disable it and restart Blender before installing the new version

3. Check the box to enable the add-on and paste your API key in the token field.
<img width="480" alt="addon-enable" src="https://github.com/user-attachments/assets/1da2428a-bab4-42d8-991d-1561a253fe55">

🌟 404 tab should now appear in the sidebar 🌟

<img width="480" alt="tool" src="https://github.com/user-attachments/assets/39a8f968-526d-4ac9-9b24-9a52fc7a9a0f">


## Usage
### Generating
1. Type your prompt and click Generate. Each generation should take **20 to 30 seconds**.
> [!NOTE]
>- If the network is busy, the operation will automatically be canceled after 1 minute. Try again.
>- For best results, describe a single object/element for each generation, rather than an entire scene or room at once.
>- To view the material in object or edit mode, open the Shading Menu (shortcut z) and select Material Preview (shortcut 2).

2. Adjust display settings *(optional)*\
After the splat is generated, the Display Settings dropdown will appear. Gaussian Splats are often rendered with some zero or low opacity points. Increasing the opacity threshold will filter out any points beneath the set threshold.
<img width="480" alt="display" src="https://github.com/user-attachments/assets/d65ae186-25b8-47f0-9d0d-7b3357f7e09e">


3. Convert to mesh *(optional)*\
There are two ways to convert to mesh.
  - **Low Poly**: Check the **convert** box located beneath the Display Settings dropdown. Smaller voxel size will result in a more detailed mesh, while larger voxel size will result in a lower poly count. The modifier must be applied to complete the mesh conversion\
  - **High Poly**: Apply the geometry nodes modifier **without** checking the convert box.
<img width="480" alt="mesh" src="https://github.com/user-attachments/assets/7c00756b-3b63-4dd7-b0ff-aa3bc03459af">


> [!NOTE]
> For questions or help troubleshooting, join our [Discord server](https://discord.gg/404gen).
