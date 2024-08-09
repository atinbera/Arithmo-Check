import streamlit as st
from PIL import Image
from collections import Counter
import random 

st.title("Welcome to Arithmo Check")

img=Image.open("image/math1.jpg")
st.image(img)


st.text("""
    Arithmo Check is web application, where you can test your relation with mathematics,
    just answering few question's ans.
""")

# Assuming quiz1 is a multiple-choice question
quiz_mapping = {
    'Strongly Agree': 1,
    'Moderately Agree': 2,
    'Moderately Disagree': 3,
    'Strongly Disagree': 4,
    'Not yet decided': 5
}

quiz_options = list(quiz_mapping.keys())

# Section 1: Teacher and Learning Environment
st.header("Teacher and Learning Environment")
quiz1_answer = quiz_mapping[st.radio("**Do you feel that unavailability of a good Math teacher is a reason behind your fear of math?**", quiz_options, key="quiz1")]
st.markdown("<br>", unsafe_allow_html=True)
quiz2_answer = quiz_mapping[st.radio("**Do you get frustrated or frightened when you fail to solve problems repeatedly?**", quiz_options, key="quiz2")]
st.markdown("<br>", unsafe_allow_html=True)
quiz3_answer = quiz_mapping[st.radio("**Do you feel rote learning of mathematics increase Math phobia?**", quiz_options, key="quiz3")]

# Section 2: Psychological Factors
st.header("Psychological Factors")
quiz4_answer = quiz_mapping[st.radio("**Do you have Dyscalculia?**", quiz_options, key="quiz4")]
st.markdown("<br>", unsafe_allow_html=True)
quiz5_answer = quiz_mapping[st.radio("**Do you think psychological disorder is one of the reasons behind Math phobia?**", quiz_options, key="quiz5")]
st.markdown("<br>", unsafe_allow_html=True)
quiz6_answer = quiz_mapping[st.radio("**Do you think lack of concentration is one of the reasons behind your fear of math?**", quiz_options, key="quiz6")]

# Section 3: Conceptual Understanding
st.header("Conceptual Understanding")
quiz7_answer = quiz_mapping[st.radio("**Do you think unclear concepts of the topics are the reasons behind Math phobia?**", quiz_options, key="quiz7")]
st.markdown("<br>", unsafe_allow_html=True)
quiz8_answer = quiz_mapping[st.radio("**Do you think Yoga can solve the Math phobia?**", quiz_options, key="quiz8")]
st.markdown("<br>", unsafe_allow_html=True)
quiz9_answer = quiz_mapping[st.radio("**Do you think Math phobia is caused due to the pressure of performing well?**", quiz_options, key="quiz9")]

# Section 4: Practice and Real-World Connection
st.header("Practice and Real-World Connection")
quiz10_answer = quiz_mapping[st.radio("**Do you feel Mathematics phobia arises because you are not able to connect Mathematics with the real world?**", quiz_options, key="quiz10")]
st.markdown("<br>", unsafe_allow_html=True)
quiz11_answer = quiz_mapping[st.radio("**Do you agree that regular practice of Mathematics can solve the problems related to Math phobia?**", quiz_options, key="quiz11")]
st.markdown("<br>", unsafe_allow_html=True)
quiz12_answer = quiz_mapping[st.radio("**Do you think Math phobia is caused due to the pressure of performing well?**", quiz_options, key="quiz12")]

# Section 5: Problem-Solving Techniques
st.header("Problem-Solving Techniques")
quiz13_answer = quiz_mapping[st.radio("**Does breaking up a complicated problem into smaller part help in betterment?**", quiz_options, key="quiz13")]
st.markdown("<br>", unsafe_allow_html=True)
quiz14_answer = quiz_mapping[st.radio("**Does studying in peer groups and seeking help from teacher help to eradicate Math phobia?**", quiz_options, key="quiz14")]
st.markdown("<br>", unsafe_allow_html=True)
quiz15_answer = quiz_mapping[st.radio("**Does frequent mock tests help to release the pressure?**", quiz_options, key="quiz15")]

# Define the mapping from options to integers
answers = [
    quiz1_answer, quiz2_answer, quiz3_answer, quiz4_answer, quiz5_answer,
    quiz6_answer, quiz7_answer, quiz8_answer, quiz9_answer, quiz10_answer,
    quiz11_answer, quiz12_answer, quiz13_answer, quiz14_answer, quiz15_answer
]

a = answers.count(1) + answers.count(2)
b = answers.count(4) + answers.count(5)
c=answers.count(3)
flag = 0

if st.button('Submit',key='button'):
    flag = 1
    st.write('Thank you for your submission!')

st.write("""__________________________________________________________________________________________________________________________\
         ____________________________________________________________________________________________________________________________""")

# print(sorted_ans)
if flag==1:
    st.markdown("## Result:")
    if b>a or b>12:
        st.image(Image.open("image/bad.png"),width=200)
        st.error("It looks like you're struggling with Mathematics. Don't give up, keep practicing!") 
    elif a == b or c>8:
        st.image(Image.open("image/moderate.png"),width=200)
        st.info("You're doing okay, but there's room for improvement. Keep practicing!")
    else:
        st.image(Image.open("image/good.png"),width=200)
        st.success("Great job! You're excelling in Mathematics. Keep up the good work!")

    def determine_level(a, b, c):
        if a==15:
            return 10
        elif a>=12 & a<15:
            return random.randint(7,10)
        elif b>=12 and b<15 or a>=8 & a<12 or c>=7:
            return random.randint(4,8)
        elif b>=4 & b<8:
            return random.randint(2,5)
        elif b>12:
            return random.randint(1,3)
        
    level = determine_level(a, b, c)
    st.slider("Your level", 1, 10, level) 
st.write("""____________________________________________________________________________________________""")
# Footer
footer = """
<style>
footer {
    position: fixed;
    bottom: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    background-color: #f1f1f1;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    color: #333;
}
</style>
<div class="footer">
    <p>© 2024 Alphabet. All rights reserved.</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)