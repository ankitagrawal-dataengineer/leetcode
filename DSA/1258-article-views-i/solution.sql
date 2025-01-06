select author_id id from views
where author_id = viewer_id
group by author_id
order by author_id;
