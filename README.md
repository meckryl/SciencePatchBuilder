# Science Patch Builder
A python script intended to streamline the process of creating a patch that reblanaces location reward scalars

## Required mods (These need to be set up before you can install):
It is highly recommended to use CKAN to install all of these with a single click: https://github.com/KSP-CKAN/CKAN

- SpaceWarp: https://github.com/SpaceWarpDev/SpaceWarp
- PatchManager: https://github.com/KSP2Community/PatchManager
- TextAssetDumper: https://github.com/KSP2Community/TextAssetDumper

## Installation:
- Download the latest version of Python: https://www.python.org/downloads/
- Download the latest item from [Releases](https://github.com/meckryl/SciencePatchBuilder/releases)
- Place the .zip file in "\<YourKSP2Installation>/BepInEx/plugins", then click "Extract here"
- Open KSP2, open Settings > Mods, then scroll down to Patch manager and make sure "Always Invalidated Cache" is on
- Go back to the title screen, click "Dump", then close the game
- In your plugins folder, find the TextAssetDumper directory, then go through Dump > text_assets and scroll down to "science_region"
- Copy the entire contents of "science_region", then go back to the SciencePatchBuilder folder and paste into *both* "science_region_default" and "science_region_updated"

## Usage:
- Edit science values in "science_region_updated" (do NOT edit "science_region_default")
- Once you are done editing, run the python script and your changes will automatically be reflected in a .patch file which will take affect the next time you run the game
