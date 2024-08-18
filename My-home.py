import streamlit as st
from PIL import Image
page = st.sidebar.radio('Zhangjiayi15436`s Website  |  Zhangjiayi15436的网站',['说明', '我的自制工具','我的分享图片','闲聊区','我的推荐', '我的视频','词典'])
def page1():      
    '''我的自制工具'''
    st.write(':sunglasses:图片换色小工具:sunglasses:')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_type = uploaded_file.type
        file_name = uploaded_file.name
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色滤镜')
            co = st.toggle('增强对比度')
            bw = st.toggle('黑白滤镜')
        b = st.button('开始处理')
        #tab1, tab2, tab3, tab4 = st.tabs(['原图', '改色1', '改色2', '改色3'])
        #with tab1:
            #st.write('原图--------V')
            #st.image(img)
        #with tab2:
            #st.write('已处理--------V')
            #st.image(img_change(img, 0, 1, 2))
        #with tab3:
            #st.write('已处理--------V')
            #st.image(img_change(img, 1, 2, 0))
        #with tab4:
            #st.write('已处理--------V')
            #st.image(img_change(img, 1, 0, 2))
        if b:
            if ch:
                img = img_change(img, 0, 1, 2)
                st.image(img)
            if co:
                img_change_co(img)
                st.image(img)
            if bw:
                img = img_change_bw(img)
                st.image(img)
        

def page2():
    def image(aa, text):
        st.write(text + '--------------')
        st.image(aa)
        pass
    image_1 = 'image\minecraft_image.png'
    '''我的分享图片'''
    st.write('图片')
    st.write('---------------------->')
    image(image_1, '???')
    image('image\mc.png', '鬼畜的mc')
    
    pass

def page3():
    '''闲聊区'''
    st.write('闲聊区')
    with open('leave_message.txt', 'r', encoding='utf-8') as f:
        message_list = f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split('#')
    for i in message_list:
        if i[1] == 'zhangjiyi15436':
            with st.chat_message('😊'):
                st.write(i[1], ':', i[2])
        elif i[1] == '_gongmin':
            with st.chat_message('🎶'):
                st.write(i[1], ':', i[2])
    name = st.selectbox('我是.....', ['zhangjiayi15436', '_gongmin'])
    new_message = st.text_input('想要说的话.....')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1), name, new_message])
        with open('leave_message.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in message_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
            
    pass

def page4():
    '''我的推荐'''
    music = 'radio/bilibili.mp3'
    image = 'music_image/1212.png'
    st.write('我的音乐')
    st.write('---------------------->')
    def audio(mp3, text, type, image):
        with open(mp3, 'rb') as f:
            mymp3 = f.read()
        st.write(text + 'V--------------V')
        st.audio(mymp3, format = 'audio/'+type, start_time = 0)
        st.image(image)
        pass
    audio(music, '银行不妙曲', 'mp3', image)
    audio('radio/Государственный гимн СССР.mp3', 'Государственный гимн СССР[牢不可破的联盟]', 'mp3', 'music_image/cccp.png')
    audio('radio/月亮之上.mp3', '月亮之上[交响乐版]', 'mp3', 'music_image/yue.png')
    audio('radio/Positive Outlook.mp3', 'Positive Outlook[CMS(中国航天)发射专用曲]', 'mp3', 'music_image/cms.png')
    st.image('music_image/space.png')
    audio('radio/space_ender.mp3', '太空电梯[流浪地球2]', 'mp3', 'music_image/space1.png')
    st.image('music_image/space2.png')
    st.image('music_image/space3.png')
    st.write('我的电影推荐')
    st.write('---------------------->')
    st.write('我的游戏推荐')
    st.write('---------------------->')
    st.write('我的书籍')
    st.write('---------------------->')
    pass

def page5():
    st.write('我的视频')
    st.write('---------------------->')
    def video(mp4, text):
        with open(mp4, 'rb') as f:
            myvideo = f.read()
        st.write(text + '--------------V')
        st.video(myvideo, start_time = 0)
    video('video/j-10.mp4', '旱地拔葱？')
    video('video/chuan.mp4', '川普激情演唱')
    

def page0():
    st.write('<我的视频>板块目前无法使用')
    st.write('---------------------------------------')
    st.write('规则')
    st.write('阿八阿八阿八阿八阿八.....,不能蓄意攻击,明白？')
    st.write('---------------------------------------')
    st.write('想保存图片，手机是长按，在菜单中选择‘保存图片到本地’')
    st.write('电脑是右击，在菜单中选择‘将图像另存为’')
    st.write('保存音乐手机端进度条边上有保存按钮，电脑端在进度条右侧点击2个点，有保存选项')
    pass

def img_change(img, br, bg, bb):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][br]
            g = img_array[x, y][bg]
            b = img_array[x, y][bb]
            img_array[x, y] = (b, g, r)
    return img

def img_change1(img):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            img_array[x, y] = (g, b, r)
    return img

def img_change2(img):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            img_array[x, y] = (r, b, g)
    return img

def page1123():
    st.write('‘智慧’的词典')
    #>>>
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    #>>>
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    word = st.text_input('请输入要查询的单词:')
    #>>
    if word in words_dict:
        n2 = words_dict[word][0]
        n1 = words_dict[word][1]
        st.write('#'+str(n2)+'|'+n1)
        if n2 in times_dict:
            times_dict[n2] += 1
        else:
            times_dict[n2] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数:', times_dict[n2])
        #>>
        if word == 'snow' or word == 'winter':
            st.snow()
        if word == 'luck':
            st.write('Why are you luckier than me? F*** you!')
        if word == 'clown':
            st.balloons()
        if word == 'joker':
            st.balloons()
            st.image('image/joker.png')
    
    pass

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

if page=='说明':
    page0()
elif page== '我的自制工具':
    page1()
elif page== '我的分享图片':
    page2()
elif page== '闲聊区':
    page3()
elif page== '我的推荐':
    page4()
elif page== '我的视频':
    page5()
elif page=='词典':
    page1123()
