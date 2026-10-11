# Player Face Recognition

An automated computer vision and deep learning pipeline designed to detect, encode, and identify sports players from video footage and images.

---

## Overview

The **Player Face Recognition** project provides an end-to-end workflow for recognizing individual players during matches or training sessions. It leverages modern facial detection and embedding models to extract facial features, index known player profiles from a dataset, and accurately identify players across image streams or video files.

---

## Project Structure

```text
player_face_recognition/
├── dataset/             # Known player reference images organized by individual/label
├── images/              # Sample test images and visual outputs
├── programs/            # Core execution scripts and Jupyter notebooks
│   └── *.ipynb / *.py   # Training, preprocessing, and inference scripts
├── github link/         # External references, demo video links, and resources
└── README.md            # Project documentation
Features
Automated Face Detection: Locates faces in cluttered sports scenes and complex angles.

Feature Extraction & Encoding: Computes distinct 128-d / deep facial embeddings for each target player.

Real-Time / Batch Recognition: Compares detected face encodings against reference embeddings using Euclidean distance or cosine similarity.

Annotated Output: Visual bounding boxes and player name tags overlaid onto target frames/videos.

Prerequisites & Installation
1. Clone the Repository
Bash
git clone [https://github.com/Rajkumar-Ai-Engineer/player_face_recognition.git](https://github.com/Rajkumar-Ai-Engineer/player_face_recognition.git)
cd player_face_recognition
2. Environment Setup
Create and activate an isolated Python virtual environment:

Bash
# Using conda
conda create -n player_rec python=3.10 -y
conda activate player_rec

# Or using venv
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3. Install Dependencies
Bash
pip install opencv-python dlib face_recognition numpy matplotlib ipykernel
Note: Installing dlib may require CMake and C++ build tools installed on your operating system.

Getting Started
Step 1: Prepare the Dataset
Place reference images of each player in the dataset/ directory.

Structure your dataset into subfolders named after each player:

Plaintext
dataset/
├── player_one/
│   ├── img1.jpg
│   └── img2.jpg
└── player_two/
    ├── img1.jpg
    └── img2.jpg
Step 2: Running via Jupyter Notebook
Launch the Jupyter Notebook environment to run the step-by-step pipeline:

Bash
jupyter notebook
Navigate to the programs/ folder and open the main recognition notebook to:

Load and inspect player reference photos.

Generate and serialize face encodings.

Run player detection and classification on target match videos or test photos.

Future Improvements
Incorporate multi-object tracking (e.g., DeepSORT, ByteTrack) to maintain continuous tracking through occlusions.

Combine facial recognition with jersey number and OCR detection for low-resolution or turned-away frames.
