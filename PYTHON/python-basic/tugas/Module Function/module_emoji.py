def convert_mood(mood_list):
    mapping = {
        "senang": "😀",
        "biasa": "😐",
        "sedih": "😢",
        "semangat": "💪"
    }
    return list(map(lambda mood: mapping.get(mood, "❓"), mood_list))
