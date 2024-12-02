def find_longest_words(text):
    words = text.split()
    
    cleaned_words = [word.strip(".,!?\"':;()[]") for word in words]
    
    max_length = max(len(word) for word in cleaned_words)
    longest_words = [word for word in cleaned_words if len(word) == max_length]
    
    return longest_words

text = "Chào mừng bạn đến với thế giới của lập trình Python. Hãy khám phá và học hỏi thật nhiều điều mới mẻ!"

longest_words = find_longest_words(text)
print("Những từ dài nhất trong văn bản là:", longest_words)
