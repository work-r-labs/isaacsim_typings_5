# IsaacSim Typings

This repo contains stub files generated from NVIDIA's Isaacsim for use with vscode to enable type completion / checking

## Usage

Clone this repo and configure your vscode to use the supplied files as stubs.

https://code.visualstudio.com/docs/python/settings-reference

## Generating Stubs

If you are only looking to use the provided stub files, then you can ignore this section.

These commands will install `pybind11-stubgen` into your isaacsim python environment and then


```bash
~/isaacsim/python.sh -m pip install pybind11-stubgen
~/isaacsim/python.sh isaacsim_stubgen.py
```