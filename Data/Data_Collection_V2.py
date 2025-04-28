import requests   
import pandas as pd
import time

# Function to fetch data for a specific game (appdetails)
def fetch_game_data(app_id):
    url = f"https://steamspy.com/api.php?request=appdetails&appid={app_id}"
    response = requests.get(url)
    time.sleep(1)  # To avoid hitting rate limits

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for AppID {app_id}")
        return None

# Fetch top 100 games in the last two weeks
def fetch_top_100_games():
    url = "https://steamspy.com/api.php?request=top100in2weeks"
    response = requests.get(url)
    time.sleep(1)  # To avoid hitting rate limits

    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching top 100 games data.")
        return None

# Main function to fetch data for top 100 games and save to CSV
def save_top_100_game_data():
    top_100_data = fetch_top_100_games()

    if top_100_data:
        game_data_list = []

        # Iterate through each game in the top 100 data
        for app_id, game_info in top_100_data.items():
            game_data = fetch_game_data(app_id)
            if game_data:
                game_data_list.append({
                    'Game Name': game_info['name'],
                    'AppID': game_info['appid'],
                    'Owners': game_info.get('owners', 'N/A'),
                    'Players (2 Weeks)': game_info.get('average_2weeks', 'N/A'),
                    'Peak Players': game_info.get('ccu', 'N/A'),
                    'Average Playtime (Lifetime)': game_info.get('average_forever', 'N/A'),
                    'Average Playtime (2 Weeks)': game_info.get('average_2weeks', 'N/A'),
                    'Price': game_info.get('price', 'N/A'),
                    'Developer': game_info.get('developer', 'N/A'),
                    'Publisher': game_info.get('publisher', 'N/A'),
                    'Genres': ", ".join(game_info.get('genre', []))
                })

        # Save data to CSV
        df = pd.DataFrame(game_data_list)
        df.to_csv('top_100_games_with_playtime.csv', index=False)
        print("Data saved to top_100_games_with_playtime.csv")
    else:
        print("Failed to fetch top 100 games.")

# Run the script
save_top_100_game_data()
