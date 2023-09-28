SELECT hotel_address, additional_number_of_scoring, review_date, average_score, hotel_name,
reviewer_nationality, negative_review, review_total_negative_word_counts, 
total_number_of_reviews, positive_review, review_total_positive_word_counts,
total_number_of_reviews_reviewer_has_given, reviewer_score, tags, days_since_review, lat, lng
FROM public.hotel_reviews
where hotel_name ='Hotel Arena'
;


SELECT additional_number_of_scoring ,review_date ,average_score ,
review_total_negative_word_counts ,total_number_of_reviews ,total_number_of_reviews_reviewer_has_given ,
reviewer_score ,days_since_review 
FROM public.hotel_reviews
where hotel_name ='Hotel Arena'
--group by hotel_name 
;

SELECT hotel_name ,reviewer_score ,count(reviewer_score)
FROM public.hotel_reviews
where hotel_name ='Hotel Arena'
group by hotel_name ,reviewer_score 
order by 2
;

