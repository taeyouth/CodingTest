#### 고양이와 개는 몇마리 있을까
~~~MYSQL
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE;
~~~
고양이가 먼저 조회되도록 해야해서 order by를 붙였다.

#### 동명 동물 수 찾기
~~~MYSQL
SELECT NAME, COUNT(NAME) AS cnt FROM ANIMAL_INS 
GROUP BY NAME HAVING cnt>=2 ORDER BY NAME ;
~~~
WHERE절로 GROUP BY 앞에 cnt>=2 조건을 붙여봤지만 실행되지 않았음. 이유는 추후 알아봐야 

