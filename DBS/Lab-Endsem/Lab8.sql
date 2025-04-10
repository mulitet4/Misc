-- 1
create table salary_raise(
  instructor_id varchar(5),
  raise_date DATE,
  raise_amt numeric(10, 2),
  foreign key (instructor_id) references instructor(id) on delete set NULL
);

DECLARE
  cursor c_instr(dn instructor.dept_name%type) is select * from instructor where dept_name = dn for update;
  inp_dn instructor.dept_name%type;
BEGIN
  inp_dn := &instructor_dept_name;
  for instr in c_instr(inp_dn) loop
    insert into salary_raise values (instr.id, sysdate, instr.salary * 0.05); 
    update instructor set salary = salary + salary * 0.05 where current of c_instr;
  end loop;
  close c_instr;
END;
/

-- 2
DECLARE
  cursor c_stud is select id, name, tot_cred from student order by tot_cred;
  v_id student.id%type;
  v_name student.name%type;
  v_totcred student.tot_cred%type;
BEGIN
  open c_stud;
  loop
    fetch c_stud into v_id, v_name, v_totcred;
    exit when c_stud%notfound or c_stud%rowcount > 10;
    dbms_output.put_line('Name: ' || v_name || 'Total Creds: ' || v_totcred);
  end loop;
  close c_stud;
END;
/

-- 3
DECLARE
  cursor c_course is 
    select c.course_id, c.title, c.dept_name, c.credits, i.instructor_name, s.building, s.room_number, s.time_slot_id, count(t.id) from course c join section s on c.course_id = s.course_id join teaches te on c.course_id = te.course_id join instructor i on te.id = i.id join takes t on c.course_id = t.course_id group by c.course_id, c.title, c.dept_name, c.credits, i.instructor_name, s.building, s.room_number, s.time_slot_id
BEGIN
  for c in c_course loop
    -- Display all the details
  end loop;
END;
/

-- 4
DECLARE
  cursor c_stud is select * from takes t natural join student s where t.course_id = 'CS101' and s.tot_cred < 30 for update;
BEGIN
  for s in c_stud loop
    delete from takes where current of c_stud;
  end loop;
END;
/

-- 5
update studenttable set lettergrade = 'F'; 
DECLARE
  cursor c_stud is select * from studenttable for update;
  gr varchar2(2);
BEGIN
  for s in c_stud loop
    if(s.gpa between 0 and 4) then gr := 'F';
    -- Other elsif statements
    elsif(s.gpa between 9 and 10) then gr := 'A+';
    else gr := 'NULL';
    update studenttable set lettergrade = gr where current of c_stud;
  end loop;
END;
/

-- 6
DECLARE
  inp_c instructor.course%type;
  cursor c_instr(c teaches.id%type) is select i.name from instructor i join teaches te on i.id = te.id where te.id=c;
BEGIN
  inp_c := &course_id;
  for i in c_instr(inp_dn) loop
    -- dbms_output.put_line(...details...);
  end loop;
END;
/

-- 7
DECLARE
  cursor c_stud is select t.id as student_id from advisor a join takes t on a.s_id = t.id join teaches te on a.t_id = te.id where te.course_id = t.course_id and te.sec_id = t.sec_id and t.semester = te.semester and t.year = te.year;
BEGIN
  for s in c_stud loop
    dbms_output.put_line('Student ID: ' || s.student_id);
  end loop;
END;
/