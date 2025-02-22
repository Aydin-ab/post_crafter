Below is an example **README.md** you might include in your repository. Feel free to adjust the wording, formatting, and details to match your exact project needs:

---

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
- **Generate Calendars**: Build event calendars, complete with images and captions for each date.
- **OpenRouter Integration**: Optionally use an alternative model via OpenRouter if desired.

---

## Requirements

- Python 3.7 or higher
- [pip](https://pip.pypa.io/en/stable/installing/) for package management

---

## Installation

1. **Clone** this repository (or download the source):
   ```bash
   git clone https://github.com/your-username/post_crafter.git
   ```
2. **Navigate** into the project directory:
   ```bash
   cd post_crafter
   ```
3. **Install** in editable mode (developer mode):
   ```bash
   pip install -e .
   ```
   This command:
   - Installs the Python package and its dependencies.
   - Registers the CLI tool `post-crafter` on your PATH.

> **Note**: If you want to install in a virtual environment, create/activate it first.

---

## Configuration

Post Crafter looks for the following environment variables:

- `CLOUDFLARE_API_TOKEN`  
  Your Cloudflare API token for AI services.  
- `CLOUDFLARE_ACCOUNT_ID`  
  Your Cloudflare account ID.  
- `OPENROUTER_KEY` *(optional)*  
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

### Cloudflare API Token and Account ID

1. Log in to [Cloudflare dashboard](https://dash.cloudflare.com/) and select your account.
2. Go to **AI** → **Workers AI**.
3. Select **Use REST API**
4. Select **Create a Workers AI API Token**.
5. Select **Create a Workers AI API Token**.
6. Select **Create API Token**.
7. Copy the token and set it as `CLOUDFLARE_API_TOKEN`.
8. The account ID will be displayed on the same page, copy it and set it as `CLOUDFLARE_ACCOUNT_ID`

### OpenRouter Key

If you have an [OpenRouter account](https://openrouter.ai/):

1. Go to your user settings (your profile picture in the top right).
2. Go to `Keys`.
3. Create a key, copy it and set it as `OPENROUTER_KEY`

---

## Usage

After installation, you should have the command `post-crafter`. Run:

```bash
post-crafter --help
```

This prints top-level usage and subcommands. Each subcommand also accepts `--help`.

### Available Commands

Below is a quick overview of available subcommands.

1. **Generate Image**
   ```bash
   post-crafter generate_image --product_description "Stylish running shoes"
   ```
   Saves `output.png` in the current directory.

2. **Generate Caption**
   ```bash
   post-crafter generate_caption --product_description "Comfortable and trendy sunglasses"
   ```
   Prints a generated caption to stdout.

3. **Generate Calendar Event**
   ```bash
   post-crafter generate_calendar_event \
       --product_description "Gym pair of shoe" \
       --frequency_days 7 \
       --start_date "03/01/2025" \
       --num_events 5
   ```
   Prints out a schedule of events.

4. **Generate Calendar**
   ```bash
   llm generate_calendar \
       --product_description "Smooth bamboo bedsheets spring collection" \
       --frequency_days 7 \
       --start_date "02/25/2025" \
       --num_events 5 \
       --project_name "bamboo-bedsheets"
   ```
   - Creates a new directory (e.g., `bamboo-bedsheets`).
   - Generates images and captions for each event date.
   - Stores them in the directory along with an `schedule.json` file.

---

## Troubleshooting

- **Module not found** or **Command not found**:  
  Make sure you installed the package (`pip install -e .`) and that your Python environment is active.  
- **Permission errors on Linux**:  
  You might need `sudo pip install -e .` if installing system-wide (though a virtual environment is recommended).  
- **Missing environment variables**:  
  Double-check `.env` or environment variables if you get authentication errors from Cloudflare or OpenRouter.  
- **Check versions**:  
  Run `pip list` to confirm you have `requests`, `python-dotenv`, etc. installed.


Happy Crafting!