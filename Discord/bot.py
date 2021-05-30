import random
import re
import csv
import discord
from discord.ext import commands

app = commands.Bot(command_prefix='!')

# embed
# embed = discord.Embed(title='This is Embed', description='This is description of Embed', color = 0x00ff00)
# embed.add_field(name='This is feild 1',value='This is Value of Field 1', inline=True)
# embed.set_image(url='url')
# embed.set_thumbnail(url='url')
# embed.set_footer(text='footer text', image_url='this is option')

def problem_list_class1(num):
    class1 = []
    with open('class1.csv', 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        for idx, line in enumerate(rdr):
            class1.append(line[0])

    # random.shuffle(class1)
    result = []
    for s in class1:
        temp = re.compile(r"(\t|ESSENTIAL|STANDARD?)").split(s.rstrip())
        if 'ESSENTIAL' in temp:
            result.append([temp[0], temp[2]])

    return result[num], len(result)
def problem_list_class2(num):
    class1 = []
    with open('class2.csv', 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        for idx, line in enumerate(rdr):
            class1.append(line[0])

    # random.shuffle(class1)
    result = []
    for s in class1:
        temp = re.compile(r"(\t|ESSENTIAL|STANDARD?)").split(s.rstrip())
        if 'ESSENTIAL' in temp:
            result.append([temp[0], temp[2]])

    return result[num], len(result)
def problem_list_class3(num):
    class1 = []
    with open('class3.csv', 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        for idx, line in enumerate(rdr):
            class1.append(line[0])

    # random.shuffle(class1)
    result = []
    for s in class1:
        temp = re.compile(r"(\t|ESSENTIAL|STANDARD?)").split(s.rstrip())
        if 'ESSENTIAL' in temp:
            result.append([temp[0], temp[2]])

    return result[num], len(result)
def problem_list_class4(num):
    class1 = []
    with open('class4.csv', 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        for idx, line in enumerate(rdr):
            class1.append(line[0])

    # random.shuffle(class1)
    result = []
    for s in class1:
        temp = re.compile(r"(\t|ESSENTIAL|STANDARD?)").split(s.rstrip())
        if 'ESSENTIAL' in temp:
            result.append([temp[0], temp[2]])

    return result[num], len(result)
def problem_list_class5(num):
    class1 = []
    with open('class5.csv', 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        for idx, line in enumerate(rdr):
            class1.append(line[0])

    # random.shuffle(class1)
    result = []
    for s in class1:
        temp = re.compile(r"(\t|ESSENTIAL|STANDARD?)").split(s.rstrip())
        if 'ESSENTIAL' in temp:
            result.append([temp[0], temp[2]])

    return result[num], len(result)
def problem_list_class6(num):
    class1 = []
    with open('class6.csv', 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        for idx, line in enumerate(rdr):
            class1.append(line[0])

    # random.shuffle(class1)
    result = []
    for s in class1:
        temp = re.compile(r"(\t|ESSENTIAL|STANDARD?)").split(s.rstrip())
        if 'ESSENTIAL' in temp:
            result.append([temp[0], temp[2]])

    return result[num], len(result)

@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def 어려워(ctx):
    await ctx.send('👉 https://codeup.kr/problemsetsol.php?psid=33')

@app.command() # !rithm을 하고 아무런 메세지를 전달하지 않으면 에러 -> Null처리
async def RITHM(ctx, *, text = None):
    if(text != None):
        await ctx.send(text)
    await ctx.send('✊✊✊화이팅✊✊✊')
@app.command() # !rithm을 하고 아무런 메세지를 전달하지 않으면 에러 -> Null처리
async def Rithm(ctx, *, text = None):
    if(text != None):
        await ctx.send(text)
    await ctx.send('✊✊화이팅✊✊')
@app.command()  # !rithm을 하고 아무런 메세지를 전달하지 않으면 에러 -> Null처리
async def rithm(ctx, *, text=None):
    if (text != None):
        await ctx.send(text)
    await ctx.send('✊화이팅✊')

@app.command()
async def 오늘의(ctx, *text):
    level = text[0]
    num1 = int(text[1])
    try:
        num2 = int(text[2])
    except:
        pass
    if level == '기초':
        problem1, l1 = problem_list_class1(num1)
        problem2, l2 = problem_list_class1(num2)
        answer = f"✏오늘의 문제✏\n\n{problem1[0]}\n\t📚 문제 : {problem1[1]}\n{problem2[0]}\n\t📚 문제 : {problem2[1]}\n\n" \
                 f"{l1-num2}개의 문제가 남았습니다!"
        await ctx.send(answer)
    elif level == '레벨2':
        problem1, l1 = problem_list_class2(num1)
        problem2, l2 = problem_list_class2(num2)
        answer = f"✏오늘의 문제✏\n\n{problem1[0]}\n\t📚 문제 : {problem1[1]}\n{problem2[0]}\n\t📚 문제 : {problem2[1]}\n\n" \
                 f"{l1-num2}개의 문제가 남았습니다!"
        await ctx.send(answer)
    elif level == '레벨3':
        problem1, l1 = problem_list_class3(num1)
        problem2, l2 = problem_list_class3(num2)
        answer = f"✏오늘의 문제✏\n\n{problem1[0]}\n\t📚 문제 : {problem1[1]}\n{problem2[0]}\n\t📚 문제 : {problem2[1]}\n\n" \
                 f"{l1-num2}개의 문제가 남았습니다!"
        await ctx.send(answer)
    elif level == '레벨4':
        problem1, l1 = problem_list_class4(num1)
        # problem2, l2 = problem_list_class4(num2)
        answer = f"✏오늘의 문제✏\n\n{problem1[0]}\n\t📚 문제 : {problem1[1]}\n\n{l1-num1}개의 문제가 남았습니다!"
                 # f"{problem2[0]}\n\t📚 문제 : {problem2[1]}\n\n" \
                 # f"{l1-num2}개의 문제가 남았습니다!"
        await ctx.send(answer)
    elif level == '레벨5':
        problem1, l1 = problem_list_class4(num1)
        answer = f"✏오늘의 문제✏\n\n{problem1[0]}\n\t📚 문제 : {problem1[1]}\n\n{l1-num1}개의 문제가 남았습니다!"
        await ctx.send(answer)
    elif level == '레벨6':
        problem1, l1 = problem_list_class4(num1)
        answer = f"✏오늘의 문제✏\n\n{problem1[0]}\n\t📚 문제 : {problem1[1]}\n\n{l1-num1}개의 문제가 남았습니다!"
        await ctx.send(answer)

# @app.command()
# async def today(ctx, *, text):
#     await ctx.send(text)
# @app.command()
# async def 따라하기2(ctx, text):
#     await ctx.send(text)
# @app.command()
# async def 따라하기3(ctx, *text):
#     txt = ''
#     for tmp in text:
#         txt += tmp
#         txt += ', '
#     await ctx.send(txt[:-2])


app.run('ODQ4MjEyODA2NzA3OTcwMDc5.YLJVvA.4QZEPjXYfaOpV9GkZG9FKlhDmOk')