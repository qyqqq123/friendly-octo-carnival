import streamlit as st
from gtts import gTTS
import os

# 设置页面配置
st.set_page_config(page_title="东南亚与中文反诈语音库", page_icon=":shield:")

# 定义反诈知识数据
anti_fraud_knowledge = {
    "中文": [
        "网络刷单多陷阱，轻松赚钱是幻影。先给甜头引上钩，大额投入全赔净。",
        "交友平台要谨慎，甜言蜜语藏陷阱。索要钱财别轻信，爱情不是交易品。"
    ],
    "东南亚（以泰语为例）": [
        "การทำงานล่วงเวลาภายในเครือข่ายมีข้อผิดพลาดมากมาย ความสำเร็จในการหาเงินง่ายๆ เป็นภาพลวงตา. ให้ความรู้สึกดีเพื่อดึงดูดเข้ามา และการลงทุนจำนวนมากจะสูญเสียทั้งหมด.",
        "ต้องระมัดระวังในแพลตฟอร์มการแชท คำพูดหวาน ๆ มีข้อผิดพลาดอยู่เบื้องหลัง. อย่าเชื่อคำขอเงิน เพื่อนรักไม่ใช่สิ่งซื้อขาย."
    ]
}

# 页面标题
st.title("东南亚与中文反诈语音库")

# 选择语言
language = st.selectbox("选择语言", list(anti_fraud_knowledge.keys()))

# 显示反诈知识列表
st.subheader(f"{language} 反诈知识")
for index, knowledge in enumerate(anti_fraud_knowledge[language]):
    st.write(f"{index + 1}. {knowledge}")

    # 播放语音按钮
    if st.button(f"播放 {language} 第 {index + 1} 条语音"):
        try:
            # 根据语言选择合适的语言代码
            if language == "中文":
                lang_code = "zh-CN"
            elif language == "东南亚（以泰语为例）":
                lang_code = "th"

            # 使用 gTTS 将文本转换为语音
            tts = gTTS(text=knowledge, lang=lang_code)
            audio_file = f"audio_{index}.mp3"
            tts.save(audio_file)

            # 在 Streamlit 中播放语音
            with open(audio_file, "rb") as f:
                audio_bytes = f.read()
            st.audio(audio_bytes, format="audio/mp3")

            # 删除临时音频文件
            os.remove(audio_file)
        except Exception as e:
            st.error(f"语音播放出错: {e}")
    
