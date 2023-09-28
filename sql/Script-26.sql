--select * from temp_table_1
--
--select * from temp_table_2

select * from temp_table_1 t1 left outer join temp_table_2 t2
on t1.a=t2.b