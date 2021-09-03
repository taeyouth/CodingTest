#### 루시와 엘라 찾기
~~~MYSQL
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle','Rogan','Sabrina','Mitty');
~~~


#### 이름에 EL 들어가는 강아지 찾기 (대소문자 구분 X)
~~~MYSQL
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS 
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'Dog' 
ORDER BY NAME;
~~~
LIKE는 대소문자를 구분하지 않는다
BINARY(NAME) LIKE '%el%' 로 쿼리 작성 시 구분한다

#### 중성화 여부 파악하기
~~~MYSQL
SELECT ANIMAL_ID, NAME, 
IF(SEX_UPON_INTAKE REGEXP ('Neutered|Spayed'),'O','X') AS '중성화' 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
~~~
여러 문자열을 검색하려면 LIKE IN과 같은 기능을 내는 REGEXP ('문자열1'|'문자열2'|'문자열3') 문법을 사용하면 된다

#### 오랜기간 보호한 동물(2)
~~~MYSQL
SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS AS INS LEFT JOIN ANIMAL_OUTS AS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY DATEDIFF(OUTS.DATETIME, INS.DATETIME) DESC LIMIT 2 ;
~~~
날짜끼리 차이를 계산할 때는 DATEDIFF 함수를 사용한다


#### DATETIME에서 DATE로 형 변환
~~~MYSQL
SELECT ANIMAL_ID, NAME, 
DATE_FORMAT(DATETIME,'%Y-%m-%d') 
FROM ANIMAL_INS ORDER BY ANIMAL_ID;
~~~
새삼 스럽지만 DATE_FORMAT()을 사용하면 날짜 데이터를 원하는 형태에 맞게 출력할 수 있다.
