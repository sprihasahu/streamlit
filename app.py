import streamlit as st
st.title('my home page')
st.header('i am header')
st.markdown('**STREAMLIT IS AMAZING**')
st.markdown('# heading1')
st.markdown('## heading2')
st.markdown('### heading3')
st.markdown('#### heading4')
st.markdown('##### heading5')
st.markdown('###### heading6')
st.code(
    '''
    a=1
    b=2
    c=a+b
    print("sum:",c)
    print("hello world")
    ''', language='python'
)
st.text('I am Spriha', help='https://github.com/sprihasahu')
t1