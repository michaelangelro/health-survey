import streamlit as st

# 각 설문 카테고리 이름과 연결 모듈 이름
categories = [
    ("⚡ 피로/활력", "fatigue"),
    ("🛡️ 면역 건강", "immune"),
    ("🌙 수면/스트레스", "stress"),
    ("🌀 장 건강", "gut"),
    ("👁️ 눈 건강", "eye"),
    ("💓 혈액순환", "blood"),
    ("🌸 피부 건강", "skin"),
    ("🦴 관절 건강", "joint"),
    ("👩 여성 건강", "women")
]

# 선택 상태 저장
st.title("🩺 건강기능식품 설문 메인 페이지")
st.subheader("카테고리를 선택해 설문을 진행하세요.")

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# 버튼 그리드 UI
cols = st.columns(3)
for idx, (label, module_name) in enumerate(categories):
    with cols[idx % 3]:
        if st.button(label):
            st.session_state.selected_category = module_name

# 설문 모듈 로드
if st.session_state.selected_category:
    if st.session_state.selected_category == "fatigue":
        import fatigue as selected_survey
    elif st.session_state.selected_category == "immune":
        import immune as selected_survey
    elif st.session_state.selected_category == "stress":
        import stress as selected_survey
    elif st.session_state.selected_category == "gut":
        import gut as selected_survey
    elif st.session_state.selected_category == "eye":
        import eye as selected_survey
    elif st.session_state.selected_category == "blood":
        import blood as selected_survey
    elif st.session_state.selected_category == "skin":
        import skin as selected_survey
    elif st.session_state.selected_category == "joint":
        import joint as selected_survey
    elif st.session_state.selected_category == "women":
        import women as selected_survey

    selected_survey.run()  # 각 설문 파일에 run() 함수 정의 필요
