import streamlit as st
import random

st.set_page_config(layout="wide")

def replace_with_dots(text):
    text_list = list(text)
    num_dots = len(text_list) // 5
    dot_positions = random.sample(range(len(text_list)), num_dots)
    for pos in dot_positions:
        text_list[pos] = '.'
    return ''.join(text_list)

def mix_letters(text):
    def shuffle_word(word):
        if len(word) <= 3:
            return word
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]

    words = text.split()
    shuffled_text = ' '.join(shuffle_word(word) for word in words)
    return shuffled_text

def remove_spaces(text):
    return text.replace(" ", "")

def add_random_spaces(text):
    text_without_spaces = remove_spaces(text)
    num_spaces = len(text) // 5
    positions = random.sample(range(len(text_without_spaces)), num_spaces)
    text_with_spaces = list(text_without_spaces)
    for pos in sorted(positions):
        text_with_spaces.insert(pos, ' ')
    return ''.join(text_with_spaces)

def expand_paragraphs_backwards(text):
    paragraphs = text.split('\n\n')
    reversed_paragraphs = ['\n\n'.join(paragraph.split('\n')[::-1]) for paragraph in paragraphs]
    return '\n\n'.join(reversed_paragraphs)

def main():
    st.markdown(
        """
        <style>
        .reportview-container .main .block-container{
            max-width: 80%;
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }
        .stTextArea, .stButton {
            font-size: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Приложение для преобразования текста")

    st.subheader("Введите ваш текст ниже:")
    text = st.text_area("Входной текст", height=300, key="input_text")

    if 'original_text' not in st.session_state:
        st.session_state.original_text = ""

    if st.button("Показать оригинальный текст"):
        st.session_state.original_text = text

    if st.button("Заменить 1/5 букв на точки"):
        st.session_state.original_text = replace_with_dots(st.session_state.original_text)

    if st.button("Перемешать буквы в словах"):
        st.session_state.original_text = mix_letters(st.session_state.original_text)

    if st.button("Удалить все пробелы"):
        st.session_state.original_text = remove_spaces(st.session_state.original_text)

    if st.button("Удалить пробелы и добавить случайные пробелы"):
        st.session_state.original_text = add_random_spaces(st.session_state.original_text)

    if st.button("Развернуть абзацы"):
        st.session_state.original_text = expand_paragraphs_backwards(st.session_state.original_text)

    st.subheader("Преобразованный текст:")
    st.text_area("Результат", value=st.session_state.original_text, height=800, key="output_text")

if __name__ == "__main__":
    main()
