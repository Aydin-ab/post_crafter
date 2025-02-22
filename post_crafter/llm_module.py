from openai import OpenAI

from dotenv import load_dotenv
import os
from datetime import datetime

from getpass import getpass
import requests
from datetime import datetime, timedelta
import json

class LLM:
    def __init__(self, company_description=None):
        # Read the API key from the dotenv
        load_dotenv()
        if "CLOUDFLARE_API_TOKEN" in os.environ:
            self.api_token = os.environ["CLOUDFLARE_API_TOKEN"]
        else:
            self.api_token = getpass("Enter you Cloudflare API Token")


        if "CLOUDFLARE_ACCOUNT_ID" in os.environ:
            self.account_id = os.environ["CLOUDFLARE_ACCOUNT_ID"]
        else:
            self.account_id = getpass("Enter your account id")

        # Set the company description
        self.company_description = company_description

        # Set the models
        self.txt_to_img_model = "@cf/lykon/dreamshaper-8-lcm"
        #self.txt_to_txt_model = "@cf/meta/llama-3-8b-instruct" # TOO SLOW, use openrouter instead


        # OPTIONAL
        if "OPENROUTER_KEY" in os.environ:
            self.openrouter_api_key = os.environ["OPENROUTER_KEY"]
        else:
            self.openrouter_api_key = getpass("Enter your OpenRouter API Key")

        self.openrouter_client = OpenAI(
          base_url="https://openrouter.ai/api/v1",
          api_key=self.openrouter_api_key,
        )

    def generate_image(self, product_description, output_file="output.png", caption=None) :
        # Specify in the prompt that the image must be photo realist
        prompt = f"Realistic image of the following product description:\n{product_description}"
        # If a caption is provided, add it to the prompt
        if caption:
            prompt += f"\n\nCaption of the image should be: {caption}"
        # Call the API to generate the image
        response = requests.post(
                    f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/ai/run/{self.txt_to_img_model}",
                    headers={"Authorization": f"Bearer {self.api_token}"},
                    json={"prompt": prompt}
                )
        with open(output_file, "wb") as file:
            file.write(response.content)

    '''
    def generate_caption(self, product_description):
        prompt = f"Create adequate and trend-relevant captions for the following product description:\n{product_description}\n\nCaption:"
        response = requests.post(
            f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/ai/run/{self.txt_to_txt_model}",
            headers={"Authorization": f"Bearer {self.api_token}"},
            json={"messages": [
                {"role": "system", "content": self.company_description},
                {"role": "user", "content": prompt}
            ]}
        )
        return response.json()["result"]["response"]
    '''

    def generate_caption(self, product_description):
        prompt = f"Create one adequate and trend-relevant caption for the following product description:\n{product_description}\n\nCaption:"
        completion = self.openrouter_client.chat.completions.create(
          model="meta-llama/llama-3-8b-instruct:free",
          messages=[
            {
              "role": "system",
              "content": self.company_description
            },
            {
              "role": "user",
              "content": prompt
            }
          ]
        )
        return completion.choices[0].message.content
  
    '''
    def generate_calendar_event(self, product_description, frequency_days, start_date= None, num_events= 10):
        # If the start date is not provided, use today's date
        if not start_date:
            start_date = datetime.now().strftime('%m/%d/%Y')

        prompt = f"Create a posting calendar for the following product description:\n{product_description}. The events should happen every {frequency_days} days starting on the {start_date}. Create the next {num_events} events\n\nCalendar:"
        response = requests.post(
            f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/ai/run/{self.txt_to_txt_model}",
            headers={"Authorization": f"Bearer {self.api_token}"},
            json={
                "prompt": prompt,
                "messages": [
                {"role": "system", "content": self.company_description},
                {"role": "user", "content": prompt}
                ],
                "max_tokens": 2048,
            }
        )
        return response.json()["result"]["response"]
    '''

    def generate_events_schedule(self, product_description, frequency_days, start_date= None, num_events= 10):
        # If the start date is not provided, use today's date
        if not start_date:
            start_date = datetime.now().strftime('%m/%d/%Y')

        prompt = f"Create a posting calendar for the following product description:\n{product_description}. The events should happen every {frequency_days} days starting on the {start_date}. The date should be in format <'%m/%d/%Y'> and the calendar should be a list of <date>: <event>. Create the next {num_events} events\n\nCalendar:"
        completion = self.openrouter_client.chat.completions.create(
          model="meta-llama/llama-3-8b-instruct:free",
          messages=[
            {
              "role": "system",
              "content": self.company_description
            },
            {
              "role": "user",
              "content": prompt
            }
          ]
        )
        return completion.choices[0].message.content
    
    # Create a function to generate a calendar of posts to do for a specific product description
    # The posts should include a caption generated by the generate_caption function above and an image generated by the generate_image function above
    # The posts should happen every frequency_days starting on the start_date (default to today)
    # Create the next num_events events in the calendar (default to 10)
    # The function should return a list of dictionaries with the following keys: "date", "caption", "image"
    # The "date" should be in MM/DD/YYYY format
    # The "caption" should be the caption generated by the generate_caption function
    # The "image" should be the image generated by the generate_image function, saved in a file at <project_name>/output_<date>.png where <date> is the date of the post in MM_DD_YYYY format (e.g. 01_01_2023) and project_name is the name of the project given as an argument to the function
    def generate_posts_schedule(self, product_description, frequency_days, start_date= None, num_events= 10, project_name=None):
        # If the start date is not provided, use today's date
        if not start_date:
            start_date = datetime.now().strftime('%m/%d/%Y')
        # If the project name is not provided, use a shortened product description
        if not project_name:
            # To sanitize the project name, we keep only alphanumeric characters
            project_name = "".join(c for c in product_description if c.isalnum())
            # If the project name is too long, we truncate it
            if len(project_name) > 10:
                project_name = project_name[:10]
        
        # Create a directory to store the images
        os.makedirs(project_name, exist_ok=True)

        # Create an empty list to store the events
        events = []
        # Generate the next num_events events
        for i in range(num_events):
            # Calculate the date of the event
            date = datetime.strptime(start_date, '%m/%d/%Y') + timedelta(days=i*frequency_days)
            date_str = date.strftime('%m/%d/%Y')
            # Generate the caption
            caption = self.generate_caption(product_description)
            # Generate the image
            image_file = f"{project_name}/output_{date.strftime('%m_%d_%Y')}.png"
            self.generate_image(product_description, image_file, caption)
            # Add the event to the list
            events.append({"date": date_str, "caption": caption, "image": image_file})
        
        # Save the events to a json file
        with open(f"{project_name}/schedule.json", "w") as file:
            json.dump(events, file)
        return events


  
# Usage:
#llm = LLM()
#print(llm.generate_events_schedule("a pair of sport shoe that you can wear to the gym. They should be comfortable, durable and stylish.", 7, "01/01/2023", 3,))
