#!/usr/bin/env bash
set -euo pipefail

DEST_DIR="./fourofour_3d_gen/wheels"
mkdir -p "$DEST_DIR"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

PLATFORMS=(
  "macosx_11_0_arm64"
  "win_amd64"
  "manylinux2014_x86_64"
)

IMPLEMENTATION="cp"   
PYTHON_TARGETS=(
  "3.11 cp311"
  "3.13 cp313"
)

PACKAGES=(
  "annotated-types==0.7.0"
  "certifi==2025.8.3"
  "charset-normalizer==3.4.3"
  "idna==3.10"
  "mixpanel==4.10.1"
  "pydantic==2.11.7"
  "pydantic-core==2.33.2"
  "requests==2.32.5"
  "six==1.17.0"
  "typing-extensions==4.15.0"
  "typing-inspection==0.4.2"
  "urllib3==2.5.0"
)

for pkg in "${PACKAGES[@]}"; do
  for target in "${PYTHON_TARGETS[@]}"; do
    read -r PYTHON_VERSION ABI <<< "$target"
    for plat in "${PLATFORMS[@]}"; do
      echo ">>> Downloading $pkg for $plat (Python $PYTHON_VERSION)"
      pip download \
        --dest "$TMP_DIR" \
        --only-binary=:all: \
        --no-deps \
        --platform "$plat" \
        --python-version "$PYTHON_VERSION" \
        --implementation "$IMPLEMENTATION" \
        --abi "$ABI" \
        "$pkg"
    done
  done
done

find "$DEST_DIR" -maxdepth 1 -type f -name "*.whl" -delete
mv "$TMP_DIR"/*.whl "$DEST_DIR"/
echo "All wheels downloaded into $DEST_DIR/"
