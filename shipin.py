import os
import tempfile
import streamlit as st

# 预定义登录账户和密码
login_accounts = {
    "student1": "Y6nF3k9z",
    "student2": "L8jP5t4q",
    "student3": "R7kM2l5x",
    "student4": "Bj3fL2q9",
    "student5": "T4nP9m6v",
    "student6": "Qe8kL7p2",
    "student7": "W8mJ2k3r",
    "student8": "R5nG4b7x",
    "student9": "X2dL9m3k",
    "student10": "N7pB4f2w",
    "student11": "M5hT3l8n",
    "student12": "J9kP6d2f",
    "student13": "U4bL8m5z",
    "student14": "K7dN2j5r",
    "student15": "Z3gP9k1m",
    "student16": "Y8nM3l2j",
    "student17": "D6kF4t9n",
    "student18": "P3lJ7b5f",
    "student19": "S9kM5d2x",
    "student20": "F4nP3l7k",
    "student21": "L8jT2k9f",
    "student22": "G5mK9n3p",
    "student23": "Q2dL7b4n"
}


# 用于记录用户登录状态
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 用户认证函数
def authenticate(username, password):
    return username in login_accounts and login_accounts[username] == password

# 登录表单
def login_form():
    st.title("🎓 课程登录")
    st.write("请输入您的用户名和密码登录课程")
    username = st.text_input("用户名").strip()
    password = st.text_input("密码", type="password").strip()
    if st.button("登录"):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.session_state.run_once = True  # 标志变量，避免多次重新加载
            st.write("🔄 数据正在加载，请稍候...")
            st.experimental_rerun()
        else:
            st.error("❌ 用户名或密码错误，请重试。")

# 在 main 函数的开头检查 run_once
if 'run_once' in st.session_state:
    del st.session_state.run_once  # 清除标志位

# XOR 解密函数
def xor_decode(data, key):
    return bytearray([b ^ key for b in data])

# 解密音频文件
def decode_audio(input_path, key=123):
    with open(input_path, 'rb') as f:
        encoded_data = f.read()
    return xor_decode(encoded_data, key)

# 章节和文件路径定义
chapters = {
    "考前指导": {
        "考前指导": "encoded/0.dat",
        "前导课": "encoded/1_0.dat"
    },
    "第1章 飲食料品製造業での管理": {
        "１．安全・安心な食 品を作る全体像": "encoded/1_1.dat",
        "２．安全な職場環境": "encoded/1_2.dat",
        "３．作業 者と管理者の違い": "encoded/1_3.dat",
        "４．管理の結果としての記録": "encoded/1_4.dat"
    },
    "第2章 安全·安心な食品製造": {
        "1.一般衛生管理": "encoded/2_1.dat",
        "2.HACCP": "encoded/2_2.dat",
        "3.生物的危害の管理": "encoded/2_3.dat",
        "4.化学的危害の管理": "encoded/2_4.dat",
        "5.物理的危害の管理": "encoded/2_5.dat",
        "6.その他の管理": "encoded/2_6.dat"
    },
    "第3章 安全・安心の管理": {
        "１．労働安全衛生法": "encoded/3_1.dat",
        "２．正しい服装と手順": "encoded/3_2.dat",
        "３．労働災害": "encoded/3_3.dat",
        "４．労働災害の防止策": "encoded/3_4.dat",
        "５．安全意識": "encoded/3_5.dat"
    },
    "第4章 品質管理": {
        "1.作業前の管理点": "encoded/4_1.dat",
        "2.作業中の管理点": "encoded/4_2.dat",
        "3.作業後の管理点": "encoded/4_3.dat"
    },
    "第5章 納期管理": {
        "1.作業前の管理点": "encoded/5_1.dat",
        "2.作業中の管理点": "encoded/5_2.dat",
        "3.作業後の管理点": "encoded/5_3.dat"
    },
    "第6章 コスト管理": {
        "1.作業前の管理点": "encoded/6_1.dat",
        "2.作業中の管理点": "encoded/6_2.dat",
        "3.作業後の管理点": "encoded/6_3.dat"
    },
    "第7章 より良い管理のために": {
        "１．製造の位置づけ": "encoded/7_1.dat",
        "２．食品ロスへの対応": "encoded/7_2.dat",
        "３．マネジメントシステム": "encoded/7_3.dat",
        "４．リスクアセスメント": "encoded/7_4.dat",
        "５．３Ｍの管理": "encoded/7_5.dat",
        "６．改善活動": "encoded/7_6.dat",
        "７．コミュニケーション": "encoded/7_7.dat"
    }
}

# 课程页面
def course_page():
    st.title("📚 课程内容")
    
    # 增加描述的字体大小
    st.markdown("<h3>请选择章节查看内容</h3>", unsafe_allow_html=True)
    st.write("")  # 空行

    # 章节选择
    st.markdown("<h4>选择章节</h4>", unsafe_allow_html=True)
    chapter = st.selectbox("", list(chapters.keys()))
    st.write("")  # 空行

    # 显示章节内容
    if chapter:
        subchapters = chapters[chapter]
        
        # 展示子章节及音频
        for subchapter_title, file_path in subchapters.items():
            st.subheader(subchapter_title)
            
            # 解码音频文件
            decoded_audio = decode_audio(file_path)
            
            # 创建临时文件
            temp_dir = tempfile.gettempdir()
            file_name = os.path.basename(file_path).replace('.dat', '.mp3')
            temp_audio_path = os.path.join(temp_dir, file_name)
            with open(temp_audio_path, 'wb') as f:
                f.write(decoded_audio)

            # 播放音频
            st.audio(temp_audio_path, format="audio/mp3")

            # 添加空行
            st.markdown("<hr>", unsafe_allow_html=True)

# 主函数
def main():
    st.set_page_config(page_title="课程平台", layout="centered", initial_sidebar_state="collapsed")

    if st.session_state.logged_in:
        course_page()
    else:
        login_form()

if __name__ == "__main__":
    main()






# import os
# import tempfile
# import streamlit as st

# # 预定义登录账户和密码
# login_accounts = {
#     "admin": "password123",
#     "student2": "password456",
#     "student3": "password789"
# }

# # 用于记录用户登录状态
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False

# # 用户认证函数
# def authenticate(username, password):
#     return username in login_accounts and login_accounts[username] == password

# # 登录表单
# def login_form():
#     st.title("🎓 课程登录")
#     st.write("请输入您的用户名和密码登录课程")
#     username = st.text_input("用户名").strip()
#     password = st.text_input("密码", type="password").strip()
#     if st.button("登录"):
#         if authenticate(username, password):
#             st.session_state.logged_in = True
#             st.write("🔄 数据正在加载，请稍候...")
#             st.experimental_rerun()
#         else:
#             st.error("❌ 用户名或密码错误，请重试。")

# # XOR 解密函数
# def xor_decode(data, key):
#     return bytearray([b ^ key for b in data])

# # 解密音频文件
# def decode_audio(input_path, key=123):
#     with open(input_path, 'rb') as f:
#         encoded_data = f.read()
#     return xor_decode(encoded_data, key)

# # 章节和文件路径定义
# chapters = {
#     "考前指导": {
#         "考前指导": "encoded/0.dat",
#         "前导课": "encoded/1_0.dat"
#     },
#     "第1章 飲食料品製造業での管理": {
#         "１．安全・安心な食 品を作る全体像": "encoded/1_1.dat",
#         "２．安全な職場環境": "encoded/1_2.dat",
#         "３．作業 者と管理者の違い": "encoded/1_3.dat",
#         "４．管理の結果としての記録": "encoded/1_4.dat"
#     },
#     "第2章 安全·安心な食品製造": {
#         "1.一般衛生管理": "encoded/2_1.dat",
#         "2.HACCP": "encoded/2_2.dat",
#         "3.生物的危害の管理": "encoded/2_3.dat",
#         "4.化学的危害の管理": "encoded/2_4.dat",
#         "5.物理的危害の管理": "encoded/2_5.dat",
#         "6.その他の管理": "encoded/2_6.dat"
#     },
#     "第3章 安全・安心の管理": {
#         "１．労働安全衛生法": "encoded/3_1.dat",
#         "２．正しい服装と手順": "encoded/3_2.dat",
#         "３．労働災害": "encoded/3_3.dat",
#         "４．労働災害の防止策": "encoded/3_4.dat",
#         "５．安全意識": "encoded/3_5.dat"
#     },
#     "第4章 品質管理": {
#         "1.作業前の管理点": "encoded/4_1.dat",
#         "2.作業中の管理点": "encoded/4_2.dat",
#         "3.作業後の管理点": "encoded/4_3.dat"
#     },
#     "第5章 納期管理": {
#         "1.作業前の管理点": "encoded/5_1.dat",
#         "2.作業中の管理点": "encoded/5_2.dat",
#         "3.作業後の管理点": "encoded/5_3.dat"
#     },
#     "第6章 コスト管理": {
#         "1.作業前の管理点": "encoded/6_1.dat",
#         "2.作業中の管理点": "encoded/6_2.dat",
#         "3.作業後の管理点": "encoded/6_3.dat"
#     },
#     "第7章 より良い管理のために": {
#         "１．製造の位置づけ": "encoded/7_1.dat",
#         "２．食品ロスへの対応": "encoded/7_2.dat",
#         "３．マネジメントシステム": "encoded/7_3.dat",
#         "４．リスクアセスメント": "encoded/7_4.dat",
#         "５．３Ｍの管理": "encoded/7_5.dat",
#         "６．改善活動": "encoded/7_6.dat",
#         "７．コミュニケーション": "encoded/7_7.dat"
#     }
# }

# # 课程页面
# def course_page():
#     st.title("📚 课程内容")
#     st.write("请选择章节查看内容")

#     # 章节选择
#     chapter = st.selectbox("选择章节", list(chapters.keys()))
#     if chapter:
#         subchapters = chapters[chapter]
        
#         # 展示子章节及音频
#         for subchapter_title, file_path in subchapters.items():
#             st.subheader(subchapter_title)
            
#             # 解码音频文件
#             decoded_audio = decode_audio(file_path)
            
#             # 创建临时文件
#             temp_dir = tempfile.gettempdir()
#             file_name = os.path.basename(file_path).replace('.dat', '.mp3')
#             temp_audio_path = os.path.join(temp_dir, file_name)
#             with open(temp_audio_path, 'wb') as f:
#                 f.write(decoded_audio)

#             # 播放音频
#             st.audio(temp_audio_path, format="audio/mp3")

#             # 添加空行
#             st.markdown("<hr>", unsafe_allow_html=True)

# # 主函数
# def main():
#     st.set_page_config(page_title="课程平台", layout="centered", initial_sidebar_state="collapsed")

#     if st.session_state.logged_in:
#         course_page()
#     else:
#         login_form()

# if __name__ == "__main__":
#     main()
