/*
 * titok_df=df_tiktok_emails.merge(df_tiktok_texts,how="left",on="email_id")

 * titok_df["signup_diff"]=titok_df.action_date-titok_df.signup_date

 * titok_df[(titok_df.signup_diff.dt.days>=1)&(titok_df.signup_action=="Confirmed")]

 */

with cte as (
select (tt.action_date::date-te.signup_date::date) as day_diff,* from tiktok_emails te left join tiktok_texts tt on te.email_id=tt.email_id
order by te.user_id, action_date asc
)
select * from cte
where day_diff>1
and signup_action='Confirmed'
--where datediff(te.signup_date,tt.action_date)
