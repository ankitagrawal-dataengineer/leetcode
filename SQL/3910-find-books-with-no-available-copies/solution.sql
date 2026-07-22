select
    lb.book_id,
    lb.title,
    lb.author,
    lb.genre,
    lb.publication_year,
    lb.total_copies as current_borrowers
from library_books lb
join borrowing_records br
on 
    lb.book_id=br.book_id
where br.return_date is null
group by 
    lb.book_id,
    lb.total_copies
having 
    lb.total_copies=count(br.book_id)
order by
    current_borrowers desc,
    lb.title asc;