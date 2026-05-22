# 404—GEN Blender Add-on
**Version:** v0.14.2 (Released May 2026)

[![Discord](https://img.shields.io/discord/1065924238550237194?logo=discord&logoColor=%23FFFFFF&logoSize=auto&label=Discord&labelColor=%235865F2)](https://discord.gg/404gen)
[![Create Release](https://github.com/404-Repo/404-gen-blender-add-on/actions/workflows/create-release.yml/badge.svg)](https://github.com/404-Repo/404-gen-blender-add-on/actions/workflows/create-release.yml)

## Overview
The **404—GEN** Blender Add-on is a decentralized, AI-powered toolset designed to generate production-ready 3D Meshes and 3D Gaussian Splats (3DGS) natively in Blender. 

[Project Repo](https://github.com/404-Repo/404-gen-subnet) | [Website](https://404.xyz/) | [X](https://x.com/404gen_)

### Core Components
* **3D Generation:** A text or 2D-to-3D asset generation engine.
* **Splat Editing:** Geometry and Shader Node trees that allow users to view and edit Gaussian Splats natively in Blender.
* **Mesh Conversion for 3DGS:** A specialized texture baking and mesh generation pipeline optimized for 3D Gaussian Splats.

> 🔑 **API & Access:** Features personal API key integration for uninterrupted service, with credit top-ups managed directly via [gen.404.xyz](https://gen.404.xyz).

### Software Requirements
* **Blender 4.5+** ([Download Here](https://www.blender.org/download/))

---

## Installation

### Step 1: Download the Add-on
Download the latest release ZIP file from Gumroad. **Do not unzip the file.**

### Step 2: Install via Blender Preferences
1. Open Blender and navigate to `Edit` ➡️ `Preferences` ➡️ `Add-ons`.
2. Click **Install from Disk...** in the top right corner.
3. Select the downloaded addon ZIP file and click **Install Add-on**.

<img width="659" height="448" alt="Blender Preferences Window" src="https://github.com/user-attachments/assets/44e80616-00fe-4f5d-8b09-6c1a6ca9a16d" />

> [!IMPORTANT]
> **Note for Upgrading Users:** If you have a previous version enabled, you must uninstall it and restart Blender before installing the new version.

### Step 3: Enable and Install Dependencies
1. Check the box next to **404—GEN** to enable it.
2. Expand the add-on dropdown menu.
3. Click **[Install Dependencies]**.
4. Review the Privacy Notice and click **[Accept]**.

> [!TIP]
> **Windows Users:** If the dependency installation fails, close Blender, right-click the Blender icon, select **Run as Administrator**, and then retry this step.

> [!WARNING]
> **Do not change the default URL.**

---

## Usage Guide

### Step 1: Access the Interface
Press <kbd>N</kbd> on your keyboard (or click the small arrow in the viewport) to expand the sidebar panel and select the **404 Tab**.

<img width="410" height="310" alt="Text Prompt" src="https://github.com/user-attachments/assets/d103a005-c6f4-4440-abbb-8e401597eeb6" />


### 1. Generating from a Text Prompt
1. Type your description into the **Text Prompt Field**.
2. Click **[Generate]**.

> 💡 **Best Practices:** Describe a single object or character. Avoid generating complex multi-object scenes or entire rooms at once. Read more in the [Prompts Guide](#).

### 2. Generating from a 2D Image Prompt
1. Click the **Open Image** folder icon.
2. Select your 2D source image and click **[Generate]**.

   <img width="475" height="472" alt="Image Prompt" src="https://github.com/user-attachments/assets/a337a6dd-ee7c-4b2a-90fc-58b8e9d998dd" />


> 💡 **Best Practices:** Use high-resolution images (up to **1024x1024 max**) featuring a clean, isolated object on a solid white background.

> [!WARNING]
> The Text Prompt Field is completely disabled when a 2D image prompt is active.

### 3. Viewport Shading Setup
To view the generated material properly in Object or Edit mode:
* Press <kbd>Z</kbd> to open the Shading Menu and select **Material Preview** (or press <kbd>2</kbd>).

---

## Personal API Keys

By default, the 404—GEN Blender Add-on uses a public, shared API key. This means you might encounter rate limits during peak hours, even if you haven't generated much yourself.

### For Uninterrupted Access:
1. **Sign Up:** Head to [gen.404.xyz](https://gen.404.xyz) and create an account via Email, GitHub, or Discord.
2. **Add Credits:** Top up your account balance to power your generations.
3. **Generate Your Key:** Create a personal API Key in your web dashboard.
4. **Link to Blender:** Paste the key into the API field located under `Edit` ➡️ `Preferences` ➡️ `Add-ons` ➡️ `404—GEN`.

> [!NOTE]
> **Fair Billing Policy:** You only pay for successful generations. If a generation fails for any reason, the credit cost is automatically refunded to your balance.

---

## Mesh Conversion for 3DGS

Once a Gaussian Splat is generated, the **Splat Display Settings** and **Mesh Conversion** dropdown menus will become available.

> [!WARNING]
> **Avoid Modifier Application:** Applying the geometry nodes modifier directly will result in a massive, high-poly mesh that degrades drastically if simplified. For optimal visual quality and poly-count control, always use the custom **[Generate Mesh]** button.

<img width="399" height="743" alt="Mesh Conversion" src="https://github.com/user-attachments/assets/8e1bf5b3-e993-4eb7-8056-c2ed1c079780" />


### Splat Display Settings Reference

| Setting | Description |
| :--- | :--- |
| **Opacity Threshold** | Filters out fully or partially transparent ellipsoids. Elements below this threshold are hidden. |
| **Display Percentage** | Controls the percentage of total Gaussian Splat points displayed in the viewport. |
| **Min Detail Size** | Controls the density of the generated mesh. Lower values yield higher geometric detail. |
| **Simplify** | Decimates and smooths the final extracted mesh. Higher values produce lighter, smoother meshes. |
| **Angle Limit** | Adjusts the UV unwrapping angle constraint. Lower this value if the final texture exhibits black or missing artifacts. |
| **Texture Size** | Sets the resolution of the baked texture maps in pixels (e.g., 2048). |


