# coding=utf-8


import colorama
import string
import time
from colorama import Fore, Back, Style
from colorama import init
from chinese import ChineseAnalyzer


class Nederlands:

    def woord_raden(self, x, y, z):

        woord = x.lower()
        woord_letters = set(woord)
        alfabet = set(string.ascii_lowercase)
        gebruikte_letters = set()

        init(autoreset = True)
    
        levens = y

        while levens > 0 and len(woord_letters) > 0:
            print(z)
            print("Je hebt nog", levens, "levens over en je hebt al deze letters gebruikt: ", " ".join(gebruikte_letters))

            woord_list = [letter if letter in gebruikte_letters else '-' for letter in woord]
            print("Het huidige woord: ", " ".join(woord_list))

            gebruiker_letter = input("Raad de letter: ").lower()
            if gebruiker_letter in alfabet - gebruikte_letters:
                gebruikte_letters.add(gebruiker_letter)
                if gebruiker_letter in woord_letters:
                    woord_letters.remove(gebruiker_letter)
                    print("")
            
                else:
                    levens = levens - 1 
                    print("\nJouw letter,", gebruiker_letter, "is niet in het woord 😕 .")

            elif gebruiker_letter in gebruikte_letters:
                print("\nJe hebt al de letter gebruikt. Probeer een andere letter te raden 🤔 .")

            else:
                print("\nDat is geen geldige letter 🤭 .")

        if levens == 0:
            print("Je hebt verloren 😧 ! Het woord was", Fore.CYAN + woord.upper())
        else:
            print("Hoeraaa 🎉! Je hebt het woord", Fore.CYAN + woord.upper(), "geraden! 😎")

        return Fore.CYAN + x

    def mad_libs(self):
        
        # The words.

        bij_naamwoord_1 = Fore.CYAN + input(" ☀️ Bijvoeglijk naamwoord (DE-woord): ").lower() + Fore.WHITE
        bij_naamwoord_2 = self.woord_raden("vrolijk", 7, " 😁 blij, opgewekt").lower() + Fore.WHITE
        bij_naamwoord_3 = Fore.CYAN + input(" 📦 Bijvoeglijk naamwoord (DE-woord): ").lower() + Fore.WHITE
        bij_naamwoord_4 = Fore.CYAN + input(" 👀 Bijvoeglijk naamwoord (meervoud): ").lower() + Fore.WHITE
        
        naamwoord_1 = self.woord_raden("woonwagen", 4, " 🚍 Grote wagen die als woning is ingericht.").lower() + Fore.WHITE
        naamwoord_2 = Fore.CYAN + input(" 🪥 Ding dat je in je handen kan houden: ").lower() + Fore.WHITE
        naamwoord_3 = self.woord_raden("pap", 6, "Meel, rijst e.d. gekookt in melk of water.").lower() + Fore.WHITE
        naamwoord_4 = Fore.CYAN + input("Lichaamsdeel 👃 🧠 🦷 👂 👅 🫁 👁 : ").lower() + Fore.WHITE

        plaats_1 = Fore.CYAN + input("Plaats (HET-woord): ").lower() + Fore.WHITE
        plaats_2 = Fore.CYAN + input("Plaats: ") + Fore.WHITE
        
        gevoel_1 = Fore.CYAN + input(" ☺️ Gevoel dat iemand heeft als hij iets fijn vindt: ").lower() + Fore.WHITE
        gevoel_2 = Fore.CYAN + input(" 😌 Gevoel dat iemand heeft als hij iets fijn vindt: ").lower() + Fore.WHITE
        gevoel_3 = self.woord_raden("Droevig", 5, " 😔 Treurig, Verdrietig") + Fore.WHITE
        
        kleur_1 = Fore.CYAN + input(" 🟫 Kleur: ").lower() + Fore.WHITE
        kleur_2 = Fore.CYAN + input(" 🟩 Kleur (meervoud): ").lower() + Fore.WHITE
        
        diertje_1 = Fore.CYAN + input(" 🐖 Diertje met een verkleiningsachtervoegsel (-je, -tje etc.): ").lower() + Fore.WHITE
        
        naam_1 = Fore.CYAN + input("Naam: ").capitalize() + Fore.WHITE
        naam_2 = Fore.CYAN + input("Naam: ").capitalize() + Fore.WHITE
        
        werkwoord_1 = Fore.CYAN + input(" 🧘‍♂️ Werkwoord: ").lower() + Fore.WHITE
        werkwoord_2 = self.woord_raden("optreden", 6, " 💃 In het openbaar spreken, musiceren, acteren enz.").lower() + Fore.WHITE
        
        print("\n\n")
        print(f"""Op een {bij_naamwoord_1} zomerdag zat clown {naam_1} op de trap van zijn {naamwoord_1}. Hij had een {naamwoord_2} in zijn hand en roerde ermee in het zand. Zijn gezicht was niet erg {bij_naamwoord_2}. Het leek wel of clown {naam_1} verdriet had.\n\nZachtjes mompelde hij: 'Wat ben ik toch eenzaam... Iedere avond maak ik de mensen in het {plaats_1} aan het lachen met mijn grappen, dan hebben ze allemaal plezier. En als het programma afgelopen is, gaan de mensen {gevoel_1} en {gevoel_2} naar {plaats_2}, terwijl ik dan weer in m'n eentje naar mijn {naamwoord_1} ga...' Hij zuchtte eens diep.\n\n{gevoel_3} staarde de clown naar de grond. Er rolde een traan over zijn clownsgezicht. Net toen {naam_1} besloot naar binnen te gaan, kwam een {kleur_1} {diertje_1} aanlopen. Het diertje kefte luid: 'Waaf...waaf... Het leek wel of het {naam_1} aandacht wilde trekken.\n\nClown {naam_1} schrok even van de druktemaker maar boog zich toen voorover om het {diertje_1} zachtjes over zijn {naamwoord_4} te aaien.\n\n'Daag {diertje_1}... Ik heet {naam_1}' zei hij vriendelijk. 'Hoe heet jij?' Natuurlijk kon het {diertje_1} niets terugzeggen, hij keek alleen maar met z'n grote {kleur_2} ogen naar de clown. \nHet dier snuffelde even aan de wagen en liep toen naar binnen. {naam_1} volgde en maakte snel iets te eten voor het {diertje_1}. Hij zettee een {bij_naamwoord_3} doos in een hoekje van z'n {naamwoord_1} en fluisterde: 'Zo, dit is je bedje. Je mag net zo lang bij mij {werkwoord_1} als je maar wilt...' Je zou denken dat het {diertje_1} de woorden van de clown begrepen had, want kwispelend met z'n korte staart liep hij parmantig naar de doos, waar {naam_1} een dekentje in gelegd had en sprong erin. Hij keek trouwhartig over de rand van de doos alsof hij {naam_1} bedanken wilde voor zijn gastvrijheid!\n{naam_1} liep naar zijn keukentje en maakte een bord {naamwoord_3} voor zichzelf klaar. 'Zo, nu ben ik niet meer alleen!' zei hij blij. Onder het eten keek hij af en toe verheugd naar de doos, waarin het {diertje_1} lag. Het was in slaap gevallen.\n{naam_1} glimlachte en mompelde in zichzelf: 'Ik noem hem {naam_2}, dat vind ik een leuke naam! En eh... ik neem hem mee op reis. Dan ben ik nooit meer alleen...'\nOmdat {naam_1} 's avonds weer voor alle grote en kleine mensen in het circus moest gaan {werkwoord_2}, ging hij na het eten ook een dutje doen. Hij trok z'n {bij_naamwoord_4} flapschoenen uit en dook snel in z'n bed. Voor hij z'n ogen dicht deed, keek hij nog even blij naar z'n nieuwe vriend {naam_2}.""")


class English:

    def guess_word(self, x, y, z):

        word = x.lower()
        word_letters = set(word)
        alphabeat = set(string.ascii_letters)
        used_letters = set()

        init(autoreset = True)
    
        lives = y

        while lives > 0 and len(word_letters) > 0:
            print(z)
            print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

            word_list = [letter if letter in used_letters else '-' for letter in word]
            print("Current word: ", " ".join(word_list))

            user_letter = input("Guess a letter: ").lower()
            if user_letter in alphabeat - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print("")
            
                else:
                    lives = lives - 1 
                    print("\nYour letter,", user_letter, "is not in the word 🤔 .")

            elif user_letter in used_letters:
                print("\nYou have already used that letter. Guess another letter 😊 .")

            else:
                print("\nThat is not a valid letter 🤭 .")

        if lives == 0:
            print("You lost 🥺 . The word was", Fore.GREEN + word.upper())
        else:
            print("Hoeray 🎉 ! You guessed the word", Fore.GREEN + word.upper(), "😎 !")

        return Fore.GREEN + x # returns the original value 

    def mad_libs(self):

        # The words.

        paris = self.guess_word("Paris", 3, " 🇫🇷 The capital of France, on the River Seine.") + Fore.WHITE
        amsterdam = self.guess_word("Amsterdam", 2, " 🇳🇱 The capital and largest city of the Netherlands. It is built on some ninety islands separated by canals.") + Fore.WHITE
        istanbul = self.guess_word("Istanbul", 3, " 🇹🇷 A port in Turkey on the Bosporus, lying partly in Europe, partly in Asia.") + Fore.WHITE
        cinnamon = self.guess_word("cinnamon", 5, "An aromatic spice made from the peeled, dried, and rolled bark of a SE Asian tree.") + Fore.WHITE
        wonderful = self.guess_word("wonderful", 5, " ✨ Inspiring delight, pleasure, or admiration; extremely good; marvellous.") + Fore.WHITE
        
        drink = Fore.GREEN + input(" ☕️ Drink：").lower() + Fore.WHITE
        vehicle = Fore.GREEN + input(" 🚄 Vehicle：").lower() + Fore.WHITE
        adj_1 = Fore.GREEN + input("Adjective：").lower() + Fore.WHITE
        place = Fore.GREEN + input("Place：") + Fore.WHITE
        flower = Fore.GREEN + input(" 🌹 Flower (plural)：").lower() + Fore.WHITE
        adj_2 = Fore.GREEN + input("Adjective：").lower() + Fore.WHITE
        
        print("\n\n")
        print(f"""{paris} was as {wonderful} as I hoped it would be - sunny, relaxed, lively, full of good food and wine. For a week, I just walked till my feet hurt. And when I was tired, I sat with a {drink} in the sun, until I was ready to work again. Really... is not a good city for walking. This is because zebra crossing count for nothing!\n\n Along its canals {amsterdam} is a very {adj_1} city. And I wanted to find out what it was like to live in one of the thousands of colourful houseboats. I arrived by {vehicle} at the {adj_2} Central Station, I rented a bike and made my way to the {place}.\n\n {istanbul} is one of those exciting, busy cities where everything is possible. I have never seen so much activity and heard such loud music coming from every door. On my first day there, I made my way to the Grand Bazaar which is full of exotic smells of {flower}, honey, leather and {cinnamon}.""")


class 中文:

    def 单词_猜猜(self, x, y, z):
        
        中文_元音 = {'ā', 'ē', 'ī', 'ō', 'ū', 'á', 'é', 'í', 'ó', 'ú', 'ǎ', 'ě', 'ǐ', 'ǒ', 'ǔ', 'à', 'è', 'ì', 'ò', 'ù'}
        字母 = {'d', 'b', 'z', 'g', 'u', 'f', 'r', 'v', 'q', 'k', 'o', 'x', 'n', 'w', 'l', 'i', 'm', 'p', 't', 'j', 's', 'h', 'e', 'a', 'c', 'y'}
        字母.update(中文_元音) # combining Chinese vowels with English letters.
        
        init(autoreset = True) # automatically back to default color again.

        analyzer = ChineseAnalyzer()
        单词 = x # the hieroglyph.
        result = analyzer.parse(x)
        单词 = result.pinyin().lower() # converts the hieroglyph to pinyin.

        单词_字母 = set(单词) # letters the pinyin hieroglyph.
        用过的_字母 = set() # what the user has guessed.
    
        生命 = y # number of lives.

        while 生命 > 0 and len(单词_字母) > 0:
        
            print(z) # word meaning.
            print("你还剩下", 生命, "条生命，你用了所有这些字母: ", " ".join(用过的_字母))

            单词_列表 = [字母 if 字母 in 用过的_字母 else '-' for 字母 in 单词]
            print("当前的单词: ", " ".join(单词_列表))

            用户_字母 = input("猜猜这个单词: ").lower()
            if 用户_字母 in 字母 - 用过的_字母:
                用过的_字母.add(用户_字母)
                if 用户_字母 in 单词_字母:
                    单词_字母.remove(用户_字母)
                    print("")
            
                else:
                    生命 = 生命 - 1 
                    print("\n你的字母,", 用户_字母, "不在单词里 😧 。")

            elif 用户_字母 in 用过的_字母:
                print("\n你已经用过这个字母了 👀 。试着猜猜另一个字母。")

            else:
                print("\n那不是一个有效的字母 🙄 。")

        if 生命 == 0:
            print("你输了 🥺 ！这个词是", Fore.YELLOW + result.original(), result.pinyin())
            print("\n\n")
        else:
            print("厉害啦 🎉 ! 你猜对了这个词", Fore.YELLOW + result.original(), result.pinyin())
            print("\n\n") 

        return Fore.YELLOW + result.original()

    def mad_libs(self):

        # The words.

        男生的名字 = Fore.YELLOW + input(" 🧑  男生的名字：") + Fore.WHITE
        身体的部分 = Fore.YELLOW + input(" 👃 🧠 🦷 👂 👅 🫁  👁  身体的部分：") + Fore.WHITE 
        中国食物1 = Fore.YELLOW + input(" 🥘  中国食物：") + Fore.WHITE 
        中国食物2 = Fore.YELLOW + input(" 🥟  北菜：") + Fore.WHITE 
        中国食物3 = Fore.YELLOW + input(" 🍲  南菜：") + Fore.WHITE 
        外国人 = Fore.YELLOW + input(" 👤  外国人：") + Fore.WHITE 
        
        print("❗️ 现在下六题你打拼音包括词重音。例如，如果单词就是 “ 先生 ”，那你打 ” xiānsheng “。 ❗️ 每次你得到一个提示。")
        time.sleep(7)

        方便面 = self.单词_猜猜("方便面", 5, " 🍜  一种方便食品。烤制或油炸过的面条，配有佐料，用开水冲泡后就可食用。") + Fore.WHITE
        欧洲 = self.单词_猜猜("欧洲", 3, " 🇪🇺  欧罗巴洲的简称。") + Fore.WHITE
        台湾 = self.单词_猜猜("台湾", 5, " 🇹🇼  位于中国东海南部，隔台湾海峡与福建省相望。") + Fore.WHITE
        先生 = self.单词_猜猜("先生", 5, " 👨‍🦰  对年龄比自己大的有学问有声望的人的敬称。") + Fore.WHITE 
        性情 = self.单词_猜猜("性情", 5, " 👤  秉性和气质。") + Fore.WHITE 
        国籍 = self.单词_猜猜("国籍", 4, " 🌐  指一个人具有的属于某个国家的公民的法律资格。") + Fore.WHITE 
        
        动词1 = Fore.YELLOW + input(" 🏃‍♂️  动词：") + Fore.WHITE 
        动词2 = Fore.YELLOW + input(" 🤼  第二个动词：") + Fore.WHITE 
        数词 = Fore.YELLOW + input(" 🔢  数词：") + Fore.WHITE 
        语言 = Fore.YELLOW + input(" 🗣  语言：") + Fore.WHITE 
        国家 = Fore.YELLOW + input(" 🇺🇳  国家：") + Fore.WHITE 
        词1 = Fore.YELLOW + input(" 🈶  任何一个字：") + Fore.WHITE 
        词2 = Fore.YELLOW + input(" 🈷️  任何第二个字：") + Fore.WHITE 
        
        print("\n\n")
        print(f"""我的{先生}很可惜是一个{外国人}。这样来称呼自己的{先生}不免有排外的味道，但是因为语文和风俗在各国之间确有大不相同之处，我们的婚姻生活也实在有许多无法共通的地方。\n\n当切决定下嫁给{男生的名字}时，我明白的告诉他，我们不但{国籍}不相同，{身体的部分}也不相同，将来婚后可能会{动词1}甚至于{动词2}。他回答我：“我知道你{性情}不好，心地却是很好的，{动词1}{动词2}都可能发生，不过我们还是要结婚。” 于是我们认识了{数词}年之后终于结婚了。\n\n我不是妇女解放运动的支持者，但是我极不愿在婚后失去独立的人格和内心的自由自在化，所以我一再强调，婚后我还是“我行我素”，要不然不结婚。{男生的名字}当时对我说：” 我就是要你 '你行你素'，失去了你的个性和作风，我何必娶你呢！” 好，大丈夫的论调，我十分安慰。{男生的名字}做的太太，语文将就他。可怜的外国人，”{词1}” 和 ”{词2}” 这两个字教了他那么多遍，他还是分不清，我只有讲他的话，这件事总算放他一马了。（但是将来孩子来了，打死也要学{语言}，这点他相当赞成。）\n\n闲话不说，做家庭主妇，第一便是下厨房。我一向对做家事十分痛恨，但对煮菜却是十分有兴趣，几只洋葱，几片肉，一炒变出一个菜来，我很欣赏这种艺术。\n\n母亲在{台湾}，知道我婚后因为{男生的名字}工作的关系，要到大荒漠地区的{国家}去，十二分的心痛，但是因为钱是{男生的名字}赚，我只有跟了饭票走，毫无选择的余地。婚后开厨不久，我们吃的全部是西菜。后来家中航空包裹飞来接济，我收到大批{中国食物1}、{中国食物2}、{中国食物3}、{方便面}、猪肉干等珍贵食品，我乐得爱不释手，加上{欧洲}女友寄来罐头酱油，我的家庭 “中国饭店” 马上开张，可惜食客只有一个不付钱的。（后来上门来要吃的朋友可是排长龙啊！）""")
        

def play_again():
    if user_input == "nl":
        antwoord = input("Zou je nog een keertje willen spelen? (JA) of NEE): ").upper()
        if antwoord == "JA":
            antwoord = input("Misschien wil je dan nog proberen in het Engels? (JA) of (NEE)").upper()
            if antwoord == "JA":
                en = English()
                print(en.mad_libs())
            elif antwoord == "NEE":
                antwoord = input("Kan je waarschijnlijk Chinees spreken? (JA) of (NEE): ").upper()
                if antwoord == "JA":
                    cn = 中文()
                    print(cn.mad_libs())
                else: 
                    print("Ik hoop dat je dit leuk vond! Doei 👋")
                    print("\n\n")
            else:
                print("Ik hoop dat je dit leuk vond! Doei 👋")
                print("\n\n")
        else:
            print("Ik hoop dat je dit leuk vond! Doei 👋")
            print("\n\n")
            
    if user_input == "en":
        answer = input("Would you like to play one more time? (YES) or (NO): ").upper()
        if answer == "YES":
            answer = input("Cool！Maybe you want to play in another foreighn language. Do you know Chinese? (YES) or (NO): ").upper()
            if answer == "YES":
                cn = 中文()
                print(cn.mad_libs())
            elif answer == "NO":
                answer = input("Do you speak Dutch? (YES) or (NO): ").upper()
                if answer == "YES":
                    nl = Nederlands()
                    print(nl.mad_libs())
                else: 
                    print("I hope you found this funny! Bye 👋")
                    print("\n\n")
            else:
                print("I hope you found this funny! Bye 👋")
                print("\n\n")
        else:
            print("I hope you found this funny! Bye 👋")
            print("\n\n")

    if user_input == "cn":
        答案 = input("你想不想再玩儿一次吗 👁 👅 👁 ? (是) 还是 (不是) ： ") 
        if 答案 == "是":
            答案 = input("很好！那你可能想试一下其他的语言。你会说英语吗？（是）还是（不是）：")
            if 答案 == "是":
                en = English()
                print(en.mad_libs())
            elif 答案 == "不是":
                答案 = input("你会说荷兰语吗？（是）还是（不是）：")
                if 答案 == "是":
                    nl = Nederlands()
                    print(nl.mad_libs())
                else:
                    print("我希望你喜欢了这个游戏！再见 👋")
                    print("\n\n")
            else:
                print("我希望你喜欢了这个游戏！再见 👋")
                print("\n\n")
        else:
            print("我希望你喜欢了这个游戏！再见 👋")
            print("\n\n")
                
    
#### MAIN CODE ####


user_input = input("Which language would you like to play (NL, EN, CN): ")


if user_input == "nl":
    nl = Nederlands()
    nl.mad_libs()
    play_again()

if user_input == "en":
    en = English()
    en.mad_libs()
    play_again()

if user_input == "cn":
    cn = 中文()
    cn.mad_libs()
    play_again()