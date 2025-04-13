import requests
import json
import time
import random
import pyfiglet
from colorama import Fore, Style

Ab = '\033[1;92m'
aB = '\033[1;91m'
AB = '\033[1;96m'
aBbs = '\033[1;93m'
AbBs = '\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'

ab = pyfiglet.figlet_format("Digital Miners")
print(a_bSa + ab)
print(Fore.GREEN + " ⛏️ RED COIN BOT SCRIPT ⛏️ ")
print(Fore.RED + f" 📢 TELEGRAM GROUP: {Fore.GREEN}@DigitalMiners777")
print(Fore.YELLOW + " 👨‍💻 DEVELOPED BY: @Anaik7777 ")
print(f"{Fore.WHITE}═" * 60)
print(Fore.CYAN + " ✯ If You Have Any Issues, Please Visit Group And Discuss ✯")
print(f"{Fore.WHITE}═" * 60)

def send_graphql_request(query_id):
    url = "https://backend.red-coin.site/api/graphql"
    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'origin': 'https://red-coin.site',
        'referer': 'https://red-coin.site/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }

    payload = {
        "variables": {
            "initData": query_id,
            "friendCode": None
        },
        "query": """
        mutation ($initData: String, $friendCode: String) {
          initGame(initData: $initData, friendCode: $friendCode) {
            user {
              id
              telegram_id
              name
              token
            }
          }
        }
        """
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()
        if 'data' in data and 'initGame' in data['data'] and data['data']['initGame'] and 'user' in data['data']['initGame']:
            user_data = data['data']['initGame']['user']
            return user_data, user_data.get('token')
        else:
            print(Fore.RED + f" ⚠️ Error: Invalid GraphQL response for query ID: {query_id}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f" ❌ Request error for query ID {query_id}: {e}")
        return None, None
    except (KeyError, TypeError, json.JSONDecodeError) as e:
        print(Fore.RED + f" 💔 Error processing JSON response for query ID {query_id}: {e}")
        return None, None

def send_adsgram_request(telegram_id):
    url = f"https://backend.red-coin.site/api/adsgram?userId={telegram_id}&secret=6310"
    headers = {
        'accept': '*/*',
        'origin': 'https://red-coin.site',
        'referer': 'https://red-coin.site/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f" ❌ AdsGram request error for user {telegram_id}: {e}")
        return None
    except json.JSONDecodeError:
        print(Fore.RED + f" 💔 Error decoding AdsGram JSON response for user {telegram_id}")
        return None

def start_farming(token):
    url = "https://backend.red-coin.site/api/graphql"
    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'origin': 'https://red-coin.site',
        'referer': 'https://red-coin.site/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'token': token
    }
    payload = {
        "variables": {},
        "query": """
        mutation ($is_vtono_boost: Boolean, $ton_transaction_unique_boost: String) {
          startFarming(
            is_vtono_boost: $is_vtono_boost
            ton_transaction_unique_boost: $ton_transaction_unique_boost
          ) {
            unique
            wait_time
            end_timer
            earn_per_second
            current_balance {
              tonomo
              vTono
              __typename
            }
            __typename
          }
        }
        """
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f" ❌ Farming request error: {e}")
        return None
    except json.JSONDecodeError:
        print(Fore.RED + " 💔 Error decoding farming JSON response.")
        return None

def get_tasks():
    url = "https://backend.red-coin.site/api/graphql"
    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'origin': 'https://red-coin.site',
        'referer': 'https://red-coin.site/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }
    payload = {
        "operationName": "getTasks",
        "variables": {},
        "query": "mutation getTasks {\n  loadTasks {\n    tasks {\n      type\n      list {\n        id\n      }\n    }\n  }\n}"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        response_json = response.json()
        data = response_json.get('data', {}).get('loadTasks', {})
        task_ids = []
        for category in data.get('tasks', []):
            for task in category.get('list', []):
                task_ids.append(task.get('id'))
        for checkin_task in data.get('checkin', []):
            task_ids.append(checkin_task.get('id'))
        return task_ids
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f" ❌ Get tasks request error: {e}")
        return []
    except (KeyError, TypeError, AttributeError, json.JSONDecodeError):
        print(Fore.RED + " 💔 Error processing get tasks JSON response.")
        return []

def claim_task(telegram_id, task_id):
    url = "https://backend.red-coin.site/api/graphql"
    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'origin': 'https://red-coin.site',
        'referer': 'https://red-coin.site/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }
    payload = {
        "variables": {"tasks_id": task_id},
        "query": "mutation ($tasks_id: ID) {\n  claimTasks(tasks_id: $tasks_id) {\n    amount\n    tonomo\n  }\n}"
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f" ❌ Claim task request error for task {task_id}: {e}")
        return None
    except json.JSONDecodeError:
        print(Fore.RED + f" 💔 Error decoding claim task JSON response for task {task_id}")
        return None

if __name__ == "__main__":
    query_id = input(Fore.YELLOW + " 🔑 Enter your query ID: " + Fore.RESET).strip()
    if not query_id:
        print(Fore.RED + " ⚠️ Query ID cannot be empty.")
        exit()

    user_data, token = send_graphql_request(query_id)
    if user_data and token:
        telegram_id = user_data['telegram_id']
        name = user_data['name']
        print(Fore.GREEN + f" ✅ User: {name}, Telegram ID: {telegram_id}, Token: {token}")

        farming_response = start_farming(token)
        print(Fore.BLUE + " 🚜 Farming Response:", farming_response)

        tasks = get_tasks()
        print(Fore.MAGENTA + f" 📝 Found {len(tasks)} tasks.")
        for task_id in tasks:
            claim_response = claim_task(telegram_id, task_id)
            print(Fore.CYAN + f" 🎁 Claim Response for Task {task_id}:", claim_response)
            time.sleep(random.uniform(1, 3)) # Be polite

        print(Fore.YELLOW + " 📺 Watching Ads...")
        for i in range(10):
            print(Fore.YELLOW + f" ⏳ Attempting to watch ad {i+1}...")
            adsgram_response = send_adsgram_request(telegram_id)

            if adsgram_response and not adsgram_response.get("success", False):
                print(Fore.RED + " 🛑 Ads limit reached or error encountered. Stopping ad watching.")
                break

            print(Fore.GREEN + " ✅ AdsGram Response:", adsgram_response)
            time.sleep(random.uniform(5, 10)) # Be polite

        print(Fore.GREEN + " ✨ Script finished.")
    else:
        print(Fore.RED + f" ❌ Failed to initialize game with query ID: {query_id}")
