import pandas as pd
from data_helpers import *
    
def add_data_to_list(df, data):
    for index, row in df.iterrows():
        data.append(DataObject().create(
            title=row['title'],
            year=row['year'],
            genre=row['genres'],
            plot=row['overview'],
            lang=row['language'], 
            poster=row['poster'],
            rating=row['rating'],
            trailor=row['trailer'],
            runtime = row['runtime'],
            budget = row['budget'],
            revenue = row['revenue'],
            director = row['directors'],
            director_img = row['director_images'],
            top_cast = row['top_cast'],
            top_cast_img = row['top_cast_images']
        ))
    return data

if __name__ == "__main__":
    
     # -------------------------
    # đọc dữ liệu từ file csv
    df = pd.read_csv('DataMovie_TMDB_MAIN.csv')
    
    # chia dữ liệu thành hai DataFrame tránh bị lỗi khi thêm vào danh sách quá nhiều dữ liệu
    df_1 = df[:5000]
    df_2 = df[5000:]
    
    # thêm dữ liệu vào danh sách data (list)
    data = []
    data = add_data_to_list(df_1, data)
    data = add_data_to_list(df_2, data)
    
    # hiển thị số lượng phim trong danh sách
    print(f'Total number of movies: {len(data)}')
    # -------------------------