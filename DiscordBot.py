#run.py
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #봇이 실행되면 콘솔창에 표시

@client.event
async def on_message(message):
    if message.author == client.user: # 봇 자신이 보내는 메세지는 무시
        return

    if message.content.startswith('$멍'): # 만약 $hello로 시작하는 채팅이 올라오면
        await message.channel.send('한때는 배리나를 품고\n'
                                   '한때는 김틀딱을 품었다가\n'
                                   '문재앙과 민주당을 품은 역적이다') # Hello!라고 보내기
    if message.content.startswith('$뚜썸'):
        await message.channel.send('존잘러')
    if message.content.startswith('$복실'):
        await message.channel.send('알코올중독말기 30under \n 똥차수집기&폐급페티쉬 \n 태릉이놓친 인재 \n 복실하다 [동사] \n '
                                   '뜻 : 복실-하다 (飮酒하다 [음ː주하다]) \n 나는 내일이없는것처럼 복실하다 간이 망가졌다.')
    if message.content.startswith('$조용희'):
        await message.channel.send('前) 격포홍보대사 \n 前) 격포해녀문화보존회장 \n 前) 격포청년회장 \n 前) 육군보병학교 박격포교관 '
                                   '\n 現) 대전 마라탕협회장 \n 現) 석춘식팬클럽회장 \n 現) 오픈톡 공식NPC \n 現) 사이버망령 쪼스비')
    if message.content.startswith('$엘무'):
        await message.channel.send('엘무!신조! \n'
                                   '우리는 음주와 흡연에 충성을 다하는 대한민국 술꾼이다!\n'
                                   '하나! 우리는 음주민주주의를 수호하며 주류통일에 역군이된다.\n\n'
                                   '둘! 우리는 실전과같은 음주로 멸망전의 승리자가된다!\n\n'
                                   '셋! 우리는 주도를 준수하고 술집의 명령에 절대복종한다!\n\n'
                                   '넷! 우리는 소주와 맥주를지키며 음주애로 굳게 단결한다!')
    if message.content.startswith('$민초'):
        await message.channel.send('종필이꺼')
    if message.content.startswith('$종필'):
        await message.channel.send('민초꺼')
    if message.content.startswith('$시연'):
        await message.channel.send('뚜썸이꺼')
    if message.content.startswith('$딩동'):
        await message.channel.send('브루애미')

client.run('mytoken') #토큰
