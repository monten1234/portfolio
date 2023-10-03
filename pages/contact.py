import streamlit as st

def contact():
    st.markdown("")
    st.markdown("""
            <div style="background-color: #eeeeee; padding: 10px; border-radius: 5px; font-size: 16px;">
                メールアドレス：
            </div>
            """,unsafe_allow_html=True)
    st.write("")
    st.markdown("""
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 40px;">   sample@email.com</p>
                """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

def main():
    st.title("連絡先")
    contact()
    

if __name__ == '__main__':
    main()
