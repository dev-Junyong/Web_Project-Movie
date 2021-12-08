import requests
import json
with open("popular.json", "w", encoding="UTF8") as json_file:

    apikey = "5840e483e50b84b21ef125134cf65bc4"
    movie_list = range(1, 501)
    movie_list = list(map(str, movie_list))


    # api = "https://api.themoviedb.org/3/movie/{movies}?api_key={key}&language=ko-KR"
    popurlar = "https://api.themoviedb.org/3/movie/popular?api_key={key}&language=ko-KR&page={movies}"
    credit = "https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={key}&language=ko-KR"


    class Default(dict):

        def __missing__(self, key):
            return key

    ret = []
    for name in movie_list:
        try:
            url = popurlar.format_map(Default(movies=name, key=apikey))
            r = requests.get(url)
            data = json.loads(r.text)
            # print(data)

            for j in data["results"]:
                url2 = credit.format_map(Default(movie_id=j["id"], key=apikey))
                print(j["id"])
                c = requests.get(url2)
                c_data = json.loads(c.text)
                # print(c_data)
                cre = {"movie_id": j["id"]}
                cre["cast"] = c_data["cast"]
                cre["crew"] = c_data["crew"]
                ret.append(cre)
        except:
            print('pass')

    json.dump(ret, json_file, ensure_ascii=False)
