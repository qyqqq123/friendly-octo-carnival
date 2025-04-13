import streamlit as st

# 页面配置
st.set_page_config(
    page_title="链盟跨境反诈平台",
    page_icon=":shield:",
    layout="wide"
)

# 自定义CSS
st.markdown(
    """
    <style>
    .st-header {color: #005F9F;}
    .st-table th, .st-table td {text-align: left; padding: 8px;}
    </style>
    """,
    unsafe_allow_html=True
)

# 主标题
st.title("《链盟：基于联邦学习与区块链的中国-东盟跨境反诈协同防御平台》")
st.divider()

# 项目背景
st.header("一、项目背景")
st.subheader("1. 政策背景")
st.markdown("- 中国-东盟《落实战略伙伴关系联合宣言行动计划（2021-2025）》")
st.markdown("- 2023年《中老缅泰柬越六国联合打击电诈行动》")

st.subheader("2. 社会痛点")
st.markdown("- **数据**：2022年东南亚电诈涉案超300亿美元，中缅边境窝点超2000个")
st.markdown("- **问题**：语言障碍、证据链断裂、文化冲突")
st.divider()

# 技术架构图
st.header("二、技术架构图")
st.graphviz_chart("""digraph { graph [rankdir=LR]; A->B; A->C; B->D; C->D; D->E; node [label="多语言诈骗识别层", fontname="微软雅黑"]; B [label="联邦学习数据协同层"]; C [label="区块链存证层"]; D [label="跨境预警决策层"]; E [label="多模态反诈应用层"]; }""")
st.divider()

# 核心功能模块
st.header("三、核心功能模块")
data = [["东南亚方言反诈语音库", "Wav2Vec 2.0迁移学习+标注", "100小时语音数据集"], ["跨境证据链管理系统", "Hyperledger Fabric存证", "中老警方3D可视化案例"], ["文化适配宣传生成器", "Stable Diffusion+提示词", "印尼皮影戏短视频"]]
st.table(data)
st.divider()

# 其他模块（商业模式、社会价值等按文档补充...）

if __name__ == "__main__":
    pass