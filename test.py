import time

def calculate_typing_speed(words_typed, total_time):
    words_per_minute = (words_typed / total_time) * 60
    return words_per_minute

def typing_test():
    print("Welcome to the Speed Typing Test!")
    print("Type the following text as fast as you can:")
    print("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    print("Press enter when you're done.")

    input("Press enter to start...")
    start_time = time.time()

    text_to_type = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    user_input = input(text_to_type)

    end_time = time.time()
    total_time = end_time - start_time
    words_typed = len(user_input.split())
    typing_speed = calculate_typing_speed(words_typed, total_time)
    print("Time taken:", round(total_time, 2), "seconds")
    print("Words typed:", words_typed)
    print("Typing speed:", round(typing_speed, 2), "words per minute")

typing_test()
