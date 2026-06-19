tournament_data = [
    ("An", "10", "2", "8"),
    ("Bình", "15", "0", "10"),
    ("Chi", "12", "ba", "5"),
    ("Dũng", "8", "1", "12")
]
def calculate_kda(kills, deaths, assists):
    int_kills = int(kills)
    int_deaths = int(deaths)
    int_assists = int(assists)
    
    if int_deaths == 0:
        raise ZeroDivisionError
        
    kda_value = (int_kills + int_assists) / int_deaths
    return round(kda_value, 2)

def display_tournament_kda(player_list):
    print("--- BẢNG XẾP HẠNG KDA ---")
    print(f"{'Tuyển thủ':<15} | {'KDA':<15} | Trạng thái / Kết quả")
    print("-" * 60)
    
    for player in player_list:
        player_name = player[0]
        kills = player[1]
        deaths = player[2]
        assists = player[3]
        
        try:
            kda = calculate_kda(kills, deaths, assists)
            print(f"{player_name:<15} | {kda:<15} | Thành công")
            
        except ZeroDivisionError:
            print(f"{player_name:<15} | {'Perfect':<15} | [Perfect Game] Không bị hạ gục lần nào!")
            continue
            
        except ValueError:
            print(f"{player_name:<15} | {'Lỗi':<15} | [ValueError] Lỗi dữ liệu không hợp lệ từ API!")
            continue

display_tournament_kda(tournament_data)