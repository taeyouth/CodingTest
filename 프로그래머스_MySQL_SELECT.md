#### 모든 레코드 조회하기
~~~MYSQL
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_INS.ANIMAL_ID ;
~~~
컬럼명 앞에 테이블명 안붙여도 될듯하다.

#### 역순 조회하기
~~~MYSQL
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;
~~~

#### 아픈 동물 조회하기
~~~MYSQL
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = 'SICK';
~~~

#### 젊은 동물 조회하기
~~~MYSQL
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged';
~~~

#### 동물의 아이디와 이름
~~~MYSQL
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID ;
~~~

#### 여러 기준으로 정렬하기
~~~MYSQL
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME ASC, DATETIME DESC;
~~~


#### 상위 N개 조회하기
~~~MYSQL
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1;
~~~
