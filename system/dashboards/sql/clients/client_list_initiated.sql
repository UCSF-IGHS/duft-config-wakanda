SELECT client_id,gender, hiv_diagnosis_date,enrolment_date,first_art_date, first_art_drugs,last_art_date,last_art_drugs
FROM 
(
    SELECT se.client_id,hiv_diagnosis_date, has_ever_been_initiated_on_art, age_group, SUBSTR(hiv_diagnosis_date, -4) AS year, enrolment_date,gender,first_art_date,first_art_drugs,last_art_date,last_art_drugs, first_art_regimen_line
    FROM fact_sentinel_event se 
    INNER JOIN dim_client c ON se.client_id = c.client_id 
    INNER JOIN ( 
                    SELECT age, TRIM(ten_year_interval) as age_group FROM dim_age_group
                ) ag ON c.current_age = ag.age
) a  