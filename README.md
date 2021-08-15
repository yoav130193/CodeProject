<p align="center">
    <a href="https://github.com/3b1b/manim">
        <img src="https://raw.githubusercontent.com/3b1b/manim/master/logo/cropped.png">
    </a>
</p>

BuildDots is an engine for precise programmatic animations, designed for creating explanatory math videos.

Note, there are two versions of manim.  This repository began as a personal project by the author of [3Blue1Brown](https://www.3blue1brown.com/) for the purpose of animating those videos, with video-specific code available [here](https://github.com/3b1b/videos).  In 2020 a group of developers forked it into what is now the [community edition](https://github.com/ManimCommunity/manim/), with a goal of being more stable, better tested, quicker to respond to community contributions, and all around friendlier to get started with. See [this page](https://docs.manim.community/en/stable/installation/versions.html?highlight=OpenGL#which-version-to-use) for more details.

BuildDots runs on Python 3.6 or higher (Python 3.8 is recommended).

### Directly

```sh
# Install manimgl
pip install -e .

# Try it out
manimgl example_scenes.py OpeningManimExample
# or
manim-render example_scenes.py OpeningManimExample
```

### Directly (Windows)

1. pip3 install -r requirements.txt
2. python3 main.py


1. [Install FFmpeg](https://www.wikihow.com/Install-FFmpeg-on-Windows).
2. Install a LaTeX distribution. [MiKTeX](https://miktex.org/download) is recommended.
3. Install the remaining Python packages.
    ```sh
    git clone https://github.com/3b1b/manim.git
    cd manim
    pip install -e .
    manimgl example_scenes.py OpeningManimExample
    ```

### Mac OSX

1. pip3 install -r requirements.txt
2. python3 main.py


1. Install FFmpeg, LaTeX in terminal using homebrew.
    ```sh
    brew install ffmpeg mactex
    ```
   
2. Install latest version of manim using these command.
    ```sh
    git clone https://github.com/3b1b/manim.git
    cd manim
    pip install -e .
    manimgl example_scenes.py OpeningManimExample
    ```

## Anaconda Install

1. Install LaTeX as above.
2. Create a conda environment using `conda create -n manim python=3.8`.
3. Activate the environment using `conda activate manim`.
4. Install manimgl using `pip install -e .`.


## Using buildDots
Try running the following:
```sh
manimgl example_scenes.py OpeningManimExample
```




