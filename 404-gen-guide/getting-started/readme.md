# 🔌 Blender Extension

[![Discord](https://img.shields.io/discord/1065924238550237194?logo=discord\&logoColor=%23FFFFFF\&logoSize=auto\&label=Discord\&labelColor=%235865F2)](https://discord.gg/404gen) [![Create Release](https://github.com/404-Repo/three-gen-blender-plugin/actions/workflows/create-release.yml/badge.svg)](https://github.com/404-Repo/three-gen-blender-plugin/actions/workflows/create-release.yml)

## [**404—GEN Blender Extension**](https://github.com/404-Repo/three-gen-blender-plugin)

## About

With this add-on, users can:

* Enter text prompts to generate **3D Gaussian Splats**
* Import .ply files
* Convert .ply to **mesh**

## Installation

### Software requirements

Blender 4.2+

### Instructions

1. Download the ZIP file of the most recent release and _**do not unzip**_

&#x20;

<figure><img src="https://github.com/user-attachments/assets/0373bedd-578a-4b46-903f-9e88a4918d57" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://github.com/user-attachments/assets/e91a8530-43bb-49bd-bffe-a2540f038c25" alt="" width="563"><figcaption></figcaption></figure>

2. In Blender, Edit ➡️ Preferences ➡️ Add-ons ➡️ Install ➡️ Select the add-on ZIP file

<figure><img src="https://github.com/user-attachments/assets/cf4710b1-4660-4c77-ae1c-be21ac23e515" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
If you have a previous version of this add-on enabled, you will need to uninstall it and restart Blender before installing the new version. You may also need to restart Blender after installing the new version.
{% endhint %}

3. Check the box to enable the add-on, then click Install Dependencies and accept the anonymous usage data notice (you may opt out after reading the notice).&#x20;

<figure><img src="https://github.com/user-attachments/assets/92145edb-012e-4279-b0e6-bbc401af346f" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Do not change the URL or API key
{% endhint %}

The 404 tab should now appear in the sidebar

<figure><img src="https://github.com/user-attachments/assets/72ac61fb-d0ae-4cef-9434-5ae760760c52" alt="" width="375"><figcaption></figcaption></figure>

## Usage

### Generating

1. Type your prompt and click Generate. Each generation should take **20 to 30 seconds**.

{% hint style="info" %}
* If the network is busy, the operation will automatically be canceled after 1 minute. Try again.
* For best results, describe a single object/element for each generation, rather than an entire scene or room at once.
* To view the material in object or edit mode, open the Shading Menu (shortcut z) and select Material Preview (shortcut 2).
{% endhint %}

2. Adjust display settings _(optional)_

After the splat is generated, the Display Settings dropdown will appear. Gaussian Splats are often rendered with some zero or low opacity points. Increasing the opacity threshold will filter out any points beneath the set threshold.

<figure><img src="https://github.com/user-attachments/assets/d65ae186-25b8-47f0-9d0d-7b3357f7e09e" alt="" width="563"><figcaption></figcaption></figure>

3. Convert to mesh _(optional)_

There are two ways to convert to mesh.

* **Low Poly**: Check the **convert** box located beneath the Display Settings dropdown. Smaller voxel size will result in a more detailed mesh, while larger voxel size will result in a lower poly count. The modifier must be applied to complete the mesh conversion\\
* **High Poly**: Apply the geometry nodes modifier **without** checking the convert box.&#x20;

<figure><img src="https://github.com/user-attachments/assets/7c00756b-3b63-4dd7-b0ff-aa3bc03459af" alt="" width="563"><figcaption></figcaption></figure>
