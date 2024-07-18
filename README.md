# 404-GEN BLENDER ADD-ON
![Discord](https://img.shields.io/discord/1065924238550237194?logo=discord&logoColor=%23FFFFFF&logoSize=auto&label=Discord&labelColor=%235865F2)

*404-GEN leverages decentralized AI to transform your words into detailed 3D models, bringing your ideas to life in just a few seconds*  
[Project Repo](https://github.com/404-Repo/three-gen-subnet) | [Website](https://404.xyz/) | [X](https://x.com/404gen_)

## About
- This repository is specifically for the Blender add-on and does not include the 404-GEN Discord bot or web front-end.  
- With this add-on, users can enter a text prompt to generate **3D Gaussian Splatting** then apply the geometry nodes modifier to convert to **mesh**.
> [!IMPORTANT]
> Access is currently limited to those who have been provided with a custom API key. 

## Installation
### Software requirements
Blender 4.0+  
### Instructions
1️⃣ Download the ZIP file of the most recent release and **_do not unzip_**  

2️⃣ In Blender, Edit ➡️ Preferences ➡️ Add-ons ➡️ Install ➡️ Select the add-on ZIP file

> [!NOTE]
> If you have a previous version of this add-on enabled, you will need to disable it and restart Blender before installing the new version

3️⃣ Check the box to enable the add-on and paste your API key in the token field.

<img width="400" alt="addon-enable" src="https://github.com/user-attachments/assets/1da2428a-bab4-42d8-991d-1561a253fe55">

🌟 404 tab should now appear in the sidebar 🌟

<img width="400" alt="addon-sidebar" src="https://github.com/user-attachments/assets/277bddc3-be9f-46e4-bb61-905af31ffef1">

## Usage
### Generating
Type your prompt and click Generate. Each generation should take **20 to 30 seconds**.
> [!NOTE]
>- If the network is busy, the operation will automatically be canceled after 1 minute. Try again.
>- For best results, describe a single object/element for each generation, rather than an entire scene or room at once.
>- To view the material in object or edit mode, open the Shading Menu (shortcut z) and select Material Preview (shortcut 2).

### Mesh Conversion
The generated object is rendered as a .ply, however the add-on creates a Geometry Node Modifier to easily convert to mesh.
Select Modifiers 🔧 in the Properties workspace and apply the GaussianSplatting modifier.

<img width="400" alt="addon-modifier" src="https://github.com/user-attachments/assets/a4472b0f-ad29-4410-bfe0-252336309986">

> [!NOTE]
> The mesh will be quite heavy. We will update this guide to include some techniques to reduce the size of the mesh while retaining as much visual detail as possible. In the meantime, you can join our [Discord server](https://discord.gg/404gen) for help troubleshooting.
