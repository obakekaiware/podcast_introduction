from pathlib import Path
import streamlit as st


def disply(podcast):
    st.title(podcast["title"])
    st.image(str(podcast["image_path"]))
    st.write(podcast["description"])
    st.write(f"試聴：{podcast['audio_title']}")
    st.audio(str(podcast["audio_path"]))


if __name__ == "__main__":
    left, right = st.columns(2)

    bookmen = {
        "title": "ブックメン",
        "description": "本の紹介を行い、感想を共有するプチ読書会風の番組",
        "image_path": Path("images", "bookmen.png"),
        "audio_path": Path("audios", "bookmen.mp3"),
        "audio_title": "紹介10「魍魎の匣」「女の友情と筋肉」"
    }

    title2info = {
        "bookmen": bookmen,
    }

    with left:
        disply(title2info["bookmen"])
