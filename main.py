import streamlit as st
from PIL import Image, ImageOps, ImageDraw


def displayName():
    image = "name.png"  
    st.image(image, use_column_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)


def displayCarrer():
#     st.write('<span style="font-size: 16px;">経歴：</span>', unsafe_allow_html=True)
    st.markdown("""
            <div style="background-color: #eeeeee; padding: 10px; border-radius: 5px; font-size: 16px;">
                経歴：
            </div>
            """,unsafe_allow_html=True)
    st.write("")
    st.markdown("""
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 40px;">   大分出身</p>
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 40px;">   明治大学在学中</p>
                """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    
def displayExperience():
    st.markdown("""
            <div style="background-color: #eeeeee; padding: 10px; border-radius: 5px; font-size: 16px;">
                これまでの経験：
            </div>
            """,unsafe_allow_html=True)
    st.write("")
    st.markdown('<p style="font-family:serif; color:black; font-size: 22px; margin-left: 40px;">UI開発</p>', unsafe_allow_html=True)
    img = Image.open('createUI.jpg')  
    rounded_image = round_corners(img, 80)
    # 2つのカラムを作成
    col1, col2 = st.columns(2)

    # 1つ目のカラムに画像を表示
    col2.image(img, use_column_width=True)

    # 2つ目のカラムにテキストを表示
    col1.markdown("""
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 80px;">- SwiftUIを用いたフリマアプリ開発</p>
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 80px;">- UIKit(storyboard)を用いた出会い系アプリ開発</p>
                """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    
def displaySkills():
    st.markdown("""
            <div style="background-color: #eeeeee; padding: 10px; border-radius: 5px; font-size: 16px;">
                できること：
            </div>
            """,unsafe_allow_html=True)
    st.write("")
    st.markdown("""
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 40px;">アプリ側</p>
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 80px;">- 言語 Swift</p>
                """, unsafe_allow_html=True)
    st.markdown('<p style="font-family:serif; color:black; font-size: 22px; margin-left: 80px;">- フレームワーク: SwiftUI, UIKit</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:serif; color:black; font-size: 22px; margin-left: 80px;">- firebase</p>', unsafe_allow_html=True)
    st.markdown("""
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 40px;">各種ツール</p>
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 80px;">- Github</p>
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 80px;">- Figma</p>
                """, unsafe_allow_html=True)
    st.markdown("""
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 40px;">その他</p>
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 80px;">- Githubを使ったチーム開発経験</p>
                """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)


def displayLearning():
    st.markdown("""
            <div style="background-color: #eeeeee; padding: 10px; border-radius: 5px; font-size: 16px;">
                現在学んでいること：
            </div>
            """,unsafe_allow_html=True)
    st.write("")
    st.markdown("""
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 40px;">- Streamlit</p>
                <p style="font-family:serif; color:black; font-size: 22px; margin-left: 40px;">- supabase</p>
                """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)


def displayGoal():
    st.markdown("""
            <div style="background-color: #eeeeee; padding: 10px; border-radius: 5px; font-size: 16px;">
                今後学んでいきたいこと：
            </div>
            """,unsafe_allow_html=True)
    st.write("")
    st.markdown('<p style="font-family:serif; color:black; font-size: 22px; margin-left: 40px;">Next.jsを学んで、複雑なwebサイト開発ができるようになりたい。</p>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)


def round_corners(image, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', image.size, 255)
    w, h = image.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    image.putalpha(alpha)
    return image

def main():
    displayName()
    displayCarrer()
    displayExperience()
    displaySkills()
    displayLearning()
    displayGoal()
   
   
if __name__ == '__main__':
    main()
