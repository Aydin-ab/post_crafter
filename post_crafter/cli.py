#!/usr/bin/env python3
import argparse
from .llm_module import LLM 
from datetime import datetime
import json

def main():
    parser = argparse.ArgumentParser(
        description="CLI tool for interacting with the LLM class."
    )
    subparsers = parser.add_subparsers(
        title="Commands", dest="command", help="Choose a command to run."
    )

    # --------------------------
    #  generate_image
    # --------------------------
    generate_image_parser = subparsers.add_parser(
        "generate_image", help="Generate an image based on a product description."
    )
    generate_image_parser.add_argument(
        "--product_description",
        "-p",
        required=True,
        help="A description of the product to generate an image for."
    )

    # --------------------------
    # generate_caption
    # --------------------------
    generate_caption_parser = subparsers.add_parser(
        "generate_caption", help="Generate a caption for a product description."
    )
    generate_caption_parser.add_argument(
        "--product_description",
        "-p",
        required=True,
        help="Product description to generate a caption for."
    )

    # --------------------------
    # generate_events_schedule
    # --------------------------
    generate_events_schedule_parser = subparsers.add_parser(
        "generate_events_schedule",
        help="Generate a schedule of events for a product."
    )
    generate_events_schedule_parser.add_argument(
        "--product_description",
        "-p",
        required=True,
        help="A description of the product to create a schedule of events for."
    )
    generate_events_schedule_parser.add_argument(
        "--frequency_days",
        "-f",
        type=int,
        required=True,
        help="Interval (in days) between events."
    )
    generate_events_schedule_parser.add_argument(
        "--start_date",
        "-s",
        default=None,
        help="Start date in MM/DD/YYYY format. Defaults to today's date if not provided."
    )
    generate_events_schedule_parser.add_argument(
        "--num_events",
        "-n",
        type=int,
        default=5,
        help="Number of events to create in the calendar."
    )


    # --------------------------
    # generate_posts_schedule
    # --------------------------

    generate_posts_schedule_parser = subparsers.add_parser(
        "generate_posts_schedule",
        help="Generate a calendar of events, including images and captions."
    )
    generate_posts_schedule_parser.add_argument(
        "--product_description",
        "-p",
        required=True,
        help="A description of the product to create a schedule of posts for."
    )
    generate_posts_schedule_parser.add_argument(
        "--frequency_days",
        "-f",
        type=int,
        required=True,
        help="Interval (in days) between posts."
    )
    generate_posts_schedule_parser.add_argument(
        "--start_date",
        "-s",
        default=None,
        help="Start date in MM/DD/YYYY format. Defaults to today's date if not provided."
    )
    generate_posts_schedule_parser.add_argument(
        "--num_posts",
        "-n",
        type=int,
        default=5,
        help="Number of posts to create in the calendar."
    )
    generate_posts_schedule_parser.add_argument(
        "--project_name",
        "-pn",
        default=None,
        help="Optional custom project name. If not provided, a short sanitized name from product_description is used."
    )


    # Parse the args and call the corresponding function
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    # Create an instance of LLM
    llm = LLM()

    if args.command == "generate_image":
        llm.generate_image(args.product_description)
        print("Image generated and saved as output.png")

    elif args.command == "generate_caption":
        result = llm.generate_caption(args.product_description)
        print("Caption:\n", result)

    elif args.command == "generate_events_schedule":
        result = llm.generate_events_schedule(
            product_description=args.product_description,
            frequency_days=args.frequency_days,
            start_date=args.start_date,
            num_events=args.num_events
        )
        print("Calendar:\n", result)

    elif args.command == "generate_posts_schedule":
        result = llm.generate_posts_schedule(
            product_description=args.product_description,
            frequency_days=args.frequency_days,
            start_date=args.start_date,
            num_posts=args.num_posts,
            project_name=args.project_name
        )
        print("Calendar generated successfully.\nEvents:\n", json.dumps(result, indent=2))




if __name__ == "__main__":
    main()
