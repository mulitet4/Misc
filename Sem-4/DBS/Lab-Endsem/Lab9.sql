-- 1
create or replace procedure message is
  BEGIN
    dbms_output.put_line('Good day to you!');
  END;
/

-- 2
create or replace procedure dept_details(dn department.dept_name%type) is
  BEGIN
    for i in (select id, name from instructor where dept_name = dn) loop
      dbms_output('Name ' || i.name);
    end loop;
    for c in (select id, title from course where dept_name = dn) loop
      dbms_output('Title: ' || title);
    end loop;
  END;
/

BEGIN
  dept_details('Comp. Sci.');
END;
/

-- 3
create or replace procedure course_popular(dn department.dept_name%type) is
  BEGIN
    declare t course.course_id%type;
    select c.course_id into t from course c join takes t on c.course_id = t.course_id where c.dept_name = dn group by c.course_id order by count(t.id) desc fetch first 1 row only;
    dbms_output.put_line('Dept Name: ' || dn || ' Course ID: ' || t);
  END;
/

create or replace procedure course_popular(dn department.dept_name%type) is
  t course.course_id%type;
  BEGIN
    select c.course_id into t from course c join takes t on c.course_id = t.course_id where c.dept_name = dn group by c.course_id having count(t.id) = (select MAX(cnt) from (
      select count(t2.id) as cnt from course c2 join takes t2 on c2.course_id = t2.course_id where c2.dept_name = dn group by c2.course_id
    ))
    dbms_output.put_line('Dept Name: ' || dn || ' Course ID: ' || t);
  END;
/

BEGIN
  for d in (select dept_name from department) loop
    course_popular(d.dept_name);
  end loop;
END;
/

-- 4
create or replace procedure dept_details2(dn department.dept_name%type) is 
  BEGIN
    for s in (select * from student where dept_name = dn) loop
      dbms_output.put_line('Name: ' || s.name);
    end loop;
    for c in (select * from course where dept_name = dn) loop
      dbms_output.put_line('Title: ' || c.title);
    end loop;
  END;
/

BEGIN
  for d in (select dept_name from department) loop
    dept_details2(dept_name);
  end loop;
END;
/

-- 5
create or replace function sq(x number)
returns number as
square number
  BEGIN
    square := x * x;
    return square;
  END;
/

BEGIN
  x := 5;
  dbms_output.put_line('Square ' || sq(5));
END;
/

-- 6
create or replace function department_highest(dn department.dept_name%type)
returns instructor.id%type as
ret_id instructor.id%type
  BEGIN
    select id into ret_id from instructor where dept_name = dn and salary = (select MAX(sal) from instructor where dept_name = dn);
    return ret_id;
  END;
/

BEGIN
  for d in (select * from department) loop
    dbms_output('Dept Name: ' || d.dept_name || ' Instructor: ' || department_highest(d.dept_name));
  end loop;
END;
/

-- 7
create or replace package dept_det as
  procedure dept_names(dn department.dept_name%type);
  function max_sal(dn department.dept_name%type) return instructor.salary%type;
end dept_det;
/

create or replace package body dept_det as
procedure dept_names(dn department.dept_name%type) is
  BEGIN
    for i in (select name from instructor where dept_name = dn) loop
      dbms_output.put_line('Name: ' || i.name);
    end loop;
  END;
function max_sal(dn department.dept_name%type) return instructor.salary%type as
sal instructor.salary%type;
  BEGIN
    select MAX(salary) into sal from instructor where dept_name = dn;
    return sal;
  END;
END dept_det;
/

BEGIN
  dept_det.dept_names('Comp. Sci.');
  dbms_output.put_line(dept_det.max_sal('Comp. Sci.'));
END;
/

-- 8
create or replace procedure interest(p in number, r in number, years in number, tot_sum in out number, simple_interest out number, compound_interest out number) as
  BEGIN
    simple_interest := (p * years * r) / 100;
    compound_interest := ();
    tot_sum := simple_interest + compound_interest;
  END;
/