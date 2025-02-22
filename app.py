# app.py
import streamlit as st
from post_crafter.llm_module import LLM

def main():
    st.title("🚀 Post Crafter 🚀")
    st.markdown("*A state of the art AI tool for social media marketing* - Forbes")
    st.markdown("*I am in love with the demo, whoever did that is the BOSS* - Sydney Sweeney")
    st.write("Generate images, captions, schedule idea of events and schedule postings with AI!")

    llm = LLM()  # Your class from post_crafter

    menu = ["Generate Image", "Generate Caption", "Generate Events Schedule", "Generate Posts Schedule"]
    choice = st.selectbox("Choose an action", menu)

    if choice == "Generate Image":
        product_description = st.text_input("Product Description", "")
        if st.button("Generate Image"):
            output_file = llm.generate_image(product_description)
            st.image(output_file, caption="Generated Image")

    elif choice == "Generate Caption":
        product_description = st.text_input("Product Description", "")
        if st.button("Generate Caption"):
            caption = llm.generate_caption(product_description)
            st.write("**Generated Caption:**", caption)

    elif choice == "Generate Events Schedule":  # Generate Calendar
        product_description = st.text_input("Product Description", "")
        frequency_days = st.number_input("Frequency Days", min_value=1, value=7)
        num_events = st.number_input("Number of Events", min_value=1, max_value=20, value=10)
        start_date = st.date_input("Start Date", value=None)
        if st.button("Generate Calendar"):
            events = llm.generate_events_schedule(
                product_description=product_description,
                frequency_days=frequency_days,
                num_events=num_events,
                start_date=start_date
            )
            st.write("**Generated Events:**", events)

    elif choice == "Generate Posts Schedule":
        product_description = st.text_input("Product Description", "")
        frequency_days = st.number_input("Frequency Days", min_value=1, value=7)
        num_events = st.number_input("Number of Events", min_value=1, max_value=20, value=10)
        start_date = st.date_input("Start Date", value=None)
        if st.button("Generate Posts Schedule"):
            posts = llm.generate_posts_schedule(
                product_description=product_description,
                frequency_days=frequency_days,
                num_events=num_events,
                start_date=start_date
            )
            # Format of posts is a list of {"date": date_str, "caption": caption, "image": image_file}
            # Now Display the posts
            for post in posts:
                st.write(f"**Date:** {post['date']}")
                st.write(f"**Caption:** {post['caption']}")
                st.image(post['image'], caption="Generated Image")

    
    st.markdown("**Report**")
    st.markdown("*What you've built, and any instructions for how to run it or use it*")
    st.markdown("I built a quick prototype of a caption/image generator using FREE APIs to generative models "
                "\n - We can combine both to generate a schedule of posts for social media marketing: the text-to-text model generates captions, and the text-to-image model generates the post's image "
                "\n - We can also generate a schedule of events for a calendar, and then generate posts for each event")

    st.markdown("*What AI tools did you use while working?*")
    st.markdown(
                "\n- I used LLama 3-8B for the text-to-text model, and dreamshaper for the text-to-image model"
                "\nI picked these models because they are free and have a good balance between speed and quality"
                "\nThe data we're working on are quite standard (general purpose english text and images), so I didn't need to use a more specialized or overengineered model"
                "\nMain reason was to keep the costs low (i.e ZERO lol). But more on that later"
                
                "\n\n- I use the OpenRouter API to call the text-to-text model, and the Cloudfare API to call the text-to-image model"
                "\nI could have used Cloudfare for Llama too but the calls were much much slower than OpenRouter (10sec vs 3sec)"
                "\nI also used my personal chatgpt-o1 to help me with streamlit and to write the Cloudfare/OpenRouter API requests given their documentation")

    st.markdown("*What features would you add if you were to continue to extend the project?*")
    st.markdown("- I would add the last feature to generate a video given an image/audio/caption but there was no free API for that. Video generation is quite expensive due to the amount of data/bandwith involved"
                "\nGiven a budget I would use the Stable Diffusion API to generate the video. I've wrote the pseudo-code/template function in the LLM class but it's commented out"
                "\n- I would also work on the UI/UX to make it more user-friendly and add more options to customize the generated content"
                "\nFor example I would have add a calendar and populate it with the generated events & posts, and allow the user to view the events and posts in a more visual way"
                "\n- I would also add more error handling and logging to make the tool more robust. In case the API calls fail, the user should know what happened")


    
    st.write("Made with ❤️ by Aydin, check the [github](https://github.com/Aydin-ab/post_crafter/tree/main)")

if __name__ == "__main__":
    main()
