import re # کتابخانه RegEx را فراخوانی میکنیم
import json  # برای ذخیره سازی در فرمت JSON فراخوانی میکنیم


# اینجا کلمات تکراری و بی‌معنی که زیاد تو متن هستن رو حذف می‌کنیم تا تمرکز روی کلمات مهم‌تر باشه
class WordCounter:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.text = ""
        self.words = []
        self.word_freq = {}

    def read_file(self):
        with open(self.input_path, 'r', encoding='utf-8') as file:
            self.text = file.read()

    def clean_text(self):
        # حذف ایمیل
        self.text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', '', self.text)
        # حذف لینک
        self.text = re.sub(r'https?://\S+|www\.\S+', '', self.text)
        # حذف علائم نگارشی
        self.text = re.sub(r'[^\w\u0600-\u06FF\s]', '', self.text)
        # تبدیل متن به لیست کلمات
        self.words = self.text.split()

    # لیست کلمات پرتکرار
    def remove_stopwords(self):
        stop_words = [
            'و', 'در', 'به', 'از', 'که', 'این', 'را', 'با', 'است', 'برای',
            'آن', 'یک', 'هم', 'تا', 'نیز', 'اما', 'یا', 'بر', 'اگر', 'هر',
            'چون', 'باید', 'می', 'شد', 'کند', 'کرد', 'شده', 'دیگر', 'همه',
            'نیک', 'اینجا', 'اینها', 'آنان', 'خود'
        ]
        filtered_words = []
        for word in self.words:
            if word and word not in stop_words:
                filtered_words.append(word)
        self.words = filtered_words

    # محاسبه فراوانی کلمات 
    def count_word_frequencies(self):
        freq = {}
        for word in self.words:
            freq[word] = freq.get(word, 0) + 1
        # مرتب‌سازی دیکشنری بر اساس تعداد تکرار (بیشترین به کمترین)
        self.word_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True)) # این کد باعث میشه خروجی فایل ما به ترتیب فراوانی کلمات از زیاد به کم باشه

    # اینجا میایم و فایل مون رو توی فرمت json ذخیره میکنیم
    def save_to_json(self):
        with open(self.output_path, 'w', encoding='utf-8') as file:
            json.dump(self.word_freq, file, ensure_ascii=False, indent=4)

    def process(self):
        # 1. فایل متنی رو می‌خونه
        self.read_file()
        # 2. لینک‌ها، ایمیل‌ها و علائم نگارشی رو پاک می‌کنه
        self.clean_text()
        # 3. کلمات پرتکرار (stop words) رو حذف می‌کنه
        self.remove_stopwords()
        # 4. تعداد تکرار هر کلمه رو می‌شماره
        self.count_word_frequencies()
        # 5. نتایج رو توی فایل JSON ذخیره می‌کنه
        self.save_to_json()
        # اینجا هم بهش گفتیم بیا یه پیام چاپ کن که فایل را با موفقیت ذخیره شده
        print("Json File has been saved successfully.")

# اینجا برنامه از همین فایل اجرا میشه، یه نمونه از کلاس می‌سازیم و تمام مراحل رو انجام می‌دیم
counter = WordCounter(
    '/Users/erfan/Desktop/HW_01_python/short text.txt',
    '/Users/erfan/Desktop/HW_01_python/word_frequencies.json'
)
counter.process()