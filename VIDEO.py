from moviepy.editor import (
    TextClip,
    concatenate_videoclips,
    CompositeVideoClip,
    AudioFileClip,
    ImageClip,
    VideoFileClip,
)
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os


def make_image(num, message):
    # Image size
    W = 720
    H = 480
    bg_color = "rgb(0, 0, 0)"  # 아이소프트존

    # font setting
    font = ImageFont.truetype(
        "C:\\Users\\joohj\\AppData\\Local\\Microsoft\\Windows\\Fonts\\NanumSquareRoundB.ttf",
        25,
    )
    font_color = "rgb(255, 255, 255)"  # or just 'black'
    # 원래 윈도우에 설치된 폰트는 아래와 같이 사용 가능하나,
    # 아무리 해도 한글 폰트가 사용이 안 되어.. 같은 폴더에 다운받아 놓고 사용함.
    # font = ImageFont.truetype("arial.ttf", size=28)

    image = Image.new("RGB", (W, H), color=bg_color)
    draw = ImageDraw.Draw(image)

    # Text wraper to handle long text
    # 40자를 넘어갈 경우 여러 줄로 나눔
    lines = textwrap.wrap(message, width=40)

    # start position for text
    x_text = 50
    y_text = 50

    # 각 줄의 내용을 적음
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x_text, y_text), line, font=font, fill=font_color)
        y_text += height
        # height는 글씨의 높이로, 한 줄 적고 나서 height만큼 아래에 다음 줄을 적음

    # 안에 적은 내용을 파일 이름으로 저장
    # image.save("{}.png".format(message))
    image.save(path + f"images\\image{num}.png")


def add_static_image_to_audio(image_path, audio_path, output_path):
    audio_clip = AudioFileClip(audio_path)
    image_clip = ImageClip(image_path)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 1
    video_clip.write_videofile(output_path)


def make_tts(num, text):
    tts = gTTS(text, lang="ko")
    tts.save(path + f"tts\\tts{num}.mp3")


def DeleteAllFiles(filePath):
    for file in os.scandir(filePath):
        os.remove(file.path)


def combine_video_files(video_list):
    video_clips = []
    for video in video_list:
        video_clip = VideoFileClip(video)
        video_clips.append(video_clip)
    final_video_clip = concatenate_videoclips(video_clips)
    final_video_path = path + "result\\video.mp4"
    final_video_clip.write_videofile(final_video_path)


text = """여섯 살 적에 나는 "체험한 이야기"라는 제목의, 원시림에 관한 책에서 기막힌 그림 하나를 본 적이 있다. 맹수를 집어삼키고 있는 보아 구렁이 그림이었다. 위의 그림은 그것을 옮겨 그린 것이다.
 그 책에는 이렇게 씌어 있었다.
 "보아 구렁이는 먹이를 씹지도 않고 통째로 집어삼킨다.그리고는 꼼짝도 하지 못하고 여섯 달 동안 잠을 자면서 그것을 소화시킨다."
 나는 그래서 밀림 속에서의 모험에 대해 한참 생각해 보고 난 끝에 색연필을 가지고 내 나름대로 내 생애 첫번째 그림을 그려보았다. 나의 그림 제 1호였다. 그것은 이런 그림이었다.
 나는 그 걸작품을 어른들에게 보여 주면서내 그림이 무섭지 않느냐고 물었다.
 그들은 "모자가 뭐가 무섭다는 거니?" 하고 대답했다.
 내 그림은 모자를 그린 게 아니었다. 그것은 코끼리를 소화시키고 있는 보아 구렁이었다.
 그래서 나는 어른들이 알아볼 수 있도록 보아 구렁이의 속을 그렸다. 어른들은 언제나 설명을 해주어야만 한다. 나의 그림 제 2호는 이러했다.
 어른들은 속이 보이거나 보이지 않거나 하는 보아 구렁이의 그림들은 집어치우고 차라리 지리, 역사, 계산, 그리고 문법 쪽에 관심을 가져보는 게 좋을 것이라고 충고해 주었다.
 그래서 나는 여섯 살 적에 화가라는 멋진 직업을 포기해 버렸다.내 그림제 1호와 제 2호가 성공을 거두지 못한 데 낙심해 버렸던 것이다. 어른들은언제나 스스로는 아무것도 이해하지 못한다.자꾸자꾸 설명을 해주어야 하니 맥빠지는 노릇이 아닐 수 없다.
 그래서 다른 직업을 선택하지 않을 수 없게 된 나는 비행기 조종하는 법을배웠다.세계의 여기저기 거의 안 가본 데 없이 나는 날아다녔다.그러니지리는 정말로 많은 도움을 준 셈이었다.한번 슬쩍 보고도 중국과 애리조나를 나는 구별할 수 있었던 것이다.그것은 밤에 길을 잃었을 때 아주 유용한 일이다.
 나는 그리하여 일생 동안 수없이 많은 점잖은 사람들과수많은 접촉을 가져왔다.어른들 틈에서 많이 살아온 것이다.나는 가까이서 그들을 볼 수있었다. 그렇다고 해서 그들에 대한 내 생각이 나아진건 없었다.
 조금 총명해 보이는 사람을 만날 때면나는 늘 간직해 오고 있던 예의 나의 그림 제 1호를 가지고 그 사람을 시험해 보고는 했다. 그 사람이 정말로뭘 이해할 줄 아는 사람인가알고 싶었던 것이다.그러나 으례 그 사람은"모자군" 하고 대답하는 것이었다. 그러면 나는 보아 구렁이도 원시림도 별들도 그에게 이야기하지 않았다. 그가 이해할 수 있는 이야기를 했다. 브리지니 골프니 정치니 넥타이니 하는 것들에 대해 이야기하는 것이다.
 그러면 그 어른은 매우 착실한 청년을 알게 된 것을 몹시 기뻐했다.""".split(
    "\n"
)

path = "C:\\Users\\joohj\\OneDrive\\바탕 화면\\코드\\프로젝트\\동영상제작\\"
DeleteAllFiles(path + "tts")
DeleteAllFiles(path + "images")
DeleteAllFiles(path + "videos")

for i, j in enumerate(text):
    make_image(i, j)
    make_tts(i, j)


clips = []
for i, j in enumerate(text):
    add_static_image_to_audio(
        path + f"images\\image{i}.png",
        path + f"tts\\tts{i}.mp3",
        path + f"videos\\video{i}.mp4",
    )


video_list = [path + f"videos\\video{i}.mp4" for i in range(len(text))]
print(video_list)
combine_video_files(video_list)
# # 모든 클립을 연결합니다.
# final_clip = concatenate_videoclips(clips)

# # 동영상을 파일로 저장합니다. 이때 fps (프레임 속도)를 지정해야 합니다.
# final_clip.write_videofile("Movie.mp4", fps=24)
# clips[0].write_videofile("clip1.mp4", fps=24)
