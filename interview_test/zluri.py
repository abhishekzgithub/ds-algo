"""
twitter system design
"""
{
    "userid":"tweet",
    "followers":["followerid"]
}
{
    "followerid":"tweet",
    "received":["hey"]
}

#################### People
"""
+-----------+-------------------+--------+------+
| person_id | person_name       | weight | turn |
+-----------+-------------------+--------+------+
| 5         | George Washington | 250    | 1    | 250
| 3         | John Adams        | 350    | 2    |600
| 6         | Thomas Jefferson  | 400    | 3    |1000
| 2         | Will Johnliams    | 200    | 4    |
| 4         | Rich Bezos        | 175    | 5    |
| 1         | James Elephant    | 500    | 6    |
"""
######################
"""
queue, elevator to come, weight limit is 1000kg

with onboarding_people as (
select person_name, sum(weight) over( order by turn asc) as onboarding_weight_order, turn
from people p
)

select person_name
from onboarding_people
where 
onboarding_weight_order<=1000
order by turn desc
limit 1
"""

