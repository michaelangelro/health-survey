import streamlit as st

# 수면/스트레스 설문 문항
questions = [
    "잠들기까지 30분 이상 걸리는 경우가 많다.",
    "수면 중 자주 깨거나, 깊게 못 자는 느낌이 든다.",
    "아침에 일어나도 피로가 풀리지 않는다.",
    "낮 시간에도 졸림이나 집중력 저하를 자주 느낀다.",
    "스트레스를 자주 느끼고 쉽게 해소되지 않는다.",
    "불안하거나 초조한 기분이 자주 든다.",
    "과민하거나 짜증이 많아진 느낌이 든다.",
    "잠들기 전 걱정이 많아 잠을 방해한다.",
    "수면 시간은 충분한데도 개운하지 않다.",
    "스트레스로 인해 소화 장애나 두통을 경험한 적 있다."
]

# 제목
st.title("😴 수면/스트레스 설문")
st.write("최근의 수면 질과 스트레스 상태를 확인해보세요.")
st.markdown("👉 **1 = 아니다, 5 = 그렇다**")

scores = []
with st.form("stress_survey"):
    for q in questions:
        score = st.slider(q, 1, 5, 3, format="%d")
        scores.append(score)
    submitted = st.form_submit_button("제출")

if submitted:
    total = sum(scores)
    st.subheader(f"📊 총점: {total}")

    if total >= 40:
        st.error("🌙 **심한 수면장애 및 스트레스**: 적극적인 개선이 필요합니다.")
        st.image("https://cdn.pixabay.com/photo/2018/04/20/20/57/supplement-3334792_1280.jpg", width=200)
        st.markdown("[GABA/테아닌 제품 보기](https://example.com/gaba-teanine)")
        st.image("https://cdn.pixabay.com/photo/2017/03/02/09/04/herbs-2117347_1280.jpg", width=200)
        st.markdown("[감태추출물 제품 보기](https://example.com/seaweed)")

    elif total >= 25:
        st.info("🌿 **가벼운 수면 문제**: 수면 보조 성분 복용을 고려해보세요.")
        st.image("https://cdn.pixabay.com/photo/2018/10/09/14/31/magnesium-3730144_1280.jpg", width=200)
        st.markdown("[마그네슘 제품 보기](https://example.com/magnesium)")
        st.image("https://cdn.pixabay.com/photo/2016/11/21/16/00/powder-1841128_1280.jpg", width=200)
        st.markdown("[글리신 제품 보기](https://example.com/glycine)")

    else:
        st.success("✅ **양호한 상태입니다**: 현재 상태를 잘 유지하세요.")
        st.image("https://cdn.pixabay.com/photo/2020/07/13/09/55/vitamins-5398768_1280.jpg", width=200)
        st.markdown("[비타민B군 종합비타민 보기](https://example.com/vitamin-b)")
def run():
    # 설문 코드 전체를 이 함수 안에 넣으면 됩니다.
    # 예시:
    import streamlit as st

    st.header("😴 수면/스트레스 설문")
    # 질문, 슬라이더, 제출 버튼 등
