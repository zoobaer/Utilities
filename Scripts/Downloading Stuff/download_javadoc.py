import os
import requests
import zipfile
import io

# Config
version = "3.3.6"  # Change to desired version
group = "org.lwjgl"
base_url = "https://repo1.maven.org/maven2"
output_dir = "docs"

# LWJGL modules (official set as per https://www.lwjgl.org/customize)
artifacts = [
    "lwjgl",
    "lwjgl-assimp",
    "lwjgl-bgfx",
    "lwjgl-cuda",
    "lwjgl-egl",
    "lwjgl-glfw",
    "lwjgl-jawt",
    "lwjgl-jemalloc",
    "lwjgl-libdivide",
    "lwjgl-llvm",
    "lwjgl-lmdb",
    "lwjgl-lz4",
    "lwjgl-meow",
    "lwjgl-meshoptimizer",
    "lwjgl-nanovg",
    "lwjgl-nfd",
    "lwjgl-nuklear",
    "lwjgl-odbc",
    "lwjgl-openal",
    "lwjgl-opencl",
    "lwjgl-opengl",
    "lwjgl-opengles",
    "lwjgl-openvr",
    "lwjgl-par",
    "lwjgl-remotery",
    "lwjgl-rpmalloc",
    "lwjgl-shaderc",
    "lwjgl-spvc",
    "lwjgl-sse",
    "lwjgl-stb",
    "lwjgl-tinyexr",
    "lwjgl-tinyfd",
    "lwjgl-tootle",
    "lwjgl-vma",
    "lwjgl-vulkan",
    "lwjgl-xxhash",
    "lwjgl-yoga",
    "lwjgl-zstd"
]

def download_and_extract(artifact):
    jar_name = f"{artifact}-{version}-javadoc.jar"
    jar_url = f"{base_url}/{group.replace('.', '/')}/{artifact}/{version}/{jar_name}"
    print(f"Downloading {jar_name}...")

    response = requests.get(jar_url)
    if response.status_code != 200:
        print(f"❌ Failed to download {jar_name} (status code {response.status_code})")
        return

    extract_path = os.path.join(output_dir, artifact)
    os.makedirs(extract_path, exist_ok=True)

    with zipfile.ZipFile(io.BytesIO(response.content)) as jar:
        jar.extractall(extract_path)
        print(f"✅ Extracted to {extract_path}")

def main():
    os.makedirs(output_dir, exist_ok=True)
    for artifact in artifacts:
        download_and_extract(artifact)

if __name__ == "__main__":
    main()
