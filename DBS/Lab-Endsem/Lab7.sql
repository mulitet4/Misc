-- 1.
DECLARE
	r studenttable.rollno%type;
	g studenttable.gpa%type;
BEGIN
	r := &rollno;
	dbms_output.put_line('Roll Number: ' || r);
	select gpa into g from studenttable where rollno = r;
	dbms_output.put_line('GPA: ' || g);
END;
/

-- 2.
DECLARE
	r studenttable.rollno%type;
	g studenttable.gpa%type;
	gr varchar2(2);
BEGIN
	r := &rollno;
	select gpa into g from studenttable where rollno = r;
	if (g between 0 and 4) gr := 'F';
	elsif (g between 4 and 5) gr := 'E';
	.... other elsif statements ....
	elsif(g between 9 and 10) gr := 'A+';
	else gr := 'NULL';
	end if;
	dbms_output.put_line('Grade: ' || gr);
END;
/

-- 3
DECLARE
  d_issued DATE;
  d_ret DATE;
  d_late number;
  fine number;
BEGIN
  d_issued = to_date('&date_issued', 'DD-MM-YY');
  d_ret = to_date('&date_returned', 'DD-MM-YY');
  d_late = d_ret - d_issued;
  if(d_late between 0 and 7) fine := 0;
  elsif(d_late between 8 and 15) fine := (d_late - 7);
  elsif(d_late between 16 and 30) fine := (d_late - 15) * 2 + 8;
  elsif(d_late > 30) fine := (d_late - 30) * 5 + 38;
  dbms_output.put_line('Fine: ' || fine);
END;
/

-- 4
DECLARE
  g studenttable.gpa%type;
  gr varchar2(2);
BEGIN
  for i in 1..5 loop
    select gpa into g from studenttable where rollno = i;
    if (g between 0 and 4) gr := 'F';
    elsif (g between 4 and 5) gr := 'E';
    .... other elsif statements ....
    elsif(g between 9 and 10) gr := 'A+';
    else gr := 'NULL';
    end if;
    dbms_output.put_line('GPA: ' || g);
    dbms_output.put_line('Grade: ' || gr);
  end loop;
END;
/

-- 5
alter table studenttable add lettergrade varchar2(2);
DECLARE
  cursor c_stud is select rollno, gpa from studenttable;
  r studenttable.rollno%type;
  g studenttable.gpa%type;
  gr varchar2(2);
BEGIN
  open c_stud;
  fetch c_stud into r, g;
  while c_stud%found loop
    IF g < 4 THEN gr := 'F';
    ELSIF g < 5 THEN gr := 'E';
    ELSIF g < 6 THEN gr := 'D';
    ELSIF g < 7 THEN gr := 'C';
    ELSIF g < 8 THEN gr := 'B';
    ELSIF g < 9 THEN gr := 'A';
    ELSIF g <= 10 THEN gr := 'A+';
    ELSE gr := 'NULL';
    END IF;
    update studenttable set lettergrade = gr where rollno = r;
    fetch c_stud into r, g;
  end loop;
  close c_stud
end;
/

-- 6
DECLARE
  mr studenttable.rollno%type;
  mg studenttable.gpa%type;
BEGIN
  mg := 0;
  for s in (select rollno, gpa from studenttable) loop
    if(s.gpa > mg) then 
      mg := s.gpa;
      mr := s.rollno;
    end if;
  end loop;
  dbms_output.put_line('Rollno: ' || mr || ' GPA: ' || mg);
END;
/

-- 7
DECLARE
  r studenttable.rollno%type;
  g studenttable.gpa%type;
  gr varchar2(2);
  i number;
BEGIN
  i := 1;
  <<loop_student>>
  -- Letter Grade logic
  dbms_output('Rollno: ' || r || ' Grade: ' || gr);
  i = i + 1;
  if i < 6 goto loop_student; end if;
END;
/

-- 8
DECLARE
  inp_name instructor.name%type;
  c number;
  i instructor.id%type;
  dn instructor.dept_name%type;
  sal instructor.department%type;
  no_instructor exception;
  multiple_instructor exception;
BEGIN
  inp_name := &instructor_name;
  select count(id) into c from instructor where name = inp_name;
  if c = 0 then raise no_instructor;
  elsif c > 1 then raise multiple_instructor;
  select id, dept_name, salary into i, dn, sal from instructor where name = inp_name;
  -- Display details
EXCEPTION
  when no_instructor then
    dbms_output.put_line('No Instructors found');
  when multiple_instructor then
    dbms_output.put_line('Multiple Instructors found');
END;
/