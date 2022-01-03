from design import *
from Apis import *
import threading, requests, os, ctypes
from termcolor import colored
from colorama import init
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
import re
init()
print(colored((f"{banner}"), 'red'))
active = requests.get('https://api.ipify.org/?format=json').json()
ip = active['ip']
scan = requests.get('https://pastebin.com/raw/miBm2ymP').text
try:
    by = re.search(f'{ip} "(.*?)"', scan).group(1)
except:
    pass
else:
    if ip in scan:
        print(colored('Welcome To Daylight Swap \nBy Rayan  Insta  @m1c1', cyan))
    else:
        print(f"{reda}{ip} This ip is not active")
        input()
        exit(0)
    imge = ['https://c.tenor.com/mD1iWcEHA6MAAAAC/anime-girl.gif',
     'https://c.tenor.com/ynltIl-WTboAAAAC/anime-sad.gif',
     'https://c.tenor.com/oaDTsvOKy20AAAAC/lightning-glitch.gif']
    print('\n')

    def writesomething(mark, color, text):
        print(f"""\r{qube} {colored(text=("{mark}"), color=("{color}"))} {qube2} {text} {colored(text='', color=white)}""", end='')


    class generate:

        def __init__(self, fuc):
            self.TARGET = fuc
            self.threads_list = []

        def Generate_threds(self, Attack):
            for i in range(Attack):
                threads = threading.Thread(target=(self.TARGET))
                threads.setDaemon(True)
                self.threads_list.append(threads)
            else:
                return self.threads_list

        def started(self):
            for threads_Attack in self.threads_list:
                threads_Attack.start()

        def joined(self):
            for thread_join in self.threads_list:
                thread_join.join()


    class swap:

        def __init__(self):
            self.attempt = 0
            self.Rate = 0
            self.user = None
            self.email = None
            writesomething('+', green, f"{blueq}session : ")
            self.session = input()
            self.get_info()
            print(colored((f"{banner}"), 'red'))
            print(colored('By Rayan  Insta  @m1c1', cyan))
            print('\n')
            writesomething('+', green, f"{blueq}Do You Want Checkblock For account [Y/N] : ")
            self.check_block()
            self.look = threading.Lock()
            writesomething('+', green, f"{blueq}Target : ")
            self.target = input()
            writesomething('+', green, f"{blueq}Do You Want Auto settings [Y/N] : ")
            self.settings = input()
            writesomething('+', green, f"{green}Do You Want print counter in consle [Y/N] : ")
            self.wright = input()
            if self.settings.lower() == 'y':
                ctypes.windll.user32.MessageBoxW(0, 'Are You Ready ?', 'Daylight Swap', 4096)
                threading.Thread(target=(self.PRINT)).start()
                th = generate(self.swap)
                th.Generate_threds(20)
                th.started()
                th.joined()
            else:
                writesomething('+', green, f"{blueq}Threads: ")
                self.threads = int(input())
                threading.Thread(target=(self.PRINT)).start()
                ctypes.windll.user32.MessageBoxW(0, 'Are You Ready ?', 'Daylight Swap', 4096)
                th = generate(self.swap)
                th.Generate_threds(self.threads)
                th.started()
                th.joined()

        def send(self):
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/881360737606443098/XJRGDx7U8X3oIe5n71t_m9HXoAOgP3GUEUOm4gBdhG_0DKicxGa6umCtdWLtto3OnvAK')
            embed = DiscordEmbed(title=f"Swapped @{self.target}\n\n`Swaped By Swapper {by}`", color=242424)
            embed.set_author(name='Daylight')
            embed.set_image(url=(f"{random.choice(imge)}"))
            embed.set_footer(text='Made By Rayan@m1c1')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()

        def PRINT(self):
            while True:
                if self.wright.lower() == 'y':
                    print(f"\rAttempt : {self.attempt:,} | Rate : {self.Rate:,}", end='')
                else:
                    os.system(f"title Attempt : {self.attempt:,} \\ Rate : {self.Rate:,}")

        def get_info(self):
            try:
                get = getProfileData(sessionid=(self.session))
                self.user = re.search('"username":"(.*?)",', get).group(1)
                self.email = re.search('"email":"(.*?)",', get).group(1)
                writesomething('+', green, f"{GREEN}Loged in to @{self.user}")
                input()
                clearConsle()
            except:
                writesomething('-', red, f"{reda} Bad session")
                input()

        def check_block(self):
            self.askbl = input()
            if self.askbl.lower() == 'y':
                Response = edit_profile(number='', target=(self.user + '.checkblock'), email=(self.email), sessionid=(self.session))
                if Response.__contains__('"status":"ok"'):
                    print(f"{qube} {colored(text='+', color=green)} {qube2}", colored(text=f"@{self.user} The account is working  ", color=green))
                else:
                    print(f"{qube} {colored(text='-', color=red)} {qube2}", colored(text=f"@{self.user} The account is blocked for spamming too many requests ", color=red))
                    writesomething('+', green, text='Do You Want Continue Swap [Y/N] :  ')
                    qus = input()
                    if qus.lower() == 'y':
                        return True
                        writesomething('-', red, text='Click Enter To Close')
                        input()
                        exit()
                    else:
                        pass

        def Api(self):
            edit = edit_profile(number='', target=(self.target), email=(self.email), sessionid=(self.session))
            set_user = set_username_without_proxy(target=(self.target), sessionid=(self.session))
            apis = [edit, set_user]
            return random.choice(apis)

        def swap(self):
            while True:
                Resp = self.Api()
                if Resp.__contains__('"status":"ok"'):
                    with self.look:
                        print(f"{qube} {colored(text='+', color=green)} {qube2}", colored(text=f"@{self.target} Successfly Swapped  ", color=yellow))
                        self.send()
                        ctypes.windll.user32.MessageBoxW(0, f"Successfly Swapped : @{self.target} ", 'Daylight Swap', 4096)
                        os._exit(0)
                elif Resp.__contains__("isn't"):
                    self.attempt += 1
                else:
                    self.Rate += 1


    swap()
# okay decompiling light.pyc