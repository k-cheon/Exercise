import requests

# API를 호출하고 응답을 저장합니다
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# API 응답을 변수에 저장합니다
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 저장소 정보를 확인합니다
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 첫 번째 저장소를 확인합니다
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)

# 결과를 처리합니다
print(response_dict.keys())