--SELECT id_guest, id_host, id_listing, ts_contact_at, ts_reply_at, ts_accepted_at, ts_booking_at, ds_checkin, ds_checkout, n_guests, n_messages
--FROM public.airbnb_contacts
--
--;


select dense_rank () OVER( order by sum(n_messages) desc) as ranking, id_guest, sum(n_messages) as sum_n_messages
from public.airbnb_contacts 
group by id_guest  
order by 1 asc

