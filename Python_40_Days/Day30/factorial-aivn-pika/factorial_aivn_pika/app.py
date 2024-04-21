import streamlit as st
from factorial_aivn_pika.factorial import fact

def main():
    st.title('Factorial Calculator')
    number = st.number_input('Enter a number:', min_value=0, max_value=900)
    if st.button('Calculate'):
        res = fact(number)
        st.write(f'The factorial of {number} is {res}')
        st.balloons()

if __name__ == '__main__':
    main()