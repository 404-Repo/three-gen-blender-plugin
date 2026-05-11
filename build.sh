#!/usr/bin/env bash
set -euo pipefail

./download_dependencies.sh
mkdir -p dist
blender --command extension build --source-dir ./fourofour_3d_gen --output-dir ./dist
