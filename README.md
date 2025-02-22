# Post Crafter

**Post Crafter** is a Python-based CLI tool for creating images, captions, and event calendars powered by Cloudflare’s AI services (and optionally OpenRouter). It streamlines content creation by automating tasks like generating product images, writing captions, and building posting schedules.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
   - [Available Commands](#available-commands)
6. [Getting Your API Keys](#getting-your-api-keys)
   - [Cloudflare API Token](#cloudflare-api-token)
   - [Cloudflare Account ID](#cloudflare-account-id)
   - [OpenRouter Key (Optional)](#openrouter-key-optional)
7. [License](#license)
8. [Troubleshooting](#troubleshooting)

---

## Features

- **Generate Images**: Send text prompts to Cloudflare’s image-generation model.
- **Generate Captions**: Produce trend-relevant captions for social media.
- **Generate Events Schedule**: Build a schedule of events, given a product description and the events frequency in days.
- **Generate Posts Schedule***: Build a schedule of posts, complete with images and captions for each date.

---

## Requirements

- Python 3.12 or higher
- [pip](https://pip.pypa.io/en/stable/installing/) for package management

---

## Installation

1. **Clone** this repository (or download the source):
   ```bash
   git clone https://github.com/Aydin-ab/post_crafter.git
   ```
2. **Navigate** into the project directory:
   ```bash
   cd post_crafter
   ```

*Alternative 1: Using pip install -e . (Recommended)*

3. **Make sure** you have Python >=3.12 installed
4. **Install** in editable mode (developer mode):
   ```bash
   pip install -e .
   ```
   This command:
   - Installs the Python package and its dependencies.
   - Registers the CLI tool `post-crafter` on your PATH.

> **Note**: If you want to install in a virtual environment, create/activate it first.

*Alternative 2: Using conda_env.yaml*

3. **Run** 
   ```bash
   conda env create -f conda_env.yaml
   ```
   This command:
   - Create a new conda environment `post_crafter` with Python 3.12 and the dependencies in the `requirements.txt`file.

4. **Enter** the new conda environment once it's done being created.
   ```bash
   conda activatepost_crafter
   ```
5. **Install** in editable mode (developer mode):
   ```bash
   pip install -e .
   ```
   This command:
   - Registers the CLI tool `post-crafter` on your PATH.

---

## Configuration

Post Crafter looks for the following environment variables:

- `CLOUDFLARE_API_TOKEN`  
  Your Cloudflare API token for AI services.  
- `CLOUDFLARE_ACCOUNT_ID`  
  Your Cloudflare account ID.  
- `OPENROUTER_KEY`
  An API key for OpenRouter if you want to use the OpenRouter-based endpoints.

You can **set** these environment variables manually:
```bash
export CLOUDFLARE_API_TOKEN="your-cloudflare-api-token"
export CLOUDFLARE_ACCOUNT_ID="your-cloudflare-account-id"
export OPENROUTER_KEY="your-openrouter-key"  # optional
```

Or **create a `.env` file** in your project root (if you’re using [python-dotenv](https://pypi.org/project/python-dotenv/)):
The `.env.sample` is just a template. The file name MUST BE `.env`
```
CLOUDFLARE_API_TOKEN=your-cloudflare-api-token
CLOUDFLARE_ACCOUNT_ID=your-cloudflare-account-id
OPENROUTER_KEY=your-openrouter-key
```

---


## Getting Your API Keys

*Cloudflare API Token and Account ID*

1. Log in to [Cloudflare dashboard](https://dash.cloudflare.com/) and select your account.
2. Go to **AI** → **Workers AI**.
3. Select **Use REST API**
4. Select **Create a Workers AI API Token**.
5. Select **Create API Token**.
6. Copy the token and set it as `CLOUDFLARE_API_TOKEN`.
7. The account ID will be displayed on the same page, copy it and set it as `CLOUDFLARE_ACCOUNT_ID`

*OpenRouter Key*

Create an account if you don't have one already [OpenRouter account](https://openrouter.ai/):

1. Go to your user settings (your profile picture in the top right).
2. Go to `Keys`
3. Create a key, copy it and set it as `OPENROUTER_KEY`

---

## Usage

*Option 1 : Command-Line Interface*

After installation, you should have the command `post-crafter`. 
Run:

```bash
post-crafter --help
```

This prints top-level usage and subcommands. Each subcommand also accepts `--help`.

```
usage: post-crafter [-h] {generate_image,generate_caption,generate_events_schedule,generate_posts_schedule} ...

CLI tool for interacting with the LLM class.

options:
  -h, --help            show this help message and exit

Commands:
  {generate_image,generate_caption,generate_events_schedule,generate_posts_schedule}
                        Choose a command to run.
    generate_image      Generate an image based on a product description.
    generate_caption    Generate a caption for a product description.
    generate_events_schedule
                        Generate a schedule of events for a product.
    generate_posts_schedule
                        Generate a calendar of events, including images and captions.
```

Below is a quick overview of available subcommands.

1. **Generate Image**
   ```bash
   post-crafter generate_image --help
   ```
   ```
   usage: post-crafter generate_image [-h] --product_description PRODUCT_DESCRIPTION

   options:
   -h, --help            show this help message and exit
   --product_description PRODUCT_DESCRIPTION, -p PRODUCT_DESCRIPTION
                           A description of the product to generate an image for.
   ```

   Example:
   ```bash
   post-crafter generate_image --product_description "Stylish running shoes"
   ```
   Saves `output.png` in the current directory.

2. **Generate Caption**
   ```bash
   post-crafter generate_caption --help
   ```
   ```
   usage: post-crafter generate_caption [-h] --product_description PRODUCT_DESCRIPTION

   options:
   -h, --help            show this help message and exit
   --product_description PRODUCT_DESCRIPTION, -p PRODUCT_DESCRIPTION
                           Product description to generate a caption for.
   ```

   Example:
   ```bash
   post-crafter generate_caption --product_description "Comfortable and trendy sunglasses"
   ```
   Prints a generated caption to stdout.

3. **Generate Events Schedule**
   ```bash
   post-crafter generate_events_schedule --help
   ```
   ```
   usage: post-crafter generate_events_schedule [-h] --product_description PRODUCT_DESCRIPTION --frequency_days FREQUENCY_DAYS
                                                [--start_date START_DATE] [--num_events NUM_EVENTS]

   options:
   -h, --help            show this help message and exit
   --product_description PRODUCT_DESCRIPTION, -p PRODUCT_DESCRIPTION
                           A description of the product to create a schedule of events for.
   --frequency_days FREQUENCY_DAYS, -f FREQUENCY_DAYS
                           Interval (in days) between events.
   --start_date START_DATE, -s START_DATE
                           Start date in MM/DD/YYYY format. Defaults to today's date if not provided.
   --num_events NUM_EVENTS, -n NUM_EVENTS
                           Number of events to create in the calendar.
   ```

   Example:
   ```bash
   post-crafter generate_events_schedule \
       --product_description "Gym pair of shoe" \
       --frequency_days 7 \
       --start_date "03/01/2025" \
       --num_events 5
   ```
   Prints out a schedule of events.

4. **Generate Posts Schedule**
   ```bash
   post-crafter generate_posts_schedule --help
   ```
   ```
   usage: post-crafter generate_posts_schedule [-h] --product_description PRODUCT_DESCRIPTION --frequency_days FREQUENCY_DAYS
                                             [--start_date START_DATE] [--num_events NUM_EVENTS] [--project_name PROJECT_NAME]

   options:
   -h, --help            show this help message and exit
   --product_description PRODUCT_DESCRIPTION, -p PRODUCT_DESCRIPTION
                           A product description or topic for generating events.
   --frequency_days FREQUENCY_DAYS, -f FREQUENCY_DAYS
                           Interval (in days) between events.
   --start_date START_DATE, -s START_DATE
                           Start date in MM/DD/YYYY format. Defaults to today's date if not provided.
   --num_events NUM_EVENTS, -n NUM_EVENTS
                           Number of events to create in the calendar.
   --project_name PROJECT_NAME, -pn PROJECT_NAME
                           Optional custom project name. If not provided, a short sanitized name from product_description is used.
   ```

   Example:
   ```bash
   post-crafter generate_posts_schedule \
       --product_description "Smooth bamboo bedsheets spring collection" \
       --frequency_days 7 \
       --start_date "02/25/2025" \
       --num_events 5 \
       --project_name "bamboo-bedsheets"
   ```
   - Creates a new directory (e.g., `bamboo-bedsheets`).
   - Generates images and captions for each event date.
   - Stores them in the directory along with an `schedule.json` file.

*Option 2: Streamlit App Interface*
I’ve also provided a Streamlit front-end to make it easier to interact with the tool:
1. **Install dependencies (if you haven’t already):**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

3. **Open the printed URL (usually http://localhost:8501) in your web browser. You’ll see:**
- Text input fields for generating images, captions, calendars, etc.
- A button to run the generation task
---

## Troubleshooting

- **Module not found** or **Command not found**:  
  Make sure you installed the package (`pip install -e .`) and that your Python environment is active and the right version `>3.12`.  
- **Permission errors on Linux**:  
  You might need `sudo pip install -e .` if installing system-wide (though a virtual environment is recommended).  
- **Missing environment variables**:  
  Make sure to use a `.env`to store the API keys, do not use the `.env.sample`, it's only here for guidance. Double-check your `.env` or environment variables if you get authentication errors from Cloudflare or OpenRouter.  
- **Check versions**:  
  Run `pip list` to confirm you have `requests`, `python-dotenv`, etc. installed.

---

## Report
*What you've built, and any instructions for how to run it or use it*
I built a quick prototype of a caption/image generator using FREE APIs to generative models 
- We can combine both to generate a schedule of posts for social media marketing: the text-to-text model generates captions, and the text-to-image model generates the post's image
- We can also generate a schedule of events for a calendar, and then generate posts for each event

*What AI tools did you use while working?*
- I used LLama 3-8B for the text-to-text model, and dreamshaper for the text-to-image model
I picked these models because they are free and have a good balance between speed and quality
The data we're working on are quite standard (general purpose english text and images), so I didn't need to use a more specialized or overengineered model.
Main reason was to keep the costs low (i.e ZERO lol). But more on that later.

- I use the OpenRouter API to call the text-to-text model, and the Cloudfare API to call the text-to-image model
I could have used Cloudfare for Llama too but the calls were much much slower than OpenRouter (10sec vs 3sec)
I also used my personal chatgpt-o1 to help me with streamlit and to write the Cloudfare/OpenRouter API requests given their documentation

*What features would you add if you were to continue to extend the project?*
- I would add the last feature to generate a video given an image/audio/caption but there was no free API for that. Video generation is quite expensive due to the amount of data/bandwith involved
Given a budget I would use the Stable Diffusion API to generate the video. I've wrote the pseudo-code/template function in the LLM class but it's commented out

- Given a budget I would also use better text-to-image models and get hyper-realistic high definition images, but it's quite expensive to call these APIs

- I would also work on the UI/UX to make it more user-friendly and add more options to customize the generated content
For example I would have add a calendar and populate it with the generated events & posts, and allow the user to view the events and posts in a more visual way

- I would also add more error handling and logging to make the tool more robust. In case the API calls fail, the user should know what happened



Happy Crafting!