"# SonTest"
"# SonTest"

github atom 연계 사용법

1. PC의 폴더를 정해서 github의 repositories https를 확인 후 remote 해줌

1-1 cmd에서 PC폴더로 이동 후
1-2 git config user.name Yurak-Son
1-3 git config user.email @naver.com
1-4 git remote add origin https://github.com/(name)/(repositories명).git
1-5 git remote -v
1-6 git pull --allow-unrelated-histories

2. Branch defalt 값은 main이고 같은 프로잭트에 작업자를 나눠서 작업할수있다.

3. --allow-unrelated-histories 프로잭트에 파일 차이가 많이나서 오류뜨는걸 막아줄수있다.
