from sqlalchemy import create_engine, text

db_connection_info = {
    'user': 'root',
    'password': 'asdf1234!',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'kusf3'
}


db_url = f"mysql+mysqlconnector://{db_connection_info['user']}:{db_connection_info['password']}@{db_connection_info['host']}:{db_connection_info['port']}/{db_connection_info['database']}?charset=utf8"
engine = create_engine(db_url, max_overflow=0)



#종목,지역,팀,날짜

def read_sports_gamedate(sports_type: str, date, place: str, team: str):

    if sports_type == "baseball":
        table_name = "baseball_game_date"

    elif sports_type == "soccer":
        table_name = "soccer_game_date"
    
    query_str = f'''
                select 
                    date,
                    time,
                    away_team,
                    home_team,
                    stadium,
                    group_count
                from {table_name} 
                where 1=1
                '''
    
    if place : 
        query_str += f" AND place = '{place}'"
        
    if date : 
        query_str += f" AND date = '{date}'"
    
    if team :
        query_str += f" AND (home_team = '{team}' OR away_team = '{team}')"
    
    with engine.connect() as conn:
        rows = conn.execute(text(query_str))
        
    columns = rows.keys()
    print(columns)
    
    row_dict_list = []
    for row in rows:
        row_dict = {column: str(row[idx]) for idx, column in enumerate(columns)}
        row_dict_list.append(row_dict)
    
    print(row_dict_list)
    return {
        "sports_game_date": row_dict_list        
    }

    
    
# join을 이용해 야구 경기별 그룹 데이터 리스트

def get_group_list_by_sports(date, cheer_team):
    query_str = '''
        SELECT 
            bgd2.baseball_game_ID,
            bgd2.`date` , bgd2.`time` ,
            bgd2.away_team, bgd2.home_team, bgd2.stadium,  
            bgd.group_name,
            bgd.group_leader,
            bgd.cheer_team,
            bgd.member_total ,
            bgd.member_num ,
            bgd.keyword1 ,bgd.keyword2 ,bgd.keyword3,
            bgd.group_create_date
        FROM baseball_group_data bgd
        JOIN baseball_game_date bgd2 ON bgd.baseball_game_ID = bgd2.baseball_game_ID
        WHERE 1=1
    '''
    if date: 
        query_str += f" AND `date` = '{date}'"
    
    if cheer_team:
        query_str += f" AND cheer_team = '{cheer_team}'"
    
    with engine.connect() as conn:
        rows = conn.execute(text(query_str))
        
    columns = rows.keys()
    print(columns)
    
    row_dict_list = []
    for row in rows:
        row_dict = {column: str(row[idx]) for idx, column in enumerate(columns)}
        row_dict_list.append(row_dict)
    
    print(row_dict_list)
    return {
        "bs_group_date": row_dict_list        
    }

